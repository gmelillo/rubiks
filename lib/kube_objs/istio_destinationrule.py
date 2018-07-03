# (c) Copyright 2018-2019 OLX

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from kube_obj import KubeObj, KubeSubObj
from kube_types import Nullable, Map, String, List, Integer, Enum
from .istio_loadbalancer import IstioLoadBalancer
from .istio_connectionpool import IstioConnectionPool
from .istio_http import IstioPortSelector


class OutlierDetectionHTTPSettings(KubeSubObj):
    _defaults = {
        'consecutiveErrors': None,
        'interval': None,
        'baseEjectionTime': None,
        'maxEjectionPercent': None,
    }

    _types = {
        'consecutiveErrors': Nullable(Integer),
        'interval': Nullable(String),
        'baseEjectionTime': Nullable(String),
        'maxEjectionPercent': Nullable(Integer),
    }

    def render(self):
        return self.renderer()


class IstioOutlierDetection(KubeSubObj):
    _defaults = {
        'http': None
    }

    _types = {
        'http': Nullable(OutlierDetectionHTTPSettings)
    }

    def render(self):
        return self.renderer()


class IstioTLSSettings(KubeSubObj):
    _defaults = {
        'mode': None,
        'clientCertificate': None,
        'privateKey': None,
        'caCertificates': None,
        'subjectAltNames': None,
        'sni': None
    }

    _types = {
        'mode': Nullable(Enum('DISABLE', 'SIMPLE', 'MUTUAL', 'ISTIO_MUTUAL')),
        'clientCertificate': Nullable(String),
        'privateKey': Nullable(String),
        'caCertificates': Nullable(String),
        'subjectAltNames': Nullable(List(String)),
        'sni': Nullable(String)
    }

    def render(self):
        return self.renderer()


class IstioConnectionPoolSettingsTCPSettings(KubeSubObj):
    _defaults = {
        'maxConnections': None,
        'connectTimeout': None
    }

    _types = {
        'maxConnections': Nullable(String),
        'connectTimeout': Nullable(String)
    }

    def render(self):
        return self.renderer()


class IstioConnectionPoolSettingsHTTPSettings(KubeSubObj):
    _defaults = {
        'http1MaxPendingRequests': None,
        'http2MaxRequests': None,
        'maxRequestsPerConnection': None,
        'maxRetries': None
    }

    _types = {
        'http1MaxPendingRequests': Nullable(Integer),
        'http2MaxRequests': Nullable(Integer),
        'maxRequestsPerConnection': Nullable(Integer),
        'maxRetries': Nullable(Integer)
    }

    def render(self):
        return self.renderer()


class IstioConnectionPoolSettings(KubeSubObj):
    _defaults = {
        'tcp': None,
        'http': None
    }

    _types = {
        'tcp': Nullable(IstioConnectionPoolSettingsTCPSettings),
        'http': Nullable(IstioConnectionPoolSettingsHTTPSettings)
    }

    def render(self):
        return self.renderer()


class IstioPortTrafficPolicy(KubeSubObj):
    _defaults = {
        'port': None,
        'loadBalancer': None,
        'connectionPool': None,
        'outlierDetection': None,
        'tls': None
    }

    _types = {
        'port': Nullable(IstioPortSelector),
        'loadBalancer': Nullable(IstioLoadBalancer),
        'connectionPool': Nullable(IstioConnectionPoolSettings),
        'outlierDetection': Nullable(IstioOutlierDetection),
        'tls': Nullable(IstioTLSSettings)
    }

    def render(self):
        return self.renderer()


class IstioTrafficPolicy(KubeSubObj):
    _defaults = {
        'loadBalancer': None,
        'connectionPool': None,
        'outlierDetection': None,
        'tls': None,
        'portLevelSettings': None
    }

    _types = {
        'loadBalancer': Nullable(IstioLoadBalancer),
        'connectionPool': Nullable(IstioConnectionPool),
        'outlierDetection': Nullable(IstioOutlierDetection),
        'tls': Nullable(IstioTLSSettings),
        'portLevelSettings': Nullable(IstioPortTrafficPolicy)
    }

    def render(self):
        return self.renderer()


class IstioSubset(KubeSubObj):
    _defaults = {
        'name': None,
        'labels': None,
        'trafficPolicy': None,
    }

    _types = {
        'name': Nullable(String),
        'trafficPolicy': Nullable(IstioTrafficPolicy),
        'labels': Nullable(Map(String, String)),
    }

    def render(self):
        return self.renderer(order=('name', 'trafficPolicy', 'labels'))


class IstioDestinationRuleSpecs(KubeSubObj):
    _defaults = {
        'host': None,
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
        'spec': IstioDestinationRuleSpecs()
    }

    _types = {
        'spec': Nullable(IstioDestinationRuleSpecs)
    }

    _parse_default_base = ('spec',)

    def render(self):
        ret = self.renderer(order=('spec',))
        del ret['name']
        return {'metadata': {'name': self._data['name']}, 'spec': ret['spec']}
