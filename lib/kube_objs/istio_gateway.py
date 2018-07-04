# (c) Copyright 2018-2011 OLX

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from collections import OrderedDict
from kube_obj import KubeObj, KubeSubObj
from kube_types import *

class IstioGatewaySelector(KubeSubObj):
    _defaults = {
        'app': None,
        }

    _types = {
        'app': Nullable(String),
        }
    
    def render(self):
        return self.renderer()

class IstioGateway(KubeObj):
    apiVersion = 'networking.istio.io/v1alpha3'
    kind = 'Gateway'
    kubectltype = 'istiorouterule'
    #selector = IstioGatewaySelector()

    _uses_namespace = False
    _output_order = 200
    
    _defaults = {
        'selector': IstioGatewaySelector(),
    }

    _types = {
        'selector': IstioGatewaySelector,
    }

    def render(self):
        ret = self.renderer(return_none=True)
        spec = OrderedDict()

        print (ret)
        print (spec)

        if 'selector' in ret:
            spec['selector'] = ret['selector']
#        if 'servers' in ret:
#            spec['servers'] = [ret['servers']]
#        if 'version' in ret:
#            spec['route'] = [{'labels': {'version': ret['version']}}]

        return {'metadata': {'name': ret['name']},
                'spec': spec,
                }