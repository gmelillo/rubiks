# (c) Copyright 2017-2018 OLX

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from kube_obj import KubeObj, KubeSubObj, order_dict
from kube_types import *
from .pod import *
from .selectors import *


class DplBaseUpdateStrategy(KubeSubObj):
    _exclude = {
        '.type': True,
        }

    def find_subparser(self, doc):
        if 'type' in doc and doc['type'] == 'Recreate':
            return DplRecreateStrategy
        if 'type' in doc and doc['type'] == 'RollingUpdate':
            return DplRollingUpdateStrategy


class DplRecreateStrategy(DplBaseUpdateStrategy):
    def render(self):
        return {'type': 'Recreate'}


class DplRollingUpdateStrategy(DplBaseUpdateStrategy):
    _defaults = {
        'maxSurge': None,
        'maxUnavailable': None,
        }

    _types = {
        'maxSurge': SurgeSpec,
        'maxUnavailable': SurgeSpec,
        }

    _parse_default_base = ('rollingUpdate',)

    def do_validate(self):
        return SurgeCheck.validate(self._data['maxSurge'], self._data['maxUnavailable'])

    def render(self):
        ret = self.renderer()
        if len(ret) == 0:
            return {'type': 'RollingUpdate'}
        return {'rollingUpdate': ret, 'type': 'RollingUpdate'}


class ReplicationController(KubeObj):
    apiVersion = 'v1'
    kind = 'ReplicationController'
    kubectltype = 'replicationcontroller'

    _defaults = {
        'minReadySeconds': None,
        'pod_template': PodTemplateSpec(),
        'replicas': 1,
        'selector': None,
        }

    _types = {
        'minReadySeconds': Nullable(Positive(NonZero(Integer))),
        'pod_template': PodTemplateSpec,
        'replicas': Positive(NonZero(Integer)),
        'selector': Nullable(Map(String, String)),
        }

    _parse_default_base = ('spec',)

    _parse = {
        'pod_template': ('spec', 'template'),
        }

    _exclude = {
        '.status': True,
        }

    def render(self):
        ret = self.renderer(mapping={'pod_template': 'template'}, order=('replicas', 'selector', 'template'))
        del ret['name']
        return {'metadata': {'name': self._data['name']}, 'spec': ret}


class Deployment(KubeObj):
    """
    A Deployment controller provides declarative updates for Pods and ReplicaSets.

    You describe a desired state in a Deployment object, and the Deployment controller changes the actual state to the desired state at a controlled rate.
    You can define Deployments to create new ReplicaSets, or to remove existing Deployments and adopt all their resources with new Deployments.
    """

    apiVersion = 'extensions/v1beta1'
    kind = 'Deployment'
    kubectltype = 'deployment'
    _document_url = 'https://kubernetes.io/docs/concepts/workloads/controllers/deployment/'

    _defaults = {
        'minReadySeconds': None,
        'paused': None,
        'pod_template': PodTemplateSpec(),
        'progressDeadlineSeconds': None,
        'replicas': 1,
        'revisionHistoryLimit': None,
        'selector': None,
        'strategy': None,
        }

    _types = {
        'minReadySeconds': Nullable(Positive(NonZero(Integer))),
        'paused': Nullable(Boolean),
        'pod_template': PodTemplateSpec,
        'progressDeadlineSeconds': Nullable(Positive(NonZero(Integer))),
        'replicas': Positive(NonZero(Integer)),
        'revisionHistoryLimit': Nullable(Positive(NonZero(Integer))),
        'selector': Nullable(BaseSelector),
        'strategy': Nullable(DplBaseUpdateStrategy),
        }

    _parse_default_base = ('spec',)

    _parse = {
        'pod_template': ('spec', 'template'),
        }

    _exclude = {
        '.status': True,
        }

    def render(self):
        ret = self.renderer(mapping={'pod_template': 'template'}, order=('replicas', 'template'))
        if isinstance(self._data['selector'], MatchLabelsSelector):
            self.labels.update(self._data['selector']._data['matchLabels'])
        del ret['name']
        return {'metadata': {'name': self._data['name']}, 'spec': ret}
