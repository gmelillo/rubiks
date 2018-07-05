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

    def populate_args(self, parser):
        pass

    def run(self, args):
        objs = load_python.PythonBaseFile.get_kube_objs()
        r = self.get_repository()
        md = ''

        for oname in objs.keys():
            md += objs[oname].get_help().render_markdown()

        with open(os.path.join(r.basepath, 'docs/rubiks.class.md'), 'w') as f:
            f.write(md)