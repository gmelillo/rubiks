# (c) Copyright 2017-2018 OLX

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from collections import OrderedDict
from kube_obj import KubeObj
from kube_types import *


class IstioRouteRule(KubeObj):
    apiVersion = 'config.istio.io/v1alpha2'
    kind = 'RouteRule'
    kubectltype = 'istiorouterule'

    _uses_namespace = False
    _output_order = 200

    _defaults = {
         'destination': {},
         'precedence': 1,
         'version': 'v1',
        }

    _types = {
        'destination': Map(String, String),
        'precedence': Integer,
        'version': String,
        }

    def render(self):
        ret = self.renderer(return_none=True)
        spec = OrderedDict()
        if 'destination' in ret:
            spec['destination'] = ret['destination']
        if 'precedence' in ret:
            spec['precedence'] = ret['precedence']
        if 'version' in ret:
            spec['route'] = [{'labels': {'version': ret['version']}}]

        return {'metadata': {'name': ret['name']},
                'spec': spec,
                }
