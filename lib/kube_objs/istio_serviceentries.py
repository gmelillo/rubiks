# (c) Copyright 2018-2019 OLX

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from kube_obj import KubeObj, KubeSubObj
from kube_types import Nullable, String, List, Integer, Domain


class IstioPort(KubeSubObj):
    _defaults = {
        'number': None,
        'protocol': None,
        'name': None
    }

    _types = {
        'number': Integer,
        'protocol': String,
        'name': Nullable(String)
    }

    def render(self):
        return self.renderer()


class IstioServiceEntriesSpec(KubeSubObj):
    _defaults = {
        'hosts': None,
        'ports': None,
        'subsets': [],
    }

    _types = {
        'hosts': Nullable(List(Domain)),
        'ports': Nullable(IstioPort),
    }

    def render(self):
        return self.renderer(order=('hosts', 'ports', 'subsets'))


class IstioServiceEntries(KubeObj):
    apiVersion = 'networking.istio.io/v1alpha3'
    kind = 'ServiceEntry'
    kubectltype = 'istio-serviceentry'
    _output_order = 230
    _uses_namespace = True

    _defaults = {
        'spec': IstioServiceEntriesSpec()
    }

    _types = {
        'spec': Nullable(IstioServiceEntriesSpec)
    }

    _parse_default_base = ('spec',)

    def render(self):
        ret = self.renderer(order=('spec',))
        del ret['name']
        return {'metadata': {'name': self._data['name']}, 'spec': ret['spec']}
