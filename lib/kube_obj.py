# (c) Copyright 2017-2018 OLX

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import copy
import traceback
import sys
from collections import OrderedDict
from kube_help import KubeHelper

from kube_types import *
from user_error import UserError, paths as user_error_paths


def _rec_update_objs(obj):
    for k in obj._data:
        if isinstance(obj._data[k], KubeBaseObj):
            obj._data[k]._caller_file = obj._caller_file
            obj._data[k]._caller_line = obj._caller_line
            obj._data[k]._caller_fn = obj._caller_fn
            _rec_update_objs(obj._data[k])


def order_dict(src, order):
    ret = OrderedDict()
    for k in order:
        if k in src:
            ret[k] = src[k]
    if isinstance(src, OrderedDict):
        keys = src.keys()
    else:
        keys = sorted(src.keys())
    for k in keys:
        if k not in order:
            ret[k] = src[k]
    return ret


class KubeObjNoNamespace(Exception):
    pass


class KubeObjParseError(Exception):
    def __init__(self, text, obj, input_doc):
        Exception.__init__(self, text + ' parsing ' + obj.__class__.__name__)
        self.obj = obj.__class__
        self.doc = input_doc

    def __repr__(self):
        return '{}(obj={}, doc={})'.format(self.__class__.__name__, self.obj.__name__, repr(self.doc))


class KubeTypeUnresolvable(Exception):
    pass


class KubeAttributeError(UserError, AttributeError):
    pass


class KubeBaseObj(object):
    _default_ns = 'default'
    _default_cluster = None
    _uses_namespace = False
    _defaults = {}
    _types = {}
    _map = {}
    _parse = {}
    _parse_default_base = None
    _exclude = {}
    _parent_types = None
    has_metadata = False
    _is_openshift = False
    _always_regenerate = False

    def __init__(self, *args, **kwargs):
        # put the identifier in if it's specified
        if hasattr(self, 'identifier') and len(args) > 0 and self.identifier not in kwargs:
            kwargs[self.identifier] = args[0]
        self._data = self.__class__._find_defaults('_defaults')

        self._caller_file, self._caller_line, self._caller_fn = traceback.extract_stack(limit=2)[0][0:3]

        for k in self.__class__._find_defaults('_map'):
            self._data[k] = None

        self.namespace = None
        self.set_namespace(KubeBaseObj._default_ns)

        self._in_cluster = KubeBaseObj._default_cluster
        if '_no_add' not in kwargs or not kwargs['_no_add']:
            if hasattr(self, 'add_obj'):
                self.add_obj()

        if '_no_add' in kwargs:
            del kwargs['_no_add']

        if self.has_metadata:
            self.annotations = {}
            self.labels = {}

        if hasattr(self, 'early_init'):
            self.early_init(*args, **kwargs)

        for k in kwargs:
            if self.has_metadata and k in ('annotations', 'labels'):
                setattr(self, k, kwargs[k])
                continue

            if k not in self._data:
                raise UserError(TypeError("{} is not a valid argument for {} constructor".format(
                                          k, self.__class__.__name__)))

            if not isinstance(kwargs[k], (list, dict)):
                self._data[k] = kwargs[k]
            elif isinstance(kwargs[k], list):
                self._data[k] = []
                self._data[k].extend(kwargs[k])
            else:
                if not isinstance(self._data[k], dict):
                    self._data[k] = {}
                self._data[k].update(kwargs[k])

        _rec_update_objs(self)

    def clone(self, *args, **kwargs):
        ret = self._clone()
        ret._caller_file, ret._caller_line, ret._caller_fn = traceback.extract_stack(limit=2)[0][0:3]
        _rec_update_objs(self)

        if hasattr(self, 'identifier') and len(args) > 0 and self.identifier not in kwargs:
            kwargs[self.identifier] = args[0]

        for k in kwargs:
            if self.has_metadata and k in ('annotations', 'labels'):
                setattr(self, k, kwargs[k])
                continue

            if k not in ret._data:
                raise UserError(TypeError("{} is not a valid argument for {} constructor".format(
                                          k, ret.__class__.__name__)))

            if not isinstance(kwargs[k], (list, dict)):
                ret._data[k] = kwargs[k]
            elif isinstance(kwargs[k], list):
                ret._data[k] = []
                ret._data[k].extend(kwargs[k])
            else:
                if not isinstance(ret._data[k], dict):
                    ret._data[k] = {}
                ret._data[k].update(kwargs[k])

        return ret

    def _clone(self):
        ret = self.__class__()

        for k in self._data:
            if isinstance(self._data[k], KubeBaseObj):
                ret._data[k] = self._data[k]._clone()
            else:
                ret._data[k] = copy.deepcopy(self._data[k])

        if self.has_metadata:
            ret.annotations = copy.deepcopy(self.annotations)
            ret.labels = copy.deepcopy(self.labels)

        return ret

    @classmethod
    def _find_defaults(cls, clsmap):
        ret = {}
        def _recurse(kls):
            if not (len(kls.__bases__) == 0 or (len(kls.__bases__) == 1 and kls.__bases__[0] is object)):
                for c in kls.__bases__:
                    _recurse(c)
            if hasattr(kls, clsmap):
                ret.update(copy.deepcopy(getattr(kls, clsmap)))
        _recurse(cls)
        if hasattr(cls, 'identifier'):
            if clsmap == '_types' and cls.identifier not in ret:
                ret[cls.identifier] = Identifier
            elif clsmap == '_defaults':
                # we always set the identifier to be none as a default
                ret[cls.identifier] = None
        return ret

    def set_namespace(self, name):
        if hasattr(self, 'get_ns'):
            self.namespace = self.get_ns(name)

    def check_namespace(self):
        return True

    def do_validate(self):
        return True

    @classmethod
    def resolve_types(cls):
        if not hasattr(cls, '_resolved_types'):
            def basic_validation(typ):
                if isinstance(typ, KubeType):
                    return typ
                elif isinstance(typ, (type, KubeBaseObj)):
                    return KubeType.construct_arg(typ)
                elif Integer().do_check(typ, None):
                    if typ > 0:
                        return Positive(NonZero(Integer))
                    elif typ < 0:
                        return NonZero(Integer)
                    return Integer()
                elif Number().do_check(typ, None):
                    if typ > 0:
                        return Positive(Number)
                    return Number()
                elif Boolean().do_check(typ, None):
                    return Boolean()
                elif String().do_check(typ, None):
                    return NonEmpty(String)
                return None

            types = cls._find_defaults('_defaults')
            types.update(cls._find_defaults('_types'))

            for k in types:
                t = basic_validation(types[k])
                if t is not None:
                    types[k] = t
                elif isinstance(types[k], (list, tuple)):
                    if len(types[k]) > 0:
                        t = basic_validation(types[k][0])
                        if t is not None:
                            types[k] = NonEmpty(List(t))
                elif isinstance(types[k], dict):
                    if len(types[k]) > 0:
                        kk = tuple(types[k].keys())[0]
                        vv = types[k][kk]
                        tk = basic_validation(kk)
                        tv = basic_validation(vv)
                        if tk is not None and tv is not None:
                            types[k] = NonEmpty(Map(tk, tv))

                if not isinstance(types[k], KubeType):
                    raise KubeTypeUnresolvable(
                        "Couldn't resolve (from {}) {} into a default type".format(k, repr(types[k])))

            cls._resolved_types = types

        return cls._resolved_types

    @classmethod
    def get_child_types(cls):
        types = cls.resolve_types()
        ret = {}
        for t in types.values():
            actual_type = t.original_type()
            if actual_type is None:
                continue
            if isinstance(actual_type, list):
                actual_type = actual_type[0]
            elif isinstance(actual_type, dict):
                actual_type = actual_type['value']
            ret[actual_type.__name__] = actual_type
        return ret

    @classmethod
    def is_abstract_type(cls):
        base = KubeBaseObj.render
        this = cls.render
        if hasattr(base, '__func__') and hasattr(this, '__func__'):
            # python 2.7
            return this.__func__ is base.__func__
        # python 3
        return this is base

    @classmethod
    def get_subclasses(cls, non_abstract=True, include_self=False, depth_first=False):
        def _rec_subclasses(kls):
            ret = []
            subclasses = kls.__subclasses__()
            if len(subclasses) > 0:
                if depth_first:
                    for c in subclasses:
                        ret.extend(_rec_subclasses(c))

                if non_abstract:
                    ret.extend(filter(lambda x: not x.is_abstract_type(), subclasses))
                else:
                    ret.extend(subclasses)

                if not depth_first:
                    for c in subclasses:
                        ret.extend(_rec_subclasses(c))

            return ret

        ret = _rec_subclasses(cls)
        if include_self and not(non_abstract and cls.is_abstract_type()):
            if depth_first:
                ret.append(cls)
            else:
                ret.insert(0, cls)

        return ret

    @classmethod
    def get_help(cls):
        document_link = cls._document_url if hasattr(cls, '_document_url') else None
        
        ret_help = KubeHelper(
            name=cls.__name__,
            document=cls.__doc__,
            documentlink=document_link
            )

        def _rec_superclasses(kls):
            ret = []
            superclasses = list(filter(lambda x: x is not KubeBaseObj and x is not KubeSubObj and
                                                 x is not KubeObj and x is not object,
                                       kls.__bases__))

            if len(superclasses) > 0:
                ret.extend(superclasses)
                for c in superclasses:
                    ret.extend(_rec_superclasses(c))

            return ret

        ret_help.class_subclasses = list(map(lambda x: x.__name__, cls.get_subclasses(non_abstract=False, include_self=False)))
        ret_help.class_superclasses = list(map(lambda x: x.__name__, _rec_superclasses(cls)))

        ret_help.class_types = cls.resolve_types()

        ret_help.class_is_abstract = cls.is_abstract_type()
        ret_help.class_identifier = cls.identifier if hasattr(cls, 'identifier') and cls.identifier is not None else None

        mapping = cls._find_defaults('_map')
        ret_help.class_mapping = {}
        for d in mapping:
            if mapping[d] not in ret_help.class_mapping:
                ret_help.class_mapping[mapping[d]] = []
            ret_help.class_mapping[mapping[d]].append(d)

        ret_help.class_parent_types = cls._parent_types
        ret_help.class_has_metadata = cls.has_metadata

        ret_help.class_xf_detail = {}
        for p in ret_help.class_types:
            if hasattr(cls, 'xf_' + p):
                ret_help.class_xf_detail[p] = '<unknown transformation>'
                if hasattr(getattr(cls, 'xf_' + p), '__doc__') and getattr(cls, 'xf_' + p).__doc__ is not None and len(getattr(cls, 'xf_' + p).__doc__):
                    ret_help.class_xf_detail[p] = getattr(cls, 'xf_' + p).__doc__

        return ret_help

    def has_child_object(self, obj):
        assert isinstance(obj, KubeBaseObj)
        for d in self._data:
            if obj is self._data[d]:
                return True
        return False

    def update(self, **kwargs):
        bad_args = set()
        for k in kwargs:
            if k in self._data:
                continue
            if self.has_metadata and k in ('labels', 'annotations'):
                continue
            bad_args.add(k)
        if len(bad_args) != 0:
            raise UserError(KeyError("{} isn't/aren't attributes of {}".format(
                ', '.join(map(lambda x: "'{}'".format(x), sorted(bad_args))),
                self.__class__.__name__)))
        for k in kwargs:
            if k in self._data:
                self._data[k] = kwargs[k]
            else:
                self.__setattr__(k, kwargs[k])

    def validate(self, path=None):
        if path is None:
            path = 'self'

        types = self.__class__.resolve_types()
        mapping = self.__class__._find_defaults('_map')

        if hasattr(self, 'labels'):
            Map(String, String).check(self.labels, '{}.(labels)'.format(path))
        if hasattr(self, 'annotations'):
            Map(String, String).check(self.annotations, '{}.(annotations)'.format(path))

        if not self.check_namespace():
            raise UserError(KubeObjNoNamespace("No namespace attached to object at {}".format(path)))

        data = self.xform()

        for k in types:
            if k in data:
                types[k].check(data[k], path + '.' + k)
            else:
                types[k].check(None, path + '.' + k)

        for k in data:
            if k not in types and k not in mapping:
                raise KubeTypeUnresolvable(
                    "Unknown data key {} - no type information".format(k))

        sav_data = self._data
        try:
            self._data = data
            return self.do_validate()
        finally:
            self._data = sav_data

    def render(self):
        raise NotImplementedError('method not implemented')

    def find_subparser(self, doc):
        return self.__class__

    def parser(self, doc):
        if doc is None:
            return None

        if not isinstance(doc, dict):
            raise UserError(KubeObjParseError('Expecting to parse objects as dicts', self, doc))

        kls = self.find_subparser(doc)

        if kls is None:
            raise UserError(KubeObjParseError(
                "Unable to identify correct subtype from {}".format(self.__class__.__name__), self, doc))

        if kls is not self.__class__:
            return kls().parser(doc)

        mapping = self.__class__._find_defaults('_map')
        self._data = self.__class__._find_defaults('_defaults')
        for k in mapping:
            self._data[k] = None

        expl = {}

        if self.has_metadata and 'metadata' in doc:
            expl['metadata'] = {'labels': True, 'annotations': True}
            if 'labels' in doc['metadata']:
                self.labels = copy.deepcopy(doc['metadata']['labels'])
            if 'annotations' in doc['metadata']:
                self.annotations = copy.deepcopy(doc['metadata']['annotations'])
        if hasattr(self, 'identifier') and self.identifier == 'name' and \
                'metadata' in doc and 'name' in doc['metadata']:
            self._data['name'] = doc['metadata']['name']
            if 'metadata' not in expl:
                expl['metadata'] = {}
            expl['metadata'].update({'name': True})

        if hasattr(self, 'apiVersion') and hasattr(self, 'kind'):
            expl['apiVersion'] = True
            if 'apiVersion' not in doc:
                raise UserError(KubeObjParseError('Expected apiVersion - no apiVersion found', self, doc))

            expl['kind'] = True
            if 'kind' not in doc:
                raise UserError(KubeObjParseError('Expected kind - no kind found', self, doc))

        types = self.__class__.resolve_types()
        parser = self.__class__._find_defaults('_parse')
        exclude = self.__class__._find_defaults('_exclude')

        if self.has_metadata:
            exclude['.metadata.creationTimestamp'] = True

        def do_parse(k, v):
            if k in mapping:
                o_typ = types[mapping[k]].original_type()
            else:
                o_typ = types[k].original_type()
            if o_typ is None:
                self._data[k] = copy.deepcopy(v)
            elif isinstance(o_typ, list):
                if isinstance(v, list):
                    self._data[k] = []
                    for el in v:
                        self._data[k].append(o_typ[0]().parser(el))
                else:
                    self._data[k] = copy.deepcopy(v)
            elif isinstance(o_typ, dict):
                if isinstance(v, dict):
                    self._data[k] = {}
                    for kk in v:
                        self._data[k][kk] = o_typ['value']().parser(v[kk])
                else:
                    self._data[k] = copy.deepcopy(v)
            else:
                self._data[k] = o_typ().parser(v)

        if hasattr(self, 'pre_parse_fixup'):
            try:
                doc = self.pre_parse_fixup(doc)
            except Exception as e:
                raise UserError(KubeObjParseError(
                    'Fixup failed: {}: {}'.format(e.__class__.__name__, str(e)), self, doc))

        if self._parse_default_base is not None:
            for k in types:
                if k not in parser:
                    t = list(self._parse_default_base)
                    t.append(k)
                    parser[k] = tuple(t)

            for k in mapping:
                if k not in parser:
                    t = list(self._parse_default_base)
                    t.append(k)
                    parser[k] = tuple(t)

        for k in types:
            if k not in parser and k in doc:
                do_parse(k, doc[k])
                expl[k] = True

        for k in mapping:
            if k not in parser and k in doc:
                do_parse(k, doc[k])
                expl[k] = True

        for k in parser:
            lcn = doc
            elcn = expl
            try:
                for i in parser[k][:-1]:
                    lcn = lcn[i]
                    if i not in elcn:
                        elcn[i] = {}
                    elcn = elcn[i]
                lcn = lcn[parser[k][-1]]
            except:
                lcn = None

            if lcn is not None:
                do_parse(k, lcn)
                elcn[parser[k][-1]] = True

        def rec_find_unparsed(expl, doc, path='.'):
            ret = []
            for k in doc:
                if path == '.':
                    npath = '.' + k
                else:
                    npath = path + '.' + k

                if npath in exclude and exclude[npath]:
                    continue

                if k in expl:
                    if isinstance(doc[k], dict) and isinstance(expl[k], dict):
                        ret.extend(rec_find_unparsed(expl[k], doc[k], npath))
                        continue
                    elif expl[k] == True:
                        continue
                ret.append(npath)
            return ret

        for i in rec_find_unparsed(expl, doc):
            print("Warning unparsed {}: {}".format(self.__class__.__name__, i), file=sys.stderr)

        if hasattr(self, 'parser_fixup'):
            self.parser_fixup()

        return self

    def dump_obj(self, indent=0, include_defaults=False):
        defaults = self.__class__._find_defaults('_defaults')
        mapping = self.__class__._find_defaults('_map')

        def eline(obj, pfx, idt, idt_txt, comma):
            if isinstance(obj, KubeBaseObj):
                return idt_txt + pfx + obj.dump_obj(idt, include_defaults) + comma
            elif isinstance(obj, dict):
                return idt_txt + pfx + dump_dict(obj, idt) + comma
            elif isinstance(obj, list):
                return idt_txt + pfx + dump_list(obj, idt) + comma
            else:
                return idt_txt + pfx + repr(obj) + comma

        def dump_dict(v, idt):
            if len(v) == 0:
                return '{}'
            elif len(v) == 1:
                text = ''
                args = (idt, '', '')
            else:
                text = '\n'
                args = (idt + 4, ' ' * (idt + 4), ',\n')

            for i in sorted(v.keys()):
                text += eline(v[i], repr(i) + ': ', *args)

            return '{' + text + args[1] + '}'

        def dump_list(v, idt):
            if len(v) == 0:
                return '[]'
            elif len(v) == 1:
                text = ''
                args = (idt, '', '')
            else:
                text = '\n'
                args = (idt + 4, ' ' * (idt + 4), ',\n')

            for i in v:
                text += eline(i, '', *args)

            return '[' + text + args[1] + ']'

        has_data = 0
        if hasattr(self, 'identifier') and self._data[self.identifier] is not None:
            has_data += 1

        if self.has_metadata and (not isinstance(self.annotations, dict) or len(self.annotations) != 0):
            has_data += 1

        if self.has_metadata and (not isinstance(self.labels, dict) or len(self.labels) != 0):
            has_data += 1

        for k in self._data.keys():
            if hasattr(self, 'identifier') and k == self.identifier:
                continue

            if k in mapping:
                continue

            if include_defaults or k not in defaults or self._data[k] != defaults[k]:
                has_data += 1

        if has_data == 0:
            return self.__class__.__name__ + '()'

        if has_data == 1:
            text = ''
            args = (indent, '', '')
        else:
            text = '\n'
            args = (indent + 4, ' ' * (indent + 4), ',\n')

        if hasattr(self, 'identifier') and self._data[self.identifier] is not None:
            text += eline(self._data[self.identifier], '', *args)

        if self.has_metadata and (not isinstance(self.annotations, dict) or len(self.annotations) != 0):
            text += eline(self.annotations, 'annotations=', *args)

        if self.has_metadata and (not isinstance(self.labels, dict) or len(self.labels) != 0):
            text += eline(self.labels, 'labels=', *args)

        for k in sorted(self._data.keys()):
            if hasattr(self, 'identifier') and k == self.identifier:
                continue

            if k in mapping:
                continue

            if include_defaults or k not in defaults or self._data[k] != defaults[k]:
                text += eline(self._data[k], k + '=', *args)

        return self.__class__.__name__ + '(' + text + args[1] + ')'

    def get_obj(self, prop, *args, **kwargs):
        types = self.__class__.resolve_types()

        mapping = self.__class__._find_defaults('_map')
        if prop in mapping:
            prop = mapping[prop]

        fmt = (prop, self.__class__.__name__)
        if prop not in types:
            raise KeyError("No such property '{}' on {}".format(*fmt))

        typ = types[prop]

        actual_type = typ.original_type()
        if actual_type is None:
            raise UserError(KeyError("Property '{}' can't be auto-constructed in {}".format(*fmt)))

        rtype = None
        if isinstance(actual_type, list):
            actual_type = actual_type[0]
            rtype = 'list'
        elif isinstance(actual_type, dict):
            actual_type = actual_type['value']
            rtype = 'dict'
        else:
            rtype = 'obj'

        if not isinstance(actual_type, type):
            raise TypeError("Unexpected type isn't a type is actually a {} for property '{}' in {}".
                            format(actual_type.__class__.__name__, *fmt))

        if not any(map(lambda x: x is actual_type,
                       KubeBaseObj.get_subclasses(non_abstract=False, include_self=False))):
            raise TypeError("Unexpected type {} for property '{}' in {}, must be a subclass of KubeBaseObj".
                            format(actual_type.__name__, *fmt))

        if len(args) > 0 and isinstance(args[0], type):
            if any(map(lambda x: x is args[0],
                       actual_type.get_subclasses(non_abstract=True, include_self=True))):
                actual_type = args[0]
                args = args[1:]
            else:
                raise UserError(TypeError(("Unexpected type as first argument for property '{}' in {}, must be subclass " +
                                           "of {}. Valid types are: {}").
                                           format(prop, self.__class__.__name__, actual_type.__name__,
                                                  ", ".join(map(lambda x: x.__name__,
                                                                actual_type.get_subclasses(
                                                                    non_abstract=True, include_self=True))))))

        if actual_type.is_abstract_type():
            raise UserError(TypeError("Can't construct {} for '{}' in {}, you probably want one of: {}".
                                      format(actual_type.__name__, prop, self.__class__.__name__,
                                             ", ".join(map(lambda x: x.__name__,
                                                           actual_type.get_subclasses(non_abstract=True))))))

        if rtype == 'dict':
            if len(args) == 0:
                raise UserError(ValueError("Must supply key for newly constructed property '{}' on {}".format(*fmt)))
            dkey = args[0]
            args = args[1:]

        result = actual_type(*args, **kwargs)

        new = result
        if rtype == 'list':
            new = [result]
        elif rtype == 'dict':
            new = {dkey: result}

        if self._data[prop] is None or rtype == 'obj':
            self._data[prop] = new
            return result

        if rtype == 'list' and isinstance(self._data[prop], list):
            self._data[prop].extend(new)
        elif rtype == 'dict' and isinstance(self._data[prop], dict):
            self._data[prop].update(new)
        else:
            raise UserError(TypeError("Expecting {} or None for property '{}' on {}".format(rtype, *fmt)))

        return result

    def renderer(self, zlen_ok=(), order=(), mapping=None, return_none=False):
        ret = copy.deepcopy(self._data)

        def _render(x):
            if isinstance(x, KubeBaseObj):
                return x.do_render()
            return x

        for r in self._data:
            res = _render(ret[r])
            if res is None:
                del ret[r]
            else:
                ret[r] = res

        for r in self._data:
            if r not in ret:
                continue

            if isinstance(ret[r], (list, tuple)):
                ret[r] = list(filter(lambda x: x is not None, map(_render, ret[r])))
            elif isinstance(ret[r], dict):
                tret = OrderedDict()
                keys = ret[r].keys()
                if not isinstance(ret[r], OrderedDict):
                    keys = sorted(keys)
                for k in keys:
                    res = _render(ret[r][k])
                    if res is not None:
                        tret[k] = res
                ret[r] = tret

            if isinstance(ret[r], (list, tuple, dict)):
                if len(ret[r]) == 0 and r not in zlen_ok:
                    del ret[r]

        if mapping is not None:
            for k in mapping:
                if k in ret:
                    if mapping[k] is not None:
                        ret[mapping[k]] = ret[k]
                    del ret[k]

        if return_none and len(ret) == 0:
            return None

        if len(order) != 0:
            return order_dict(ret, order)

        return order_dict(ret, ())

    def xform(self):
        ret = {}
        mapping = self.__class__._find_defaults('_map')

        for d in self._data:
            if hasattr(self, 'xf_{}'.format(d)):
                ret[d] = getattr(self, 'xf_{}'.format(d))(self._data[d])
            elif d in mapping and hasattr(self, 'xf_{}'.format(mapping[d])):
                ret[d] = getattr(self, 'xf_{}'.format(mapping[d]))(self._data[d])
            else:
                ret[d] = self._data[d]

        for d in mapping:
            if d not in ret or ret[d] is None:
                continue
            if mapping[d] in ret and ret[mapping[d]] is None:
                ret[mapping[d]] = ret[d]
            del ret[d]

        return ret

    def do_render(self):
        self.validate()

        sav_data = self._data
        try:
            self._data = self.xform()
            obj = self.render()
        finally:
            self._data = sav_data

        if obj is None:
            return None

        if hasattr(self, 'apiVersion') and hasattr(self, 'kind'):
            ret = OrderedDict(apiVersion=self.apiVersion)
            ret['kind'] = self.kind
        else:
            ret = OrderedDict()

        if self.has_metadata:
            if 'metadata' in obj:
                if 'labels' in obj['metadata']:
                    obj['metadata']['labels'].update(self.labels)
                    if hasattr(self, 'identifier'):
                        obj['metadata']['labels'] = order_dict(obj['metadata']['labels'], (self.identifier,))
                elif len(self.labels) != 0:
                    obj['metadata']['labels'] = copy.copy(self.labels)

                if 'annotations' in obj['metadata']:
                    obj['metadata']['annotations'].update(self.annotations)
                elif len(self.annotations) != 0:
                    obj['metadata']['annotations'] = copy.copy(self.annotations)

                if self._uses_namespace and hasattr(self, 'namespace') and self.namespace is not None:
                    obj['metadata']['namespace'] = self.namespace.name

                if hasattr(self, 'identifier'):
                    obj['metadata'] = order_dict(obj['metadata'], (self.identifier, 'namespace', 'annotations', 'labels'))
                else:
                    obj['metadata'] = order_dict(obj['metadata'], ('annotations', 'labels'))

            elif len(self.labels) != 0 or len(self.annotations) != 0:
                obj['metadata'] = {}
                if len(self.labels) != 0:
                    obj['metadata']['labels'] = copy.copy(self.labels)
                if len(self.annotations) != 0:
                    obj['metadata']['annotations'] = copy.copy(self.annotations)

            obj = order_dict(obj, ('metadata', 'spec'))

        if hasattr(self, 'identifier'):
            obj = order_dict(obj, (self.identifier,))

        ret.update(obj)
        return ret

    def __getattr__(self, k):
        if k != '_data' and hasattr(self, '_data') and k in self._data:
            return self._data[k]
        if k.startswith('new_') and k[4:] in self._data:
            def get_prop(*args, **kwargs):
                return self.get_obj(k[4:], *args, **kwargs)
            get_prop.__name__ = k
            return get_prop
        elif k.startswith('new_') and k[4:] + 's' in self._data:
            def get_prop(*args, **kwargs):
                return self.get_obj(k[4:] + 's', *args, **kwargs)
            get_prop.__name__ = k
            return get_prop
        raise KubeAttributeError(AttributeError('No such attribute {} for {}'.format(k, self.__class__.__name__)))

    def __setattr__(self, k, v):
        if k in ('_data',):
            pass
        elif k in self._data:
            return self._data.__setitem__(k, v)
        if k in ('labels', 'annotations', 'namespace'):
            return object.__setattr__(self, k, v)

        fn = traceback.extract_stack(limit=2)[0][0]
        for p in user_error_paths:
            if fn.startswith(p + '/'):
                return object.__setattr__(self, k, v)

        raise KubeAttributeError(AttributeError('No such attribute {} for {}'.format(k, self.__class__.__name__)))

    def __getitem__(self, k):
        if not k in self._data:
            raise UserError(KeyError("key {} is not defined for {}".format(k, self.__class__.__name__)))
        return self._data.__getitem__(k)

    def __setitem__(self, k, v):
        if not k in self._data:
            raise UserError(KeyError("key {} is not defined for {}".format(k, self.__class__.__name__)))
        return self._data.__setitem__(k, v)


class KubeObj(KubeBaseObj):
    identifier = 'name'
    has_metadata = True
    _uses_namespace = True
    _output_order = 100
    _kind_subclasses = None

    _exclude = {
        '.metadata.generation': True,
        '.metadata.namespace': True,
        '.metadata.resourceVersion': True,
        '.metadata.selfLink': True,
        '.metadata.uid': True,
        }

    @classmethod
    def is_abstract_type(cls):
        if not hasattr(cls, 'apiVersion') or not hasattr(cls, 'kind'):
            return True
        base = KubeBaseObj.render
        this = cls.render
        if hasattr(base, '__func__') and hasattr(this, '__func__'):
            # python 2.7
            return this.__func__ is base.__func__
        # python 3
        return this is base

    @classmethod
    def find_class_from_obj(cls, doc):
        if cls is not KubeObj:
            return KubeObj.find_class_from_obj(doc)

        if cls._kind_subclasses is None:
            def rec_get_subclass_by_kind(kls):
                ret = {}
                for c in kls.__subclasses__():
                    r = rec_get_subclass_by_kind(c)
                    ret.update(r)

                if hasattr(kls, 'apiVersion') and hasattr(kls, 'kind'):
                    ret[kls.kind] = kls

                return ret
            cls._kind_subclasses = rec_get_subclass_by_kind(cls)

        if not isinstance(doc, dict) or 'kind' not in doc or 'apiVersion' not in doc:
            return None

        if doc['kind'] in cls._kind_subclasses:
            return cls._kind_subclasses[doc['kind']]

        return None

    @classmethod
    def parse_obj(cls, doc):
        if cls is not KubeObj:
            raise ValueError(".parse_obj should only be called as KubeObj.parse_obj(...)")

        if not isinstance(doc, dict) or 'kind' not in doc or 'apiVersion' not in doc:
            raise UserError(ValueError(
                "Document needs to be a dictionary with 'kind' and 'apiVersion' as top-level keys"))

        my_cls = cls.find_class_from_obj(doc)

        if my_cls is not None:
            return my_cls().parser(doc)

        raise UserError(ValueError(
            "Unknown document kind: {}, no corresponding rubiks object found".format(doc['kind'])))

    def check_namespace(self):
        if isinstance(self.namespace, KubeObj) and hasattr(self.namespace, 'kind') and \
                self.namespace.kind in ('Namespace', 'Project'):
            return True
        return False

    def early_init(self, *args, **kwargs):
        if not hasattr(self, 'apiVersion') or not hasattr(self, 'kind') or not hasattr(self, 'identifier'):
            raise TypeError(
                "Class {} is an abstract base class and can't be instantiated".format(
                    self.__class__.__name__))


class KubeSubObj(KubeBaseObj):
    pass
