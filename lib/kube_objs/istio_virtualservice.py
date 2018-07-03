# (c) Copyright 2018-2019 OLX

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from kube_obj import KubeObj, KubeSubObj
from kube_types import Nullable, String, List, Domain
from .istio_http import IstioHTTPRoute


class IstioVirtualServiceSpec(KubeSubObj):
    _defaults = {
        'hosts': None,
        'gateways': None,
        'http': None,
    }

    _types = {
        'hosts': Nullable(List(Domain)),
        'gateways': Nullable(List(String)),
        'http': Nullable(List(IstioHTTPRoute)),
    }

    def render(self):
        return self.renderer(order=('hosts', 'gateways', 'http'))


class IstioVirtualService(KubeObj):
    apiVersion = 'networking.istio.io/v1alpha3'
    kind = 'VirtualService'
    kubectltype = 'istio-virtualservice'
    _output_order = 240
    _uses_namespace = True

    _defaults = {
        'spec': IstioVirtualServiceSpec()
    }

    _types = {
        'spec': Nullable(IstioVirtualServiceSpec)
    }

    _parse_default_base = ('spec',)

    def render(self):
        ret = self.renderer(order=('spec',))
        del ret['name']
        return {'metadata': {'name': self._data['name']}, 'spec': ret['spec']}
