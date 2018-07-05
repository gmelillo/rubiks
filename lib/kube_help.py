# (c) Copyright 2018-2019 OLX

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from kube_types import Map, String


# Object used to collect class definition and implement the rendering functions
class KubeHelper(object):
    _class_name = None
    _class_subclasses = []
    _class_superclasses = None
    _class_types = {}
    _class_is_abstract = None
    _class_identifier = None
    _class_mapping = []
    _class_parent_types = None
    _class_has_metadata = None
    _class_doc = None
    _class_doc_link = None
    _class_xf_hasattr = []

    def __init__(self, *args, **kwargs):
        if 'name' in kwargs:
            self._class_name = kwargs['name']
        if 'document' in kwargs:
            self._class_doc = kwargs['document']
        if 'documentlink' in kwargs:
            self._class_doc_link = kwargs['documentlink']

    def render_terminal(self):
        txt = '{}{}:\n'.format(self._class_name, self._class_is_abstract)

        if len(self._class_superclasses) != 0:
            txt += '  parents: {}\n'.format(', '.join(self._class_superclasses))
        if len(self._class_subclasses) != 0:
            txt += '  children: {}\n'.format(', '.join(self._class_subclasses))
        if len(self._class_parent_types) != 0:
            txt += '  parent types: {}\n'.format(', '.join(sorted(self._class_parent_types.keys())))
        if self._class_has_metadata:
            txt += '  metadata:\n'
            txt += '    annotations:          {}\n'.format(Map(String, String).name())
            txt += '    labels:               {}\n'.format(Map(String, String).name())
        txt += '  properties:\n'
        if self._class_identifier is not None:
            spc = ''
            if len(self._class_identifier) < 7:
                spc = (7 - len(self._class_identifier)) * ' '
            txt += '    {} (identifier): {}{}\n'.format(self._class_identifier, spc, self._class_types[self._class_identifier].name())

        for p in sorted(self._class_types.keys()):
            if p == self._class_identifier:
                continue
            spc = ''
            if len(p) < 20:
                spc = (20 - len(p)) * ' '
            xf = '*' if 'xf_{}'.format(p) in self._class_xf_hasattr else ' '

            txt += '   {}{}: {}{}\n'.format(xf, p, spc, self._class_types[p].name())
            if p in self._class_mapping:
                txt += '      ({})\n'.format(', '.join(self._class_mapping[p]))

        return txt

    
    def _get_markdown_link(self, objects):
        return ['[{}](#{})'.format(classname, classname.lower()) for classname in objects]

    def render_markdown(self):
        # Title generation based on link
        if self._class_doc_link is not None:
            txt = '## [{}]({})\n'.format(self._class_name, self._class_doc_link)
        else:
            txt = '## {}\n'.format(self._class_name)

        # Add class doc string if exists
        if self._class_doc is not None:
            txt += '\n{}\n---\n'.format(self._class_doc)

        # Parents
        if len(self._class_superclasses) != 0:
            txt += '#### Parents: {}\n'.format(', '.join(self._get_markdown_link(self._class_superclasses)))

        # Children
        if len(self._class_subclasses) != 0:
            txt += '####  Children: {}\n'.format(', '.join(self._get_markdown_link(self._class_subclasses)))

        # Parent types
        if len(self._class_parent_types) != 0:
            txt += '####  Parent types: {}\n'.format(', '.join(sorted(self._get_markdown_link(self._class_parent_types.keys()))))

        # Metadata
        if self._class_has_metadata:
            txt += '```\n'
            txt += '  metadata:\n'
            txt += '    annotations:          {}\n'.format(Map(String, String).name())
            txt += '    labels:               {}\n'.format(Map(String, String).name())
            txt += '```\n'

        # Properties table
        txt += '####  Properties:\n\n'
        txt += 'Name | Type | Identifier | Abstract | Mapping\n'
        txt += '---- | ---- | ---------- | -------- | -------\n'
        if self._class_identifier is not None:
            txt += '{} | {} | True | False | - \n'.format(self._class_identifier, self._class_types[self._class_identifier].name())
            
        for p in sorted(self._class_types.keys()):
            if p == self._class_identifier:
                continue

            is_abstract = True if 'xf_{}'.format(p) in self._class_xf_hasattr else False
            is_mapped = ', '.join(self._get_markdown_link(self._class_mapping[p])) if p in self._class_mapping else '-'

            print(self._class_types[p])

            txt += '{} | {} | False | {} | {} \n'.format(p, self._class_types[p].name(), is_abstract, is_mapped)

        return txt
        