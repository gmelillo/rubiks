# (c) Copyright 2018-2019 OLX

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from kube_obj import KubeObj, KubeSubObj
from kube_types import Nullable, Map, String, List
from .istio_loadbalancer import IstioLoadBalancer


class IstioTrafficPolicy(KubeSubObj):
    _defaults = {
        'loadBalancer': None
    }

    _types = {
        'loadBalancer': Nullable(IstioLoadBalancer)
    }

    def render(self):
        return self.renderer()


class IstioSubset(KubeSubObj):
    _defaults = {
        'name': None,
        'labels': {},
        'trafficPolicy': None,
    }

    _types = {
        'name': Nullable(String),
        'trafficPolicy': Nullable(IstioTrafficPolicy),
        'labels': Nullable(Map(String, String)),
    }

    def render(self):
        return self.renderer(order=('name', 'trafficPolicy', 'labels'))


class IstioSpecs(KubeSubObj):
    _defaults = {
        'host': '',
        'trafficPolicy': None,
        'subsets': [],
        }

    _types = {
        'host': String,
        'trafficPolicy': Nullable(IstioTrafficPolicy),
        'subsets': Nullable(List(IstioSubset)),
        }

    def render(self):
        return self.renderer(order=('host', 'trafficPolicy', 'subsets'))


class IstioDestinationRule(KubeObj):
    apiVersion = 'networking.istio.io/v1alpha3'
    kind = 'DestinationRule'
    kubectltype = 'istio-destinationrule'
    _output_order = 250
    _uses_namespace = True

    _defaults = {
        'spec': IstioSpecs()
    }

    _types = {
        'spec': Nullable(IstioSpecs)
    }

    _parse_default_base = ('spec',)

    def render(self):
        ret = self.renderer(order=('spec',))
        del ret['name']
        return {'metadata': {'name': self._data['name']}, 'spec': ret['spec']}
