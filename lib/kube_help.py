# (c) Copyright 2018-2019 OLX

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from kube_types import Map, String


# Object used to collect class definition and implement the rendering functions
class KubeHelper(object):
    # Internal data structure to store needed data
    _data = {}
    # List of all needed field to have
    _defaults = {
        'class_name': None,
        'class_subclasses': [],
        'class_superclasses': None,
        'class_types': {},
        'class_is_abstract': None,
        'class_identifier': None,
        'class_mapping': [],
        'class_parent_types': None,
        'class_has_metadata': None,
        'class_doc': None,
        'class_doc_link': None,
        'class_xf_hasattr': [],
        'class_xf_detail': []
    }
    # definition of mandatory field to display
    _mandatory = {
        'class_name': True,
        'class_subclasses': False,
        'class_superclasses': False,
        'class_types': False,
        'class_is_abstract': True,
        'class_identifier': False,
        'class_mapping': False,
        'class_parent_types': False,
        'class_has_metadata': True,
        'class_doc': False,
        'class_doc_link': False,
        'class_xf_hasattr': False,
        'class_xf_detail': False
    }

    def __init__(self, *args, **kwargs):
        self._defaults_creations()

        if 'name' in kwargs:
            self.class_name = kwargs['name']
        if 'document' in kwargs:
            self.class_doc = kwargs['document']
        if 'documentlink' in kwargs:
            self.class_doc_link = kwargs['documentlink']

    def _defaults_creations(self):
        for name in getattr(self, '_defaults'):
            if name in self._mandatory:
                self._data[name] = self._defaults[name]
            else:
                raise Exception('Missing mandatory information for {} inside {} class'.format(name, self.__class__.__name__))

    def __getattr__(self, name):
        if name in getattr(self, '_data'):
            return self._data[name]
        else:
            raise ValueError

    def __setattr__(self, name, value):
        if name in getattr(self, '_data'):
            self._data[name] = value
        else:
            raise ValueError

    def render_terminal(self):
        txt = '{}{}:\n'.format(self.class_name, self.class_is_abstract)

        if len(self.class_superclasses) != 0:
            txt += '  parents: {}\n'.format(', '.join(self.class_superclasses))
        if len(self.class_subclasses) != 0:
            txt += '  children: {}\n'.format(', '.join(self.class_subclasses))
        if len(self.class_parent_types) != 0:
            txt += '  parent types: {}\n'.format(', '.join(sorted(self.class_parent_types.keys())))
        if self.class_has_metadata:
            txt += '  metadata:\n'
            txt += '    annotations:          {}\n'.format(Map(String, String).name())
            txt += '    labels:               {}\n'.format(Map(String, String).name())
        txt += '  properties:\n'
        if self.class_identifier is not None:
            spc = ''
            if len(self.class_identifier) < 7:
                spc = (7 - len(self.class_identifier)) * ' '
            txt += '    {} (identifier): {}{}\n'.format(self.class_identifier, spc, self.class_types[self.class_identifier].name())

        for p in sorted(self.class_types.keys()):
            if p == self.class_identifier:
                continue
            spc = ''
            if len(p) < 20:
                spc = (20 - len(p)) * ' '
            xf = '*' if 'xf_{}'.format(p) in self.class_xf_hasattr else ' '

            txt += '   {}{}: {}{}\n'.format(xf, p, spc, self.class_types[p].name())
            if p in self.class_mapping:
                txt += '      ({})\n'.format(', '.join(self.class_mapping[p]))

        return txt

    
    def _get_markdown_link(self, objects):
        if isinstance(objects, list):
            return ['[{}](#{})'.format(classname, classname.lower()) for classname in objects]
        else:
            return '[{}](#{})'.format(objects, objects.lower())

    def _docstring_formatter(self):
        return '\n'.join([line.strip() for line in self.class_doc.split('\n')])

    def render_markdown(self):
        # Title generation based on link
        if self.class_doc_link is not None:
            txt = '## [{}]({})\n'.format(self.class_name, self.class_doc_link)
        else:
            txt = '## {}\n'.format(self.class_name)

        # Add class doc string if exists
        if self.class_doc is not None:
            txt += '\n{}\n'.format(self._docstring_formatter())

        # Parents
        if len(self.class_superclasses) != 0:
            txt += '#### Parents: \n'
            for obj in self._get_markdown_link(self.class_superclasses):
                txt += '- {}\n'.format(obj)

        # Children
        if len(self.class_subclasses) != 0:
            txt += '####  Children: \n'
            for obj in self._get_markdown_link(self.class_subclasses):
                txt += '- {}\n'.format(obj)

        # Parent types
        if len(self.class_parent_types) != 0:
            txt += '####  Parent types: \n'
            for obj in self._get_markdown_link(sorted(self.class_parent_types.keys())):
                txt += '- {}\n'.format(obj)

        # Metadata
        if self.class_has_metadata:
            txt += '#### Metadata\n'
            txt += 'Name | Format\n'
            txt += '---- | ------\n'
            txt += 'annotations | {}\n'.format(Map(String, String).name())
            txt += 'labels | {}\n'.format(Map(String, String).name())

        # Properties table
        if len(self.class_types.keys()) == 0:
            return txt

        txt += '####  Properties:\n\n'
        txt += 'Name | Type | Identifier | Type Transformation | Aliases\n'
        txt += '---- | ---- | ---------- | ------------------- | -------\n'
        if self.class_identifier is not None:
            txt += '{} | {} | True | - | - \n'.format(self.class_identifier, self.class_types[self.class_identifier].name())
            
        for p in sorted(self.class_types.keys()):
            if p == self.class_identifier:
                continue

            # Prepare Type transformation and remove special character that could ruin visualization in markdown
            xf_data = self.class_xf_detail[p] if p in self.class_xf_detail else '-'
            xf_data = xf_data.replace('<', '&lt;').replace('>', '&gt;')

            is_mapped = ', '.join(self._get_markdown_link(self.class_mapping[p])) if p in self.class_mapping else '-'

            original_type = self.class_types[p].original_type()
            display_type = self.class_types[p].name().replace('<', '&lt;').replace('>', '&gt;')

            if original_type is not None:
                if isinstance(original_type, list):
                    original_type = original_type[0]
                elif isinstance(original_type, dict):
                    original_type = original_type['value']
                classname = original_type.__name__
                display_type = display_type.replace(classname, self._get_markdown_link(classname))
            
            
            txt += '{} | {} | False | {} | {} \n'.format(p, display_type, xf_data, is_mapped)

        return txt
        