# (c) Copyright 2018-2019 OLX

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from collections import OrderedDict
from kube_obj import KubeObj, KubeSubObj
from kube_types import *
from .istio_http import IstioServer


class IstioGatewaySpec(KubeSubObj):
    _defaults = {
        'selector': {},
        'servers': IstioServer(),
    }

    _types = {
        'selector': Nullable(Map(String, String)),
        'servers': List(IstioServer),
    }

    def render(self):
        return self.renderer()


class IstioGateway(KubeObj):
    apiVersion = 'networking.istio.io/v1alpha3'
    kind = 'Gateway'
    kubectltype = 'istiogateway'

    _uses_namespace = False
    _output_order = 200

    _defaults = {
        'name': None,
        'spec': IstioGatewaySpec(),
    }

    _types = {
        'name': String,
        'spec': IstioGatewaySpec,
    }

    def render(self):
        ret = self.renderer(return_none=True)
        spec = OrderedDict()
        if 'selector' in ret:
            spec['selector'] = ret['selector']

        return {'metadata': {'name': ret['name']},
                'spec': ret['spec'],
                }
