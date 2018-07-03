# (c) Copyright 2018-2011 OLX

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from kube_obj import KubeSubObj
from kube_types import Nullable, Integer, String


class IstioConnectionPool(KubeSubObj):
    _defaults = {
        'maxConnections': None,
        'connectTimeout': None,
    }

    _types = {
        'maxConnections': Nullable(Integer),
        'connectTimeout': Nullable(String)
    }

    def render(self):
        filtered = {k: v for k, v in self._data.iteritems() if v is not None}
        self._data = {
            'tcp': filtered
        }
        return self.renderer()
