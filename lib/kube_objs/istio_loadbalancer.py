# (c) Copyright 2018-2011 OLX

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from kube_obj import KubeSubObj
from kube_types import Enum, Nullable, Map, String, Integer


class LoadBalancerSettingsConsistentHashLB(KubeSubObj):
    _defaults = {
        'httpHeader': None,
        'httpHeader': None
    }

    _types = {
        'httpHeader': Nullable(String),
        'minimumRingSize': Nullable(Integer)
    }

    def render(self):
        return self.renderer()


class IstioLoadBalancer(KubeSubObj):
    _defaults = {
        'simple': 'LEAST_CONN',
        'consistentHash': None,
    }

    _types = {
        'simple': Enum('LEAST_CONN', 'ROUND_ROBIN', 'RANDOM', 'PASSTHROUGH'),
        'consistentHash': Nullable(Map(String, String)),
    }

    def render(self):
        return self.renderer(order=('simple', 'consistentHash',))
