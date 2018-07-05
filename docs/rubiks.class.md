## TLSCredentials
#### Parents: [Secret](#secret)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
Map<String, String> | [secrets](#secrets) | False | False
String | [tls_cert](#tls_cert) | False | False
String | [tls_key](#tls_key) | False | False
NonEmpty<String> | [type](#type) | False | False
## Service
####  Children: [ClusterIPService](#clusteripservice), [AWSLoadBalancerService](#awsloadbalancerservice)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
NonEmpty<List<ServicePort>> | [ports](#ports) | False | True
NonEmpty<Map<String, String>> | [selector](#selector) | False | True
Nullable<Enum(u'ClientIP', u'None')> | [sessionAffinity](#sessionaffinity) | False | False
## DockerCredentials
#### Parents: [Secret](#secret)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
Map<String, Map<String, String>> | [dockers](#dockers) | False | False
Map<String, String> | [secrets](#secrets) | False | False
NonEmpty<String> | [type](#type) | False | False
## DplBaseUpdateStrategy
####  Children: [DplRecreateStrategy](#dplrecreatestrategy), [DplRollingUpdateStrategy](#dplrollingupdatestrategy)
####  Parent types: [Deployment](#deployment)
####  Properties:

Name | Type | Identifier | Abstract
## Role
#### Parents: [RoleBase](#rolebase)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
NonEmpty<List<PolicyRule>> | [rules](#rules) | False | False
## Group
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
NonEmpty<List<UserIdentifier>> | [users](#users) | False | False
## RouteTLS
####  Parent types: [Route](#route)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<NonEmpty<String>> | [caCertificate](#cacertificate) | False | False
Nullable<NonEmpty<String>> | [certificate](#certificate) | False | False
Nullable<NonEmpty<String>> | [destinationCACertificate](#destinationcacertificate) | False | False
Enum(u'Allow', u'Disable', u'Redirect') | [insecureEdgeTerminationPolicy](#insecureedgeterminationpolicy) | False | False
Nullable<NonEmpty<String>> | [key](#key) | False | False
Enum(u'edge', u'reencrypt', u'passthrough') | [termination](#termination) | False | False
## SCCRunAsUser
####  Parent types: [SecurityContextConstraints](#securitycontextconstraints)
####  Properties:

Name | Type | Identifier | Abstract
Enum(u'MustRunAs', u'RunAsAny', u'MustRunAsRange', u'MustRunAsNonRoot') | [type](#type) | False | False
Nullable<Positive<NonZero<Integer>>> | [uid](#uid) | False | False
Nullable<Positive<NonZero<Integer>>> | [uidRangeMax](#uidrangemax) | False | False
Nullable<Positive<NonZero<Integer>>> | [uidRangeMin](#uidrangemin) | False | False
## PersistentVolumeClaim
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
List<Enum(u'ReadWriteOnce', u'ReadOnlyMany', u'ReadWriteMany')> | [accessModes](#accessmodes) | False | False
Memory | [request](#request) | False | False
Nullable<BaseSelector> | [selector](#selector) | False | False
Nullable<Identifier> | [volumeName](#volumename) | False | True
## PodVolumePVCSpec
#### Parents: [PodVolumeBaseSpec](#podvolumebasespec)
####  Parent types: [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Abstract
Identifier | [claimName](#claimname) | False | False
Identifier | [name](#name) | False | False
## DCConfigChangeTrigger
#### Parents: [DCTrigger](#dctrigger)
####  Parent types: [DeploymentConfig](#deploymentconfig)
####  Properties:

Name | Type | Identifier | Abstract
## SecurityContext
####  Parent types: [ContainerSpec](#containerspec), [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<Integer> | [fsGroup](#fsgroup) | False | False
Nullable<Boolean> | [privileged](#privileged) | False | False
Nullable<Boolean> | [runAsNonRoot](#runasnonroot) | False | False
Nullable<Integer> | [runAsUser](#runasuser) | False | False
Nullable<List<Integer>> | [supplementalGroups](#supplementalgroups) | False | False
## Project
#### Parents: [Namespace](#namespace)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
## PersistentVolume
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
List<Enum(u'ReadWriteOnce', u'ReadOnlyMany', u'ReadWriteMany')> | [accessModes](#accessmodes) | False | False
Nullable<AWSElasticBlockStore> | [awsElasticBlockStore](#awselasticblockstore) | False | False
Memory | [capacity](#capacity) | False | False
Nullable<PersistentVolumeRef> | [claimRef](#claimref) | False | False
Nullable<Enum(u'Retain', u'Recycle', u'Delete')> | [persistentVolumeReclaimPolicy](#persistentvolumereclaimpolicy) | False | False
## DeploymentConfig
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
Nullable<Positive<NonZero<Integer>>> | [minReadySeconds](#minreadyseconds) | False | False
Nullable<Boolean> | [paused](#paused) | False | False
PodTemplateSpec | [pod_template](#pod_template) | False | False
Positive<NonZero<Integer>> | [replicas](#replicas) | False | False
Nullable<Positive<NonZero<Integer>>> | [revisionHistoryLimit](#revisionhistorylimit) | False | False
Nullable<Map<String, String>> | [selector](#selector) | False | False
DCBaseUpdateStrategy | [strategy](#strategy) | False | False
Boolean | [test](#test) | False | False
List<DCTrigger> | [triggers](#triggers) | False | False
## ContainerPort
####  Parent types: [ContainerSpec](#containerspec)
####  Properties:

Name | Type | Identifier | Abstract
Positive<NonZero<Integer>> | [containerPort](#containerport) | False | False
Nullable<IP> | [hostIP](#hostip) | False | False
Nullable<Positive<NonZero<Integer>>> | [hostPort](#hostport) | False | False
Nullable<String> | [name](#name) | False | False
Enum(u'TCP', u'UDP') | [protocol](#protocol) | False | False
## DCImageChangeTrigger
#### Parents: [DCTrigger](#dctrigger)
####  Parent types: [DeploymentConfig](#deploymentconfig)
####  Properties:

Name | Type | Identifier | Abstract
## RoleRef
####  Parent types: [ClusterRoleBinding](#clusterrolebinding), [PolicyBindingRoleBinding](#policybindingrolebinding), [RoleBindingBase](#rolebindingbase), [RoleBinding](#rolebinding)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<SystemIdentifier> | [name](#name) | False | False
Nullable<Identifier> | [ns](#ns) | False | False
## LifeCycleHTTP
#### Parents: [LifeCycleProbe](#lifecycleprobe)
####  Parent types: [LifeCycle](#lifecycle)
####  Properties:

Name | Type | Identifier | Abstract
NonEmpty<Path> | [path](#path) | False | False
Positive<NonZero<Integer>> | [port](#port) | False | False
Nullable<Enum(u'HTTP', u'HTTPS')> | [scheme](#scheme) | False | False
## PodVolumeItemMapper
#### Parents: [PodVolumeBaseSpec](#podvolumebasespec)
####  Children: [PodVolumeConfigMapSpec](#podvolumeconfigmapspec), [PodVolumeSecretSpec](#podvolumesecretspec)
####  Parent types: [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<Map<String, String>> | [item_map](#item_map) | False | False
Identifier | [name](#name) | False | False
## DaemonSet
#### Parents: [SelectorsPreProcessMixin](#selectorspreprocessmixin)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
PodTemplateSpec | [pod_template](#pod_template) | False | False
Nullable<BaseSelector> | [selector](#selector) | False | True
## DCBaseUpdateStrategy
####  Children: [DCRecreateStrategy](#dcrecreatestrategy), [DCRollingStrategy](#dcrollingstrategy), [DCCustomStrategy](#dccustomstrategy)
####  Parent types: [DeploymentConfig](#deploymentconfig)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<Positive<NonZero<Integer>>> | [activeDeadlineSeconds](#activedeadlineseconds) | False | False
Map<String, String> | [annotations](#annotations) | False | False
Map<String, String> | [labels](#labels) | False | False
Nullable<ContainerResourceSpec> | [resources](#resources) | False | False
## Namespace
####  Children: [Project](#project)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
## ContainerEnvSpec
#### Parents: [ContainerEnvBaseSpec](#containerenvbasespec)
####  Parent types: [ContainerSpec](#containerspec), [DCCustomParams](#dccustomparams), [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Abstract
EnvString | [name](#name) | False | False
String | [value](#value) | False | False
## PodVolumeConfigMapSpec
#### Parents: [PodVolumeItemMapper](#podvolumeitemmapper), [PodVolumeBaseSpec](#podvolumebasespec)
####  Parent types: [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<Positive<Integer>> | [defaultMode](#defaultmode) | False | False
Nullable<Map<String, String>> | [item_map](#item_map) | False | False
Identifier | [map_name](#map_name) | False | False
Identifier | [name](#name) | False | False
## MatchExpression
####  Parent types: [MatchExpressionsSelector](#matchexpressionsselector)
####  Properties:

Name | Type | Identifier | Abstract
NonEmpty<String> | [key](#key) | False | False
Enum(u'In', u'NotIn', u'Exists', u'DoesNotExist') | [operator](#operator) | False | False
Nullable<List<String>> | [values](#values) | False | False
## SCCSELinux
####  Parent types: [SecurityContextConstraints](#securitycontextconstraints)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<String> | [level](#level) | False | False
Nullable<String> | [role](#role) | False | False
Nullable<Enum(u'MustRunAs', u'RunAsAny')> | [strategy](#strategy) | False | False
Nullable<String> | [type](#type) | False | False
Nullable<String> | [user](#user) | False | False
## ClusterRoleBinding
#### Parents: [RoleBindingBase](#rolebindingbase), [RoleBindingXF](#rolebindingxf)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
RoleRef | [roleRef](#roleref) | False | True
NonEmpty<List<RoleSubject>> | [subjects](#subjects) | False | True
## AWSLoadBalancerService
#### Parents: [Service](#service)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
Nullable<Identifier> | [aws-load-balancer-backend-protocol](#aws-load-balancer-backend-protocol) | False | False
Nullable<ARN> | [aws-load-balancer-ssl-cert](#aws-load-balancer-ssl-cert) | False | False
Nullable<Enum(u'Cluster', u'Local')> | [externalTrafficPolicy](#externaltrafficpolicy) | False | False
NonEmpty<List<ServicePort>> | [ports](#ports) | False | True
NonEmpty<Map<String, String>> | [selector](#selector) | False | True
Nullable<Enum(u'ClientIP', u'None')> | [sessionAffinity](#sessionaffinity) | False | False
## Job
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
Nullable<Positive<Integer>> | [activeDeadlineSeconds](#activedeadlineseconds) | False | False
Nullable<Positive<NonZero<Integer>>> | [completions](#completions) | False | False
Nullable<Boolean> | [manualSelector](#manualselector) | False | False
Nullable<Positive<NonZero<Integer>>> | [parallelism](#parallelism) | False | False
PodTemplateSpec | [pod_template](#pod_template) | False | False
Nullable<BaseSelector> | [selector](#selector) | False | False
## RouteDestService
#### Parents: [RouteDest](#routedest)
####  Parent types: [Route](#route)
####  Properties:

Name | Type | Identifier | Abstract
Identifier | [name](#name) | False | False
Positive<NonZero<Integer>> | [weight](#weight) | False | False
## DCRecreateStrategy
#### Parents: [DCBaseUpdateStrategy](#dcbaseupdatestrategy)
####  Parent types: [DeploymentConfig](#deploymentconfig)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<Positive<NonZero<Integer>>> | [activeDeadlineSeconds](#activedeadlineseconds) | False | False
Map<String, String> | [annotations](#annotations) | False | False
Nullable<DCCustomParams> | [customParams](#customparams) | False | False
Map<String, String> | [labels](#labels) | False | False
Nullable<DCRecreateParams> | [recreateParams](#recreateparams) | False | False
Nullable<ContainerResourceSpec> | [resources](#resources) | False | False
## DplRollingUpdateStrategy
#### Parents: [DplBaseUpdateStrategy](#dplbaseupdatestrategy)
####  Parent types: [Deployment](#deployment)
####  Properties:

Name | Type | Identifier | Abstract
SurgeSpec | [maxSurge](#maxsurge) | False | False
SurgeSpec | [maxUnavailable](#maxunavailable) | False | False
## ContainerSpec
#### Parents: [EnvironmentPreProcessMixin](#environmentpreprocessmixin)
####  Parent types: [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
Nullable<List<String>> | [args](#args) | False | False
Nullable<List<String>> | [command](#command) | False | False
Nullable<List<ContainerEnvBaseSpec>> | [env](#env) | False | True
NonEmpty<String> | [image](#image) | False | False
Nullable<Enum(u'Always', u'IfNotPresent')> | [imagePullPolicy](#imagepullpolicy) | False | False
Nullable<Enum(u'DockerImage')> | [kind](#kind) | False | False
Nullable<LifeCycle> | [lifecycle](#lifecycle) | False | False
Nullable<ContainerProbeBaseSpec> | [livenessProbe](#livenessprobe) | False | False
Nullable<List<ContainerPort>> | [ports](#ports) | False | True
Nullable<ContainerProbeBaseSpec> | [readinessProbe](#readinessprobe) | False | False
Nullable<ContainerResourceSpec> | [resources](#resources) | False | False
Nullable<SecurityContext> | [securityContext](#securitycontext) | False | False
Nullable<NonEmpty<Path>> | [terminationMessagePath](#terminationmessagepath) | False | False
Nullable<List<ContainerVolumeMountSpec>> | [volumeMounts](#volumemounts) | False | True
## DplRecreateStrategy
#### Parents: [DplBaseUpdateStrategy](#dplbaseupdatestrategy)
####  Parent types: [Deployment](#deployment)
####  Properties:

Name | Type | Identifier | Abstract
## DCTrigger
####  Children: [DCConfigChangeTrigger](#dcconfigchangetrigger), [DCImageChangeTrigger](#dcimagechangetrigger)
####  Parent types: [DeploymentConfig](#deploymentconfig)
####  Properties:

Name | Type | Identifier | Abstract
## ContainerEnvSecretSpec
#### Parents: [ContainerEnvBaseSpec](#containerenvbasespec)
####  Parent types: [ContainerSpec](#containerspec), [DCCustomParams](#dccustomparams), [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Abstract
NonEmpty<String> | [key](#key) | False | False
EnvString | [name](#name) | False | False
Identifier | [secret_name](#secret_name) | False | False
## MatchExpressionsSelector
#### Parents: [BaseSelector](#baseselector)
####  Parent types: [DaemonSet](#daemonset), [Deployment](#deployment), [Job](#job), [PersistentVolumeClaim](#persistentvolumeclaim)
####  Properties:

Name | Type | Identifier | Abstract
NonEmpty<List<MatchExpression>> | [matchExpressions](#matchexpressions) | False | False
## ContainerProbeBaseSpec
####  Children: [ContainerProbeTCPPortSpec](#containerprobetcpportspec), [ContainerProbeHTTPSpec](#containerprobehttpspec)
####  Parent types: [ContainerSpec](#containerspec)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<Positive<NonZero<Integer>>> | [failureThreshold](#failurethreshold) | False | False
Nullable<Positive<Integer>> | [initialDelaySeconds](#initialdelayseconds) | False | False
Nullable<Positive<NonZero<Integer>>> | [periodSeconds](#periodseconds) | False | False
Nullable<Positive<NonZero<Integer>>> | [successThreshold](#successthreshold) | False | False
Nullable<Positive<NonZero<Integer>>> | [timeoutSeconds](#timeoutseconds) | False | False
## PodVolumeEmptyDirSpec
#### Parents: [PodVolumeBaseSpec](#podvolumebasespec)
####  Parent types: [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Abstract
Identifier | [name](#name) | False | False
## PolicyBinding
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | ColonIdentifier | True | False
List<PolicyBindingRoleBinding> | [roleBindings](#rolebindings) | False | True
## ConfigMap
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
Map<String, String> | [files](#files) | False | False
## SCCGroups
####  Parent types: [SecurityContextConstraints](#securitycontextconstraints)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<List<SCCGroupRange>> | [ranges](#ranges) | False | False
Nullable<Enum(u'MustRunAs', u'RunAsAny')> | [type](#type) | False | False
## DCCustomStrategy
#### Parents: [DCBaseUpdateStrategy](#dcbaseupdatestrategy)
####  Parent types: [DeploymentConfig](#deploymentconfig)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<Positive<NonZero<Integer>>> | [activeDeadlineSeconds](#activedeadlineseconds) | False | False
Map<String, String> | [annotations](#annotations) | False | False
DCCustomParams | [customParams](#customparams) | False | False
Map<String, String> | [labels](#labels) | False | False
Nullable<ContainerResourceSpec> | [resources](#resources) | False | False
## ContainerResourceEachSpec
####  Parent types: [ContainerResourceSpec](#containerresourcespec)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<Positive<NonZero<Number>>> | [cpu](#cpu) | False | True
Nullable<Memory> | [memory](#memory) | False | False
## StorageClass
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
Map<String, String> | [parameters](#parameters) | False | False
String | [provisioner](#provisioner) | False | False
## DCRollingParams
####  Parent types: [DCRollingStrategy](#dcrollingstrategy)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<Positive<NonZero<Integer>>> | [intervalSeconds](#intervalseconds) | False | False
SurgeSpec | [maxSurge](#maxsurge) | False | False
SurgeSpec | [maxUnavailable](#maxunavailable) | False | False
Nullable<DCLifecycleHook> | [post](#post) | False | False
Nullable<DCLifecycleHook> | [pre](#pre) | False | False
Nullable<Positive<NonZero<Integer>>> | [timeoutSeconds](#timeoutseconds) | False | False
Nullable<Positive<NonZero<Integer>>> | [updatePeriodSeconds](#updateperiodseconds) | False | False
## SCCGroupRange
####  Parent types: [SCCGroups](#sccgroups)
####  Properties:

Name | Type | Identifier | Abstract
Positive<NonZero<Integer>> | [max](#max) | False | False
Positive<NonZero<Integer>> | [min](#min) | False | False
## DCCustomParams
#### Parents: [EnvironmentPreProcessMixin](#environmentpreprocessmixin)
####  Parent types: [DCCustomStrategy](#dccustomstrategy), [DCRecreateStrategy](#dcrecreatestrategy), [DCRollingStrategy](#dcrollingstrategy)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<List<String>> | [command](#command) | False | False
Nullable<List<ContainerEnvBaseSpec>> | [environment](#environment) | False | True
NonEmpty<String> | [image](#image) | False | False
## ContainerVolumeMountSpec
####  Parent types: [ContainerSpec](#containerspec), [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Abstract
Identifier | [name](#name) | False | False
NonEmpty<Path> | [path](#path) | False | False
Nullable<Boolean> | [readOnly](#readonly) | False | False
## LifeCycleProbe
####  Children: [LifeCycleExec](#lifecycleexec), [LifeCycleHTTP](#lifecyclehttp)
####  Parent types: [LifeCycle](#lifecycle)
####  Properties:

Name | Type | Identifier | Abstract
## SASecretSubject
####  Parent types: [ServiceAccount](#serviceaccount)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<CaseIdentifier> | [kind](#kind) | False | False
Nullable<Identifier> | [name](#name) | False | False
Nullable<Identifier> | [ns](#ns) | False | False
## PodTemplateSpec
####  Parent types: [DaemonSet](#daemonset), [DeploymentConfig](#deploymentconfig), [Deployment](#deployment), [Job](#job), [ReplicationController](#replicationcontroller)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
NonEmpty<List<ContainerSpec>> | [containers](#containers) | False | False
Nullable<Enum(u'ClusterFirst')> | [dnsPolicy](#dnspolicy) | False | False
Nullable<Boolean> | [hostIPC](#hostipc) | False | False
Nullable<Boolean> | [hostNetwork](#hostnetwork) | False | False
Nullable<Boolean> | [hostPID](#hostpid) | False | False
Nullable<List<PodImagePullSecret>> | [imagePullSecrets](#imagepullsecrets) | False | True
Nullable<Identifier> | [name](#name) | False | False
Nullable<Map<String, String>> | [nodeSelector](#nodeselector) | False | False
Nullable<Enum(u'Always', u'OnFailure', u'Never')> | [restartPolicy](#restartpolicy) | False | False
Nullable<SecurityContext> | [securityContext](#securitycontext) | False | False
Nullable<Identifier> | [serviceAccountName](#serviceaccountname) | False | True
Nullable<Positive<Integer>> | [terminationGracePeriodSeconds](#terminationgraceperiodseconds) | False | False
Nullable<List<PodVolumeBaseSpec>> | [volumes](#volumes) | False | False
## User
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | UserIdentifier | True | False
Nullable<String> | [fullName](#fullname) | False | False
NonEmpty<List<NonEmpty<String>>> | [identities](#identities) | False | False
## ContainerEnvConfigMapSpec
#### Parents: [ContainerEnvBaseSpec](#containerenvbasespec)
####  Parent types: [ContainerSpec](#containerspec), [DCCustomParams](#dccustomparams), [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Abstract
NonEmpty<String> | [key](#key) | False | False
Identifier | [map_name](#map_name) | False | False
EnvString | [name](#name) | False | False
## LifeCycleExec
#### Parents: [LifeCycleProbe](#lifecycleprobe)
####  Parent types: [LifeCycle](#lifecycle)
####  Properties:

Name | Type | Identifier | Abstract
NonEmpty<List<String>> | [command](#command) | False | False
## DCRollingStrategy
#### Parents: [DCBaseUpdateStrategy](#dcbaseupdatestrategy)
####  Parent types: [DeploymentConfig](#deploymentconfig)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<Positive<NonZero<Integer>>> | [activeDeadlineSeconds](#activedeadlineseconds) | False | False
Map<String, String> | [annotations](#annotations) | False | False
Nullable<DCCustomParams> | [customParams](#customparams) | False | False
Map<String, String> | [labels](#labels) | False | False
Nullable<ContainerResourceSpec> | [resources](#resources) | False | False
Nullable<DCRollingParams> | [rollingParams](#rollingparams) | False | False
## RouteDest
####  Children: [RouteDestService](#routedestservice)
####  Parent types: [Route](#route)
####  Properties:

Name | Type | Identifier | Abstract
Positive<NonZero<Integer>> | [weight](#weight) | False | False
## ContainerEnvPodFieldSpec
#### Parents: [ContainerEnvBaseSpec](#containerenvbasespec)
####  Parent types: [ContainerSpec](#containerspec), [DCCustomParams](#dccustomparams), [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<Enum(u'v1')> | [apiVersion](#apiversion) | False | False
Enum(u'metadata.name', u'metadata.namespace', u'metadata.labels', u'metadata.annotations', u'spec.nodeName', u'spec.serviceAccountName', u'status.podIP') | [fieldPath](#fieldpath) | False | False
EnvString | [name](#name) | False | False
## ServiceAccount
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
Nullable<List<SAImgPullSecretSubject>> | [imagePullSecrets](#imagepullsecrets) | False | True
Nullable<List<SASecretSubject>> | [secrets](#secrets) | False | True
## PodVolumeBaseSpec
####  Children: [PodVolumeHostSpec](#podvolumehostspec), [PodVolumeItemMapper](#podvolumeitemmapper), [PodVolumePVCSpec](#podvolumepvcspec), [PodVolumeEmptyDirSpec](#podvolumeemptydirspec), [PodVolumeConfigMapSpec](#podvolumeconfigmapspec), [PodVolumeSecretSpec](#podvolumesecretspec)
####  Parent types: [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Abstract
Identifier | [name](#name) | False | False
## ClusterRole
#### Parents: [RoleBase](#rolebase)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
NonEmpty<List<PolicyRule>> | [rules](#rules) | False | False
## DCLifecycleHook
####  Parent types: [DCRecreateParams](#dcrecreateparams), [DCRollingParams](#dcrollingparams)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<DCLifecycleNewPod> | [execNewPod](#execnewpod) | False | False
Enum(u'Abort', u'Retry', u'Ignore') | [failurePolicy](#failurepolicy) | False | False
Nullable<DCTagImages> | [tagImages](#tagimages) | False | False
## ClusterIPService
#### Parents: [Service](#service)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
Nullable<IPv4> | [clusterIP](#clusterip) | False | False
NonEmpty<List<ServicePort>> | [ports](#ports) | False | True
NonEmpty<Map<String, String>> | [selector](#selector) | False | True
Nullable<Enum(u'ClientIP', u'None')> | [sessionAffinity](#sessionaffinity) | False | False
## PersistentVolumeRef
####  Parent types: [PersistentVolume](#persistentvolume)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<String> | [apiVersion](#apiversion) | False | False
Nullable<CaseIdentifier> | [kind](#kind) | False | False
Nullable<Identifier> | [name](#name) | False | False
Nullable<Identifier> | [ns](#ns) | False | False
## DCLifecycleNewPod
#### Parents: [EnvironmentPreProcessMixin](#environmentpreprocessmixin)
####  Parent types: [DCLifecycleHook](#dclifecyclehook)
####  Properties:

Name | Type | Identifier | Abstract
NonEmpty<List<String>> | [command](#command) | False | False
Identifier | [containerName](#containername) | False | False
Nullable<List<ContainerEnvBaseSpec>> | [env](#env) | False | True
Nullable<List<ContainerVolumeMountSpec>> | [volumeMounts](#volumemounts) | False | False
Nullable<List<Identifier>> | [volumes](#volumes) | False | False
## ContainerProbeTCPPortSpec
#### Parents: [ContainerProbeBaseSpec](#containerprobebasespec)
####  Parent types: [ContainerSpec](#containerspec)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<Positive<NonZero<Integer>>> | [failureThreshold](#failurethreshold) | False | False
Nullable<Positive<Integer>> | [initialDelaySeconds](#initialdelayseconds) | False | False
Nullable<Positive<NonZero<Integer>>> | [periodSeconds](#periodseconds) | False | False
Positive<NonZero<Integer>> | [port](#port) | False | True
Nullable<Positive<NonZero<Integer>>> | [successThreshold](#successthreshold) | False | False
Nullable<Positive<NonZero<Integer>>> | [timeoutSeconds](#timeoutseconds) | False | False
## ContainerEnvBaseSpec
####  Children: [ContainerEnvSpec](#containerenvspec), [ContainerEnvConfigMapSpec](#containerenvconfigmapspec), [ContainerEnvSecretSpec](#containerenvsecretspec), [ContainerEnvPodFieldSpec](#containerenvpodfieldspec), [ContainerEnvContainerResourceSpec](#containerenvcontainerresourcespec)
####  Parent types: [ContainerSpec](#containerspec), [DCCustomParams](#dccustomparams), [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Abstract
EnvString | [name](#name) | False | False
## PodVolumeHostSpec
#### Parents: [PodVolumeBaseSpec](#podvolumebasespec)
####  Parent types: [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Abstract
Identifier | [name](#name) | False | False
String | [path](#path) | False | False
## DCRecreateParams
####  Parent types: [DCRecreateStrategy](#dcrecreatestrategy)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<DCLifecycleHook> | [mid](#mid) | False | False
Nullable<DCLifecycleHook> | [post](#post) | False | False
Nullable<DCLifecycleHook> | [pre](#pre) | False | False
Nullable<Positive<NonZero<Integer>>> | [timeoutSeconds](#timeoutseconds) | False | False
## DCTagImages
####  Parent types: [DCLifecycleHook](#dclifecyclehook)
####  Properties:

Name | Type | Identifier | Abstract
Identifier | [containerName](#containername) | False | False
Nullable<String> | [toApiVersion](#toapiversion) | False | False
Nullable<String> | [toFieldPath](#tofieldpath) | False | False
Nullable<Enum(u'Deployment', u'DeploymentConfig', u'ImageStreamTag')> | [toKind](#tokind) | False | False
Nullable<Identifier> | [toName](#toname) | False | False
Nullable<Identifier> | [toNamespace](#tonamespace) | False | False
Nullable<String> | [toResourceVersion](#toresourceversion) | False | False
Nullable<String> | [toUid](#touid) | False | False
## Secret
####  Children: [DockerCredentials](#dockercredentials), [TLSCredentials](#tlscredentials)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
Map<String, String> | [secrets](#secrets) | False | False
NonEmpty<String> | [type](#type) | False | False
## RouteDestPort
####  Parent types: [Route](#route)
####  Properties:

Name | Type | Identifier | Abstract
Identifier | [targetPort](#targetport) | False | False
## BaseSelector
####  Children: [MatchLabelsSelector](#matchlabelsselector), [MatchExpressionsSelector](#matchexpressionsselector)
####  Parent types: [DaemonSet](#daemonset), [Deployment](#deployment), [Job](#job), [PersistentVolumeClaim](#persistentvolumeclaim)
####  Properties:

Name | Type | Identifier | Abstract
## ContainerProbeHTTPSpec
#### Parents: [ContainerProbeBaseSpec](#containerprobebasespec)
####  Parent types: [ContainerSpec](#containerspec)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<Positive<NonZero<Integer>>> | [failureThreshold](#failurethreshold) | False | False
Nullable<Domain> | [host](#host) | False | False
Nullable<Positive<Integer>> | [initialDelaySeconds](#initialdelayseconds) | False | False
NonEmpty<Path> | [path](#path) | False | False
Nullable<Positive<NonZero<Integer>>> | [periodSeconds](#periodseconds) | False | False
Positive<NonZero<Integer>> | [port](#port) | False | True
Nullable<Enum(u'HTTP', u'HTTPS')> | [scheme](#scheme) | False | False
Nullable<Positive<NonZero<Integer>>> | [successThreshold](#successthreshold) | False | False
Nullable<Positive<NonZero<Integer>>> | [timeoutSeconds](#timeoutseconds) | False | False
## ServicePort
####  Parent types: [AWSLoadBalancerService](#awsloadbalancerservice), [ClusterIPService](#clusteripservice), [Service](#service)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<Identifier> | [name](#name) | False | False
Positive<NonZero<Integer>> | [port](#port) | False | False
Enum(u'TCP', u'UDP') | [protocol](#protocol) | False | False
OneOf<Positive<NonZero<Integer>>, Identifier> | [targetPort](#targetport) | False | False
## AWSElasticBlockStore
####  Parent types: [PersistentVolume](#persistentvolume)
####  Properties:

Name | Type | Identifier | Abstract
Enum(u'ext4') | [fsType](#fstype) | False | False
AWSVolID | [volumeID](#volumeid) | False | False
## ReplicationController
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
Nullable<Positive<NonZero<Integer>>> | [minReadySeconds](#minreadyseconds) | False | False
PodTemplateSpec | [pod_template](#pod_template) | False | False
Positive<NonZero<Integer>> | [replicas](#replicas) | False | False
Nullable<Map<String, String>> | [selector](#selector) | False | False
## SAImgPullSecretSubject
####  Parent types: [ServiceAccount](#serviceaccount)
####  Properties:

Name | Type | Identifier | Abstract
Identifier | [name](#name) | False | False
## Deployment
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
Nullable<Positive<NonZero<Integer>>> | [minReadySeconds](#minreadyseconds) | False | False
Nullable<Boolean> | [paused](#paused) | False | False
PodTemplateSpec | [pod_template](#pod_template) | False | False
Nullable<Positive<NonZero<Integer>>> | [progressDeadlineSeconds](#progressdeadlineseconds) | False | False
Positive<NonZero<Integer>> | [replicas](#replicas) | False | False
Nullable<Positive<NonZero<Integer>>> | [revisionHistoryLimit](#revisionhistorylimit) | False | False
Nullable<BaseSelector> | [selector](#selector) | False | False
Nullable<DplBaseUpdateStrategy> | [strategy](#strategy) | False | False
## PodImagePullSecret
####  Parent types: [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Abstract
Identifier | [name](#name) | False | False
## RoleSubject
####  Parent types: [ClusterRoleBinding](#clusterrolebinding), [PolicyBindingRoleBinding](#policybindingrolebinding), [RoleBindingBase](#rolebindingbase), [RoleBinding](#rolebinding)
####  Properties:

Name | Type | Identifier | Abstract
CaseIdentifier | [kind](#kind) | False | False
String | [name](#name) | False | False
Nullable<Identifier> | [ns](#ns) | False | False
## SecurityContextConstraints
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
Boolean | [allowHostDirVolumePlugin](#allowhostdirvolumeplugin) | False | False
Boolean | [allowHostIPC](#allowhostipc) | False | False
Boolean | [allowHostNetwork](#allowhostnetwork) | False | False
Boolean | [allowHostPID](#allowhostpid) | False | False
Boolean | [allowHostPorts](#allowhostports) | False | False
Boolean | [allowPrivilegedContainer](#allowprivilegedcontainer) | False | False
Nullable<List<String>> | [allowedCapabilities](#allowedcapabilities) | False | False
Nullable<List<String>> | [defaultAddCapabilities](#defaultaddcapabilities) | False | False
Nullable<SCCGroups> | [fsGroup](#fsgroup) | False | False
List<SystemIdentifier> | [groups](#groups) | False | False
Nullable<Positive<Integer>> | [priority](#priority) | False | False
Boolean | [readOnlyRootFilesystem](#readonlyrootfilesystem) | False | False
Nullable<List<String>> | [requiredDropCapabilities](#requireddropcapabilities) | False | False
Nullable<SCCRunAsUser> | [runAsUser](#runasuser) | False | False
Nullable<SCCSELinux> | [seLinuxContext](#selinuxcontext) | False | False
Nullable<List<String>> | [seccompProfiles](#seccompprofiles) | False | False
Nullable<SCCGroups> | [supplementalGroups](#supplementalgroups) | False | False
List<SystemIdentifier> | [users](#users) | False | False
List<Enum(u'configMap', u'downwardAPI', u'emptyDir', u'hostPath', u'nfs', u'persistentVolumeClaim', u'secret', u'*')> | [volumes](#volumes) | False | False
## Route
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | Identifier | True | False
Domain | [host](#host) | False | False
RouteDestPort | [port](#port) | False | False
Nullable<RouteTLS> | [tls](#tls) | False | False
NonEmpty<List<RouteDest>> | [to](#to) | False | False
Enum(u'Subdomain', u'None') | [wildcardPolicy](#wildcardpolicy) | False | False
## ContainerResourceSpec
####  Parent types: [ContainerSpec](#containerspec), [DCBaseUpdateStrategy](#dcbaseupdatestrategy), [DCCustomStrategy](#dccustomstrategy), [DCRecreateStrategy](#dcrecreatestrategy), [DCRollingStrategy](#dcrollingstrategy)
####  Properties:

Name | Type | Identifier | Abstract
ContainerResourceEachSpec | [limits](#limits) | False | False
ContainerResourceEachSpec | [requests](#requests) | False | False
## PolicyBindingRoleBinding
#### Parents: [RoleBindingXF](#rolebindingxf)
####  Parent types: [PolicyBinding](#policybinding)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<Map<String, String>> | [metadata](#metadata) | False | False
SystemIdentifier | [name](#name) | False | False
Identifier | [ns](#ns) | False | False
RoleRef | [roleRef](#roleref) | False | True
NonEmpty<List<RoleSubject>> | [subjects](#subjects) | False | True
## LifeCycle
####  Parent types: [ContainerSpec](#containerspec)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<LifeCycleProbe> | [postStart](#poststart) | False | False
Nullable<LifeCycleProbe> | [preStop](#prestop) | False | False
## RoleBinding
#### Parents: [RoleBindingBase](#rolebindingbase), [RoleBindingXF](#rolebindingxf)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract
name | SystemIdentifier | True | False
RoleRef | [roleRef](#roleref) | False | True
NonEmpty<List<RoleSubject>> | [subjects](#subjects) | False | True
## MatchLabelsSelector
#### Parents: [BaseSelector](#baseselector)
####  Parent types: [DaemonSet](#daemonset), [Deployment](#deployment), [Job](#job), [PersistentVolumeClaim](#persistentvolumeclaim)
####  Properties:

Name | Type | Identifier | Abstract
Map<String, String> | [matchLabels](#matchlabels) | False | False
## PolicyRule
####  Parent types: [ClusterRole](#clusterrole), [RoleBase](#rolebase), [Role](#role)
####  Properties:

Name | Type | Identifier | Abstract
NonEmpty<List<String>> | [apiGroups](#apigroups) | False | False
Nullable<String> | [attributeRestrictions](#attributerestrictions) | False | False
Nullable<List<String>> | [nonResourceURLs](#nonresourceurls) | False | False
Nullable<List<String>> | [resourceNames](#resourcenames) | False | False
NonEmpty<List<NonEmpty<String>>> | [resources](#resources) | False | False
NonEmpty<List<Enum(u'get', u'list', u'create', u'update', u'delete', u'deletecollection', u'watch')>> | [verbs](#verbs) | False | False
## ContainerEnvContainerResourceSpec
#### Parents: [ContainerEnvBaseSpec](#containerenvbasespec)
####  Parent types: [ContainerSpec](#containerspec), [DCCustomParams](#dccustomparams), [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<Identifier> | [containerName](#containername) | False | False
Nullable<NonEmpty<String>> | [divisor](#divisor) | False | False
EnvString | [name](#name) | False | False
Enum(u'limits.cpu', u'limits.memory', u'requests.cpu', u'requests.memory') | [resource](#resource) | False | False
## PodVolumeSecretSpec
#### Parents: [PodVolumeItemMapper](#podvolumeitemmapper), [PodVolumeBaseSpec](#podvolumebasespec)
####  Parent types: [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Abstract
Nullable<Positive<Integer>> | [defaultMode](#defaultmode) | False | False
Nullable<Map<String, String>> | [item_map](#item_map) | False | False
Identifier | [name](#name) | False | False
Identifier | [secret_name](#secret_name) | False | False
