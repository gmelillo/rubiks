# (c) Copyright 2018-2019 OLX

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from command import Command
from .bases import CommandRepositoryBase
import load_python
import os

class Command_docgen(Command, CommandRepositoryBase):
    """Generate a markdown file with basic description for all object inside rubiks"""

    _description = """
    This document is automatically generated using the command `docgen` and describe all the object and types that can be used inside Rubiks to configure your cluster
    """

    def populate_args(self, parser):
        pass

    def run(self, args):
        objs = load_python.PythonBaseFile.get_kube_objs()
        types = load_python.PythonBaseFile.get_kube_types()
        formats = load_python.PythonBaseFile.get_kube_vartypes()
        
        r = self.get_repository()

        doc = '\n'.join([line.strip() for line in self._description.split('\n')])

        md = ''
        header = '<p align="center"><img src="logos/rubiks-logo-horizontal.png" title="Rubiks Logo"></p>\n\n'
        header += '# Rubiks Object Index\n{}\n\n'.format(doc)
        header += '# Table of contents\n\n'

        header += '- [Formats](#formats)\n'
        md += '\n# Formats\n\n'
        for fname in sorted(formats.keys()):
            header += '  - [{}](#{})\n'.format(fname, fname.lower())
            md += '## {}\n\n'.format(fname)
            md += '{}\n\n'.format(formats[fname].get_description())

        header += '- [Types](#types)\n'
        md += '\n# Types\n\n'
        for tname in sorted(types.keys()):
            header += '  - [{}](#{})\n'.format(tname, tname.lower())
            md += '## {}\n\n'.format(tname)
            md += '{}\n\n'.format(types[tname].get_description())


        header += '- [Objects](#objects)\n'
        md += '\n# Objects\n\n'
        for oname in sorted(objs.keys()):
            header += '  - [{}](#{})\n'.format(oname, oname.lower())
            md += objs[oname].get_help().render_markdown()

        with open(os.path.join(r.basepath, 'docs/rubiks.class.md'), 'w') as f:
            f.write(header.encode('utf-8'))
            f.write(md.encode('utf-8'))