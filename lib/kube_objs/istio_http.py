# (c) Copyright 2018-2019 OLX

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from kube_obj import KubeObj, KubeSubObj
from kube_types import Nullable, String, List, Domain, Positive, Integer, Map, Boolean


class IstioHTTPFaultInjectionAbort(KubeSubObj):
    _defaults = {
        'percent': None,
        'httpStatus': None
    }

    _types = {
        'percent': Nullable(Integer),
        'httpStatus': Integer
    }

    def render(self):
        return self.renderer()


class IstioHTTPFaultInjectionDelay(KubeSubObj):
    _defaults = {
        'percent': None,
        'fixedDelay': '5s'
    }

    _types = {
        'percent': Nullable(Positive(Integer)),
        'fixedDelay': String
    }

    def render(self):
        return self.renderer()


class IstioHTTPFaultInjection(KubeSubObj):
    _defaults = {
        'delay': None,
        'abort': None
    }

    _types = {
        'delay': Nullable(IstioHTTPFaultInjectionDelay),
        'abort': Nullable(IstioHTTPFaultInjectionAbort)
    }

    def render(self):
        if self._data['delay'] is None or self._data['abort'] is None:
            raise(Exception('A fault rule MUST HAVE delay or abort or both.'))
        return self.renderer()


class IstioStringMatch(KubeSubObj):
    _defaults = {
        'exact': None,
        'prefix': None,
        'regex': None
    }

    _types = {
        'exact': Nullable(String),
        'prefix': Nullable(String),
        'regex': Nullable(String)
    }

    def render(self):
        # TODO: Ensure at least one of the 3 is not null before rendering
        return self.renderer()


class IstioHTTPMatchRequest(KubeSubObj):
    _defaults = {
        'uri': None,
        'scheme': None,
        'method': None,
        'authority': None,
        'headers': None,
        'port': None,
        'sourceLabels': None,
        'gateways': None
    }

    _types = {
        'uri': Nullable(IstioStringMatch),
        'scheme': Nullable(IstioStringMatch),
        'method': Nullable(IstioStringMatch),
        'authority': Nullable(IstioStringMatch),
        'headers': Nullable(Map(String, String)),
        'port': Nullable(Integer),
        'sourceLabels': Nullable(Map(String, String)),
        'gateways': Nullable(List(String))
    }

    def render(self):
        return self.renderer()


class IstioHTTPRetry(KubeSubObj):
    _defaults = {
        'attempts': None,
        'perTryTimeout': None
    }

    _types = {
        'attempts': Nullable(Integer),
        'perTryTimeout': Nullable(String)
    }

    def render(self):
        return self.renderer()


class IstioHTTPRedirect(KubeSubObj):
    _defaults = {
        'uri': None,
        'authority': None
    }

    _types = {
        'uri': Nullable(String),
        'authority': Nullable(String)
    }

    def render(self):
        return self.renderer()


class IstioHTTPRewrite(KubeSubObj):
    _defaults = {
        'uri': None,
        'authority': None
    }

    _types = {
        'uri': Nullable(String),
        'authority': Nullable(String)
    }

    def render(self):
        return self.renderer()


class IstioPortSelector(KubeSubObj):
    _defaults = {
        'number': None
    }

    _types = {
        'number': Nullable(Integer)
    }

    def render(self):
        return self.renderer()


class IstioDestination(KubeSubObj):
    _defaults = {
        'host': None,
        'subset': None,
        'port': None
    }

    _types = {
        'host': Nullable(String),
        'subset': Nullable(String),
        'port': Nullable(IstioPortSelector)
    }

    def render(self):
        return self.renderer()


class IstioDestinationWeight(KubeSubObj):
    _defaults = {
        'destination': None,
        'weight': None
    }

    _types = {
        'destination': Nullable(IstioDestination),
        'weight': Nullable(Integer)
    }

    def render(self):
        return self.renderer()


class IstioCorsPolicy(KubeSubObj):
    _defaults = {
        'allowOrigin': None,
        'allowMethods': None,
        'allowHeaders': None,
        'exposeHeaders': None,
        'maxAge': None,
        'allowCredentials': None
    }

    _types = {
        'allowOrigin': Nullable(List(String)),
        'allowMethods': Nullable(List(String)),
        'allowHeaders': Nullable(List(String)),
        'exposeHeaders': Nullable(List(String)),
        'maxAge': Nullable(String),
        'allowCredentials': Nullable(Boolean)
    }

    def render(self):
        return self.renderer()


class IstioHTTPRoute(KubeSubObj):
    _defaults = {
        'match': None,
        'route': None,
        'redirect': None,
        'rewrite': None,
        'websocketUpgrade': None,
        'timeout': None,
        'retries': None,
        'fault': None,
        'mirror': None,
        'corsPolicy': None,
        'appendHeaders': None
    }

    _types = {
        'match': Nullable(List(IstioHTTPMatchRequest)),
        'route': Nullable(List(IstioDestinationWeight)),
        'redirect': Nullable(IstioHTTPRedirect),
        'rewrite': Nullable(IstioHTTPRewrite),
        'websocketUpgrade': Nullable(Boolean),
        'timeout': Nullable(String),
        'retries': Nullable(IstioHTTPRetry),
        'fault': Nullable(IstioHTTPFaultInjection),
        'mirror': Nullable(IstioDestination),
        'corsPolicy': Nullable(IstioCorsPolicy),
        'appendHeaders': Nullable(Map(String, String))
    }

    def render(self):
        return self.renderer()
