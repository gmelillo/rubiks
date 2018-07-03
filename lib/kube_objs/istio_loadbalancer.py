# (c) Copyright 2018-2011 OLX

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from kube_obj import KubeSubObj
from kube_types import Enum, Nullable, Map, String, Integer


# minimumRingSize: https://github.com/istio/api/blob/master/networking/v1alpha3/destination_rule.pb.go#L639
class IstioLoadBalancer(KubeSubObj):
    _defaults = {
        'simple': 'LEAST_CONN',
        'consistentHash': None,
        'minimumRingSize': None
    }

    _types = {
        'simple': Enum('LEAST_CONN', 'ROUND_ROBIN', 'RANDOM', 'PASSTHROUGH'),
        'consistentHash': Nullable(Map(String, String)),
        'minimumRingSize': Nullable(Integer)
    }

    def render(self):
        return self.renderer(order=('simple', 'minimumRingSize', 'consistentHash',))
