# (c) Copyright 2018-2011 OLX

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from kube_obj import KubeSubObj
from kube_types import Nullable, Integer


class IstioConnectionPool(KubeSubObj):
    _defaults = {
        'maxConnections': None,
    }

    _types = {
        'maxConnections': Nullable(Integer),
    }

    def render(self):
        return None if self._data['maxConnections'] is None else {
                'tcp': {'maxConnections': self._data['maxConnections']}
            }
