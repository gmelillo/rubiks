# (c) Copyright 2018-2019 OLX

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from kube_obj import KubeObj, KubeSubObj
from kube_types import Nullable, String, List, Integer, Domain, Map, Enum


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


class IstioServiceEntryEndpoint(KubeSubObj):
    _defaults = {
        'address': None,
        'ports': None,
        'labels': None
    }

    _types = {
        'address': String,
        'ports': Nullable(Map(String, Integer)),
        'labels': Nullable(Map(String, String))
    }


class IstioServiceEntriesSpec(KubeSubObj):
    _defaults = {
        'hosts': None,
        'ports': None,
        'addresses': [],
        'location': None,
        'resolution': None,
        'endpoints': None
    }

    _types = {
        'hosts': Nullable(List(Domain)),
        'ports': Nullable(IstioPort),
        'addresses': Nullable(List(String)),
        'location': Nullable(Enum('MESH_EXTERNAL', 'MESH_INTERNAL')),
        'resolution': Nullable(Enum('NONE', 'STATIC', 'DNS')),
        'endpoints': Nullable(List(IstioServiceEntryEndpoint))
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
