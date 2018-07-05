## TLSCredentials
#### Parents: 
- [Secret](#secret)
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
secrets | Map&lt;String, String&gt; | False | - | - 
tls_cert | String | False | - | - 
tls_key | String | False | - | - 
type | NonEmpty&lt;String&gt; | False | - | - 
## Service
####  Children: 
- [ClusterIPService](#clusteripservice)
- [AWSLoadBalancerService](#awsloadbalancerservice)
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
ports | NonEmpty&lt;List&lt;[ServicePort](#serviceport)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
selector | NonEmpty&lt;Map&lt;String, String&gt;&gt; | False | &lt;unknown transformation&gt; | - 
sessionAffinity | Nullable&lt;Enum('ClientIP', 'None')&gt; | False | - | - 
## DockerCredentials
#### Parents: 
- [Secret](#secret)
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
dockers | Map&lt;String, Map&lt;String, String&gt;&gt; | False | - | - 
secrets | Map&lt;String, String&gt; | False | - | - 
type | NonEmpty&lt;String&gt; | False | - | - 
## DplBaseUpdateStrategy
####  Children: 
- [DplRecreateStrategy](#dplrecreatestrategy)
- [DplRollingUpdateStrategy](#dplrollingupdatestrategy)
####  Parent types: 
- [Deployment](#deployment)
## Role
#### Parents: 
- [RoleBase](#rolebase)
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
rules | NonEmpty&lt;List&lt;[PolicyRule](#policyrule)&gt;&gt; | False | - | - 
## Group
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
users | NonEmpty&lt;List&lt;UserIdentifier&gt;&gt; | False | - | - 
## RouteTLS
####  Parent types: 
- [Route](#route)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
caCertificate | Nullable&lt;NonEmpty&lt;String&gt;&gt; | False | - | - 
certificate | Nullable&lt;NonEmpty&lt;String&gt;&gt; | False | - | - 
destinationCACertificate | Nullable&lt;NonEmpty&lt;String&gt;&gt; | False | - | - 
insecureEdgeTerminationPolicy | Enum('Allow', 'Disable', 'Redirect') | False | - | - 
key | Nullable&lt;NonEmpty&lt;String&gt;&gt; | False | - | - 
termination | Enum('edge', 'reencrypt', 'passthrough') | False | - | - 
## SCCRunAsUser
####  Parent types: 
- [SecurityContextConstraints](#securitycontextconstraints)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
type | Enum('MustRunAs', 'RunAsAny', 'MustRunAsRange', 'MustRunAsNonRoot') | False | - | - 
uid | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
uidRangeMax | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
uidRangeMin | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
## PersistentVolumeClaim
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
accessModes | List&lt;Enum('ReadWriteOnce', 'ReadOnlyMany', 'ReadWriteMany')&gt; | False | - | - 
request | Memory | False | - | - 
selector | Nullable&lt;[BaseSelector](#baseselector)&gt; | False | - | - 
volumeName | Nullable&lt;Identifier&gt; | False | &lt;unknown transformation&gt; | - 
## PodVolumePVCSpec
#### Parents: 
- [PodVolumeBaseSpec](#podvolumebasespec)
####  Parent types: 
- [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
claimName | Identifier | False | - | - 
name | Identifier | False | - | - 
## DCConfigChangeTrigger
#### Parents: 
- [DCTrigger](#dctrigger)
####  Parent types: 
- [DeploymentConfig](#deploymentconfig)
## SecurityContext
####  Parent types: 
- [ContainerSpec](#containerspec)
- [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
fsGroup | Nullable&lt;Integer&gt; | False | - | - 
privileged | Nullable&lt;Boolean&gt; | False | - | - 
runAsNonRoot | Nullable&lt;Boolean&gt; | False | - | - 
runAsUser | Nullable&lt;Integer&gt; | False | - | - 
supplementalGroups | Nullable&lt;List&lt;Integer&gt;&gt; | False | - | - 
## Project
#### Parents: 
- [Namespace](#namespace)
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
## PersistentVolume
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
accessModes | List&lt;Enum('ReadWriteOnce', 'ReadOnlyMany', 'ReadWriteMany')&gt; | False | - | - 
awsElasticBlockStore | Nullable&lt;[AWSElasticBlockStore](#awselasticblockstore)&gt; | False | - | - 
capacity | Memory | False | - | - 
claimRef | Nullable&lt;[PersistentVolumeRef](#persistentvolumeref)&gt; | False | - | - 
persistentVolumeReclaimPolicy | Nullable&lt;Enum('Retain', 'Recycle', 'Delete')&gt; | False | - | - 
## DeploymentConfig
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
minReadySeconds | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
paused | Nullable&lt;Boolean&gt; | False | - | - 
pod_template | [PodTemplateSpec](#podtemplatespec) | False | - | - 
replicas | Positive&lt;NonZero&lt;Integer&gt;&gt; | False | - | - 
revisionHistoryLimit | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
selector | Nullable&lt;Map&lt;String, String&gt;&gt; | False | - | - 
strategy | [DCBaseUpdateStrategy](#dcbaseupdatestrategy) | False | - | - 
test | Boolean | False | - | - 
triggers | List&lt;[DCTrigger](#dctrigger)&gt; | False | - | - 
## ContainerPort
####  Parent types: 
- [ContainerSpec](#containerspec)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
containerPort | Positive&lt;NonZero&lt;Integer&gt;&gt; | False | - | - 
hostIP | Nullable&lt;IP&gt; | False | - | - 
hostPort | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
name | Nullable&lt;String&gt; | False | - | - 
protocol | Enum('TCP', 'UDP') | False | - | - 
## DCImageChangeTrigger
#### Parents: 
- [DCTrigger](#dctrigger)
####  Parent types: 
- [DeploymentConfig](#deploymentconfig)
## RoleRef
####  Parent types: 
- [ClusterRoleBinding](#clusterrolebinding)
- [PolicyBindingRoleBinding](#policybindingrolebinding)
- [RoleBinding](#rolebinding)
- [RoleBindingBase](#rolebindingbase)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Nullable&lt;SystemIdentifier&gt; | False | - | - 
ns | Nullable&lt;Identifier&gt; | False | - | - 
## LifeCycleHTTP
#### Parents: 
- [LifeCycleProbe](#lifecycleprobe)
####  Parent types: 
- [LifeCycle](#lifecycle)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
path | NonEmpty&lt;Path&gt; | False | - | - 
port | Positive&lt;NonZero&lt;Integer&gt;&gt; | False | - | - 
scheme | Nullable&lt;Enum('HTTP', 'HTTPS')&gt; | False | - | - 
## PodVolumeItemMapper
#### Parents: 
- [PodVolumeBaseSpec](#podvolumebasespec)
####  Children: 
- [PodVolumeConfigMapSpec](#podvolumeconfigmapspec)
- [PodVolumeSecretSpec](#podvolumesecretspec)
####  Parent types: 
- [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
item_map | Nullable&lt;Map&lt;String, String&gt;&gt; | False | - | - 
name | Identifier | False | - | - 
## DaemonSet
#### Parents: 
- [SelectorsPreProcessMixin](#selectorspreprocessmixin)
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
pod_template | [PodTemplateSpec](#podtemplatespec) | False | - | - 
selector | Nullable&lt;[BaseSelector](#baseselector)&gt; | False | &lt;unknown transformation&gt; | - 
## DCBaseUpdateStrategy
####  Children: 
- [DCRecreateStrategy](#dcrecreatestrategy)
- [DCRollingStrategy](#dcrollingstrategy)
- [DCCustomStrategy](#dccustomstrategy)
####  Parent types: 
- [DeploymentConfig](#deploymentconfig)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
activeDeadlineSeconds | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
annotations | Map&lt;String, String&gt; | False | - | - 
labels | Map&lt;String, String&gt; | False | - | - 
resources | Nullable&lt;[ContainerResourceSpec](#containerresourcespec)&gt; | False | - | - 
## Namespace
####  Children: 
- [Project](#project)
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
## ContainerEnvSpec
#### Parents: 
- [ContainerEnvBaseSpec](#containerenvbasespec)
####  Parent types: 
- [ContainerSpec](#containerspec)
- [DCCustomParams](#dccustomparams)
- [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | EnvString | False | - | - 
value | String | False | - | - 
## PodVolumeConfigMapSpec
#### Parents: 
- [PodVolumeItemMapper](#podvolumeitemmapper)
- [PodVolumeBaseSpec](#podvolumebasespec)
####  Parent types: 
- [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
defaultMode | Nullable&lt;Positive&lt;Integer&gt;&gt; | False | - | - 
item_map | Nullable&lt;Map&lt;String, String&gt;&gt; | False | - | - 
map_name | Identifier | False | - | - 
name | Identifier | False | - | - 
## MatchExpression
####  Parent types: 
- [MatchExpressionsSelector](#matchexpressionsselector)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
key | NonEmpty&lt;String&gt; | False | - | - 
operator | Enum('In', 'NotIn', 'Exists', 'DoesNotExist') | False | - | - 
values | Nullable&lt;List&lt;String&gt;&gt; | False | - | - 
## SCCSELinux
####  Parent types: 
- [SecurityContextConstraints](#securitycontextconstraints)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
level | Nullable&lt;String&gt; | False | - | - 
role | Nullable&lt;String&gt; | False | - | - 
strategy | Nullable&lt;Enum('MustRunAs', 'RunAsAny')&gt; | False | - | - 
type | Nullable&lt;String&gt; | False | - | - 
user | Nullable&lt;String&gt; | False | - | - 
## ClusterRoleBinding
#### Parents: 
- [RoleBindingBase](#rolebindingbase)
- [RoleBindingXF](#rolebindingxf)
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
roleRef | [RoleRef](#roleref) | False | &lt;unknown transformation&gt; | - 
subjects | NonEmpty&lt;List&lt;[RoleSubject](#rolesubject)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
## AWSLoadBalancerService
#### Parents: 
- [Service](#service)
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
aws-load-balancer-backend-protocol | Nullable&lt;Identifier&gt; | False | - | - 
aws-load-balancer-ssl-cert | Nullable&lt;ARN&gt; | False | - | - 
externalTrafficPolicy | Nullable&lt;Enum('Cluster', 'Local')&gt; | False | - | - 
ports | NonEmpty&lt;List&lt;[ServicePort](#serviceport)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
selector | NonEmpty&lt;Map&lt;String, String&gt;&gt; | False | &lt;unknown transformation&gt; | - 
sessionAffinity | Nullable&lt;Enum('ClientIP', 'None')&gt; | False | - | - 
## Job
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
activeDeadlineSeconds | Nullable&lt;Positive&lt;Integer&gt;&gt; | False | - | - 
completions | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
manualSelector | Nullable&lt;Boolean&gt; | False | - | - 
parallelism | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
pod_template | [PodTemplateSpec](#podtemplatespec) | False | - | - 
selector | Nullable&lt;[BaseSelector](#baseselector)&gt; | False | - | - 
## RouteDestService
#### Parents: 
- [RouteDest](#routedest)
####  Parent types: 
- [Route](#route)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | False | - | - 
weight | Positive&lt;NonZero&lt;Integer&gt;&gt; | False | - | - 
## DCRecreateStrategy
#### Parents: 
- [DCBaseUpdateStrategy](#dcbaseupdatestrategy)
####  Parent types: 
- [DeploymentConfig](#deploymentconfig)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
activeDeadlineSeconds | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
annotations | Map&lt;String, String&gt; | False | - | - 
customParams | Nullable&lt;[DCCustomParams](#dccustomparams)&gt; | False | - | - 
labels | Map&lt;String, String&gt; | False | - | - 
recreateParams | Nullable&lt;[DCRecreateParams](#dcrecreateparams)&gt; | False | - | - 
resources | Nullable&lt;[ContainerResourceSpec](#containerresourcespec)&gt; | False | - | - 
## DplRollingUpdateStrategy
#### Parents: 
- [DplBaseUpdateStrategy](#dplbaseupdatestrategy)
####  Parent types: 
- [Deployment](#deployment)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
maxSurge | SurgeSpec | False | - | - 
maxUnavailable | SurgeSpec | False | - | - 
## ContainerSpec
#### Parents: 
- [EnvironmentPreProcessMixin](#environmentpreprocessmixin)
####  Parent types: 
- [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
args | Nullable&lt;List&lt;String&gt;&gt; | False | - | - 
command | Nullable&lt;List&lt;String&gt;&gt; | False | - | - 
env | Nullable&lt;List&lt;[ContainerEnvBaseSpec](#containerenvbasespec)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
image | NonEmpty&lt;String&gt; | False | - | - 
imagePullPolicy | Nullable&lt;Enum('Always', 'IfNotPresent')&gt; | False | - | - 
kind | Nullable&lt;Enum('DockerImage')&gt; | False | - | - 
lifecycle | Nullable&lt;[LifeCycle](#lifecycle)&gt; | False | - | - 
livenessProbe | Nullable&lt;[ContainerProbeBaseSpec](#containerprobebasespec)&gt; | False | - | - 
ports | Nullable&lt;List&lt;[ContainerPort](#containerport)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
readinessProbe | Nullable&lt;[ContainerProbeBaseSpec](#containerprobebasespec)&gt; | False | - | - 
resources | Nullable&lt;[ContainerResourceSpec](#containerresourcespec)&gt; | False | - | - 
securityContext | Nullable&lt;[SecurityContext](#securitycontext)&gt; | False | - | - 
terminationMessagePath | Nullable&lt;NonEmpty&lt;Path&gt;&gt; | False | - | - 
volumeMounts | Nullable&lt;List&lt;[ContainerVolumeMountSpec](#containervolumemountspec)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
## DplRecreateStrategy
#### Parents: 
- [DplBaseUpdateStrategy](#dplbaseupdatestrategy)
####  Parent types: 
- [Deployment](#deployment)
## DCTrigger
####  Children: 
- [DCConfigChangeTrigger](#dcconfigchangetrigger)
- [DCImageChangeTrigger](#dcimagechangetrigger)
####  Parent types: 
- [DeploymentConfig](#deploymentconfig)
## ContainerEnvSecretSpec
#### Parents: 
- [ContainerEnvBaseSpec](#containerenvbasespec)
####  Parent types: 
- [ContainerSpec](#containerspec)
- [DCCustomParams](#dccustomparams)
- [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
key | NonEmpty&lt;String&gt; | False | - | - 
name | EnvString | False | - | - 
secret_name | Identifier | False | - | - 
## MatchExpressionsSelector
#### Parents: 
- [BaseSelector](#baseselector)
####  Parent types: 
- [DaemonSet](#daemonset)
- [Deployment](#deployment)
- [Job](#job)
- [PersistentVolumeClaim](#persistentvolumeclaim)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
matchExpressions | NonEmpty&lt;List&lt;[MatchExpression](#matchexpression)&gt;&gt; | False | - | - 
## ContainerProbeBaseSpec
####  Children: 
- [ContainerProbeTCPPortSpec](#containerprobetcpportspec)
- [ContainerProbeHTTPSpec](#containerprobehttpspec)
####  Parent types: 
- [ContainerSpec](#containerspec)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
failureThreshold | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
initialDelaySeconds | Nullable&lt;Positive&lt;Integer&gt;&gt; | False | - | - 
periodSeconds | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
successThreshold | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
timeoutSeconds | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
## PodVolumeEmptyDirSpec
#### Parents: 
- [PodVolumeBaseSpec](#podvolumebasespec)
####  Parent types: 
- [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | False | - | - 
## PolicyBinding
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | ColonIdentifier | True | False | - 
roleBindings | List&lt;[PolicyBindingRoleBinding](#policybindingrolebinding)&gt; | False | &lt;unknown transformation&gt; | - 
## ConfigMap
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
files | Map&lt;String, String&gt; | False | - | - 
## SCCGroups
####  Parent types: 
- [SecurityContextConstraints](#securitycontextconstraints)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
ranges | Nullable&lt;List&lt;[SCCGroupRange](#sccgrouprange)&gt;&gt; | False | - | - 
type | Nullable&lt;Enum('MustRunAs', 'RunAsAny')&gt; | False | - | - 
## DCCustomStrategy
#### Parents: 
- [DCBaseUpdateStrategy](#dcbaseupdatestrategy)
####  Parent types: 
- [DeploymentConfig](#deploymentconfig)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
activeDeadlineSeconds | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
annotations | Map&lt;String, String&gt; | False | - | - 
customParams | [DCCustomParams](#dccustomparams) | False | - | - 
labels | Map&lt;String, String&gt; | False | - | - 
resources | Nullable&lt;[ContainerResourceSpec](#containerresourcespec)&gt; | False | - | - 
## ContainerResourceEachSpec
####  Parent types: 
- [ContainerResourceSpec](#containerresourcespec)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
cpu | Nullable&lt;Positive&lt;NonZero&lt;Number&gt;&gt;&gt; | False | &lt;unknown transformation&gt; | - 
memory | Nullable&lt;Memory&gt; | False | - | - 
## StorageClass
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
parameters | Map&lt;String, String&gt; | False | - | - 
provisioner | String | False | - | - 
## DCRollingParams
####  Parent types: 
- [DCRollingStrategy](#dcrollingstrategy)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
intervalSeconds | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
maxSurge | SurgeSpec | False | - | - 
maxUnavailable | SurgeSpec | False | - | - 
post | Nullable&lt;[DCLifecycleHook](#dclifecyclehook)&gt; | False | - | - 
pre | Nullable&lt;[DCLifecycleHook](#dclifecyclehook)&gt; | False | - | - 
timeoutSeconds | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
updatePeriodSeconds | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
## SCCGroupRange
####  Parent types: 
- [SCCGroups](#sccgroups)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
max | Positive&lt;NonZero&lt;Integer&gt;&gt; | False | - | - 
min | Positive&lt;NonZero&lt;Integer&gt;&gt; | False | - | - 
## DCCustomParams
#### Parents: 
- [EnvironmentPreProcessMixin](#environmentpreprocessmixin)
####  Parent types: 
- [DCCustomStrategy](#dccustomstrategy)
- [DCRecreateStrategy](#dcrecreatestrategy)
- [DCRollingStrategy](#dcrollingstrategy)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
command | Nullable&lt;List&lt;String&gt;&gt; | False | - | - 
environment | Nullable&lt;List&lt;[ContainerEnvBaseSpec](#containerenvbasespec)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
image | NonEmpty&lt;String&gt; | False | - | - 
## ContainerVolumeMountSpec
####  Parent types: 
- [ContainerSpec](#containerspec)
- [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | False | - | - 
path | NonEmpty&lt;Path&gt; | False | - | - 
readOnly | Nullable&lt;Boolean&gt; | False | - | - 
## LifeCycleProbe
####  Children: 
- [LifeCycleExec](#lifecycleexec)
- [LifeCycleHTTP](#lifecyclehttp)
####  Parent types: 
- [LifeCycle](#lifecycle)
## SASecretSubject
####  Parent types: 
- [ServiceAccount](#serviceaccount)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
kind | Nullable&lt;CaseIdentifier&gt; | False | - | - 
name | Nullable&lt;Identifier&gt; | False | - | - 
ns | Nullable&lt;Identifier&gt; | False | - | - 
## PodTemplateSpec
####  Parent types: 
- [DaemonSet](#daemonset)
- [Deployment](#deployment)
- [DeploymentConfig](#deploymentconfig)
- [Job](#job)
- [ReplicationController](#replicationcontroller)
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
containers | NonEmpty&lt;List&lt;[ContainerSpec](#containerspec)&gt;&gt; | False | - | - 
dnsPolicy | Nullable&lt;Enum('ClusterFirst')&gt; | False | - | - 
hostIPC | Nullable&lt;Boolean&gt; | False | - | - 
hostNetwork | Nullable&lt;Boolean&gt; | False | - | - 
hostPID | Nullable&lt;Boolean&gt; | False | - | - 
imagePullSecrets | Nullable&lt;List&lt;[PodImagePullSecret](#podimagepullsecret)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
name | Nullable&lt;Identifier&gt; | False | - | - 
nodeSelector | Nullable&lt;Map&lt;String, String&gt;&gt; | False | - | - 
restartPolicy | Nullable&lt;Enum('Always', 'OnFailure', 'Never')&gt; | False | - | - 
securityContext | Nullable&lt;[SecurityContext](#securitycontext)&gt; | False | - | - 
serviceAccountName | Nullable&lt;Identifier&gt; | False | &lt;unknown transformation&gt; | [serviceAccount](#serviceaccount) 
terminationGracePeriodSeconds | Nullable&lt;Positive&lt;Integer&gt;&gt; | False | - | - 
volumes | Nullable&lt;List&lt;[PodVolumeBaseSpec](#podvolumebasespec)&gt;&gt; | False | - | - 
## User
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | UserIdentifier | True | False | - 
fullName | Nullable&lt;String&gt; | False | - | - 
identities | NonEmpty&lt;List&lt;NonEmpty&lt;String&gt;&gt;&gt; | False | - | - 
## ContainerEnvConfigMapSpec
#### Parents: 
- [ContainerEnvBaseSpec](#containerenvbasespec)
####  Parent types: 
- [ContainerSpec](#containerspec)
- [DCCustomParams](#dccustomparams)
- [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
key | NonEmpty&lt;String&gt; | False | - | - 
map_name | Identifier | False | - | - 
name | EnvString | False | - | - 
## LifeCycleExec
#### Parents: 
- [LifeCycleProbe](#lifecycleprobe)
####  Parent types: 
- [LifeCycle](#lifecycle)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
command | NonEmpty&lt;List&lt;String&gt;&gt; | False | - | - 
## DCRollingStrategy
#### Parents: 
- [DCBaseUpdateStrategy](#dcbaseupdatestrategy)
####  Parent types: 
- [DeploymentConfig](#deploymentconfig)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
activeDeadlineSeconds | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
annotations | Map&lt;String, String&gt; | False | - | - 
customParams | Nullable&lt;[DCCustomParams](#dccustomparams)&gt; | False | - | - 
labels | Map&lt;String, String&gt; | False | - | - 
resources | Nullable&lt;[ContainerResourceSpec](#containerresourcespec)&gt; | False | - | - 
rollingParams | Nullable&lt;[DCRollingParams](#dcrollingparams)&gt; | False | - | - 
## RouteDest
####  Children: 
- [RouteDestService](#routedestservice)
####  Parent types: 
- [Route](#route)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
weight | Positive&lt;NonZero&lt;Integer&gt;&gt; | False | - | - 
## ContainerEnvPodFieldSpec
#### Parents: 
- [ContainerEnvBaseSpec](#containerenvbasespec)
####  Parent types: 
- [ContainerSpec](#containerspec)
- [DCCustomParams](#dccustomparams)
- [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
apiVersion | Nullable&lt;Enum('v1')&gt; | False | - | - 
fieldPath | Enum('metadata.name', 'metadata.namespace', 'metadata.labels', 'metadata.annotations', 'spec.nodeName', 'spec.serviceAccountName', 'status.podIP') | False | - | - 
name | EnvString | False | - | - 
## ServiceAccount
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
imagePullSecrets | Nullable&lt;List&lt;[SAImgPullSecretSubject](#saimgpullsecretsubject)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
secrets | Nullable&lt;List&lt;[SASecretSubject](#sasecretsubject)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
## PodVolumeBaseSpec
####  Children: 
- [PodVolumeHostSpec](#podvolumehostspec)
- [PodVolumeItemMapper](#podvolumeitemmapper)
- [PodVolumePVCSpec](#podvolumepvcspec)
- [PodVolumeEmptyDirSpec](#podvolumeemptydirspec)
- [PodVolumeConfigMapSpec](#podvolumeconfigmapspec)
- [PodVolumeSecretSpec](#podvolumesecretspec)
####  Parent types: 
- [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | False | - | - 
## ClusterRole
#### Parents: 
- [RoleBase](#rolebase)
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
rules | NonEmpty&lt;List&lt;[PolicyRule](#policyrule)&gt;&gt; | False | - | - 
## DCLifecycleHook
####  Parent types: 
- [DCRecreateParams](#dcrecreateparams)
- [DCRollingParams](#dcrollingparams)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
execNewPod | Nullable&lt;[DCLifecycleNewPod](#dclifecyclenewpod)&gt; | False | - | - 
failurePolicy | Enum('Abort', 'Retry', 'Ignore') | False | - | - 
tagImages | Nullable&lt;[DCTagImages](#dctagimages)&gt; | False | - | - 
## ClusterIPService
#### Parents: 
- [Service](#service)
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
clusterIP | Nullable&lt;IPv4&gt; | False | - | - 
ports | NonEmpty&lt;List&lt;[ServicePort](#serviceport)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
selector | NonEmpty&lt;Map&lt;String, String&gt;&gt; | False | &lt;unknown transformation&gt; | - 
sessionAffinity | Nullable&lt;Enum('ClientIP', 'None')&gt; | False | - | - 
## PersistentVolumeRef
####  Parent types: 
- [PersistentVolume](#persistentvolume)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
apiVersion | Nullable&lt;String&gt; | False | - | - 
kind | Nullable&lt;CaseIdentifier&gt; | False | - | - 
name | Nullable&lt;Identifier&gt; | False | - | - 
ns | Nullable&lt;Identifier&gt; | False | - | - 
## DCLifecycleNewPod
#### Parents: 
- [EnvironmentPreProcessMixin](#environmentpreprocessmixin)
####  Parent types: 
- [DCLifecycleHook](#dclifecyclehook)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
command | NonEmpty&lt;List&lt;String&gt;&gt; | False | - | - 
containerName | Identifier | False | - | - 
env | Nullable&lt;List&lt;[ContainerEnvBaseSpec](#containerenvbasespec)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
volumeMounts | Nullable&lt;List&lt;[ContainerVolumeMountSpec](#containervolumemountspec)&gt;&gt; | False | - | - 
volumes | Nullable&lt;List&lt;Identifier&gt;&gt; | False | - | - 
## ContainerProbeTCPPortSpec
#### Parents: 
- [ContainerProbeBaseSpec](#containerprobebasespec)
####  Parent types: 
- [ContainerSpec](#containerspec)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
failureThreshold | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
initialDelaySeconds | Nullable&lt;Positive&lt;Integer&gt;&gt; | False | - | - 
periodSeconds | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
port | Positive&lt;NonZero&lt;Integer&gt;&gt; | False | &lt;unknown transformation&gt; | - 
successThreshold | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
timeoutSeconds | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
## ContainerEnvBaseSpec
####  Children: 
- [ContainerEnvSpec](#containerenvspec)
- [ContainerEnvConfigMapSpec](#containerenvconfigmapspec)
- [ContainerEnvSecretSpec](#containerenvsecretspec)
- [ContainerEnvPodFieldSpec](#containerenvpodfieldspec)
- [ContainerEnvContainerResourceSpec](#containerenvcontainerresourcespec)
####  Parent types: 
- [ContainerSpec](#containerspec)
- [DCCustomParams](#dccustomparams)
- [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | EnvString | False | - | - 
## PodVolumeHostSpec
#### Parents: 
- [PodVolumeBaseSpec](#podvolumebasespec)
####  Parent types: 
- [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | False | - | - 
path | String | False | - | - 
## DCRecreateParams
####  Parent types: 
- [DCRecreateStrategy](#dcrecreatestrategy)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
mid | Nullable&lt;[DCLifecycleHook](#dclifecyclehook)&gt; | False | - | - 
post | Nullable&lt;[DCLifecycleHook](#dclifecyclehook)&gt; | False | - | - 
pre | Nullable&lt;[DCLifecycleHook](#dclifecyclehook)&gt; | False | - | - 
timeoutSeconds | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
## DCTagImages
####  Parent types: 
- [DCLifecycleHook](#dclifecyclehook)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
containerName | Identifier | False | - | - 
toApiVersion | Nullable&lt;String&gt; | False | - | - 
toFieldPath | Nullable&lt;String&gt; | False | - | - 
toKind | Nullable&lt;Enum('Deployment', 'DeploymentConfig', 'ImageStreamTag')&gt; | False | - | - 
toName | Nullable&lt;Identifier&gt; | False | - | - 
toNamespace | Nullable&lt;Identifier&gt; | False | - | - 
toResourceVersion | Nullable&lt;String&gt; | False | - | - 
toUid | Nullable&lt;String&gt; | False | - | - 
## Secret
####  Children: 
- [DockerCredentials](#dockercredentials)
- [TLSCredentials](#tlscredentials)
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
secrets | Map&lt;String, String&gt; | False | - | - 
type | NonEmpty&lt;String&gt; | False | - | - 
## RouteDestPort
####  Parent types: 
- [Route](#route)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
targetPort | Identifier | False | - | - 
## BaseSelector
####  Children: 
- [MatchLabelsSelector](#matchlabelsselector)
- [MatchExpressionsSelector](#matchexpressionsselector)
####  Parent types: 
- [DaemonSet](#daemonset)
- [Deployment](#deployment)
- [Job](#job)
- [PersistentVolumeClaim](#persistentvolumeclaim)
## ContainerProbeHTTPSpec
#### Parents: 
- [ContainerProbeBaseSpec](#containerprobebasespec)
####  Parent types: 
- [ContainerSpec](#containerspec)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
failureThreshold | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
host | Nullable&lt;Domain&gt; | False | - | - 
initialDelaySeconds | Nullable&lt;Positive&lt;Integer&gt;&gt; | False | - | - 
path | NonEmpty&lt;Path&gt; | False | - | - 
periodSeconds | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
port | Positive&lt;NonZero&lt;Integer&gt;&gt; | False | &lt;unknown transformation&gt; | - 
scheme | Nullable&lt;Enum('HTTP', 'HTTPS')&gt; | False | - | - 
successThreshold | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
timeoutSeconds | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
## ServicePort
####  Parent types: 
- [AWSLoadBalancerService](#awsloadbalancerservice)
- [ClusterIPService](#clusteripservice)
- [Service](#service)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Nullable&lt;Identifier&gt; | False | - | - 
port | Positive&lt;NonZero&lt;Integer&gt;&gt; | False | - | - 
protocol | Enum('TCP', 'UDP') | False | - | - 
targetPort | OneOf&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;, Identifier&gt; | False | - | - 
## AWSElasticBlockStore
####  Parent types: 
- [PersistentVolume](#persistentvolume)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
fsType | Enum('ext4') | False | - | - 
volumeID | AWSVolID | False | - | - 
## ReplicationController
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
minReadySeconds | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
pod_template | [PodTemplateSpec](#podtemplatespec) | False | - | - 
replicas | Positive&lt;NonZero&lt;Integer&gt;&gt; | False | - | - 
selector | Nullable&lt;Map&lt;String, String&gt;&gt; | False | - | - 
## SAImgPullSecretSubject
####  Parent types: 
- [ServiceAccount](#serviceaccount)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | False | - | - 
## Deployment
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
minReadySeconds | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
paused | Nullable&lt;Boolean&gt; | False | - | - 
pod_template | [PodTemplateSpec](#podtemplatespec) | False | - | - 
progressDeadlineSeconds | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
replicas | Positive&lt;NonZero&lt;Integer&gt;&gt; | False | - | - 
revisionHistoryLimit | Nullable&lt;Positive&lt;NonZero&lt;Integer&gt;&gt;&gt; | False | - | - 
selector | Nullable&lt;[BaseSelector](#baseselector)&gt; | False | - | - 
strategy | Nullable&lt;[DplBaseUpdateStrategy](#dplbaseupdatestrategy)&gt; | False | - | - 
## PodImagePullSecret
####  Parent types: 
- [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | False | - | - 
## RoleSubject
####  Parent types: 
- [ClusterRoleBinding](#clusterrolebinding)
- [PolicyBindingRoleBinding](#policybindingrolebinding)
- [RoleBinding](#rolebinding)
- [RoleBindingBase](#rolebindingbase)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
kind | CaseIdentifier | False | - | - 
name | String | False | - | - 
ns | Nullable&lt;Identifier&gt; | False | - | - 
## SecurityContextConstraints
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
allowHostDirVolumePlugin | Boolean | False | - | - 
allowHostIPC | Boolean | False | - | - 
allowHostNetwork | Boolean | False | - | - 
allowHostPID | Boolean | False | - | - 
allowHostPorts | Boolean | False | - | - 
allowPrivilegedContainer | Boolean | False | - | - 
allowedCapabilities | Nullable&lt;List&lt;String&gt;&gt; | False | - | - 
defaultAddCapabilities | Nullable&lt;List&lt;String&gt;&gt; | False | - | - 
fsGroup | Nullable&lt;[SCCGroups](#sccgroups)&gt; | False | - | - 
groups | List&lt;SystemIdentifier&gt; | False | - | - 
priority | Nullable&lt;Positive&lt;Integer&gt;&gt; | False | - | - 
readOnlyRootFilesystem | Boolean | False | - | - 
requiredDropCapabilities | Nullable&lt;List&lt;String&gt;&gt; | False | - | - 
runAsUser | Nullable&lt;[SCCRunAsUser](#sccrunasuser)&gt; | False | - | - 
seLinuxContext | Nullable&lt;[SCCSELinux](#sccselinux)&gt; | False | - | - 
seccompProfiles | Nullable&lt;List&lt;String&gt;&gt; | False | - | - 
supplementalGroups | Nullable&lt;[SCCGroups](#sccgroups)&gt; | False | - | - 
users | List&lt;SystemIdentifier&gt; | False | - | - 
volumes | List&lt;Enum('configMap', 'downwardAPI', 'emptyDir', 'hostPath', 'nfs', 'persistentVolumeClaim', 'secret', '*')&gt; | False | - | - 
## Route
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | Identifier | True | False | - 
host | Domain | False | - | - 
port | [RouteDestPort](#routedestport) | False | - | - 
tls | Nullable&lt;[RouteTLS](#routetls)&gt; | False | - | - 
to | NonEmpty&lt;List&lt;[RouteDest](#routedest)&gt;&gt; | False | - | - 
wildcardPolicy | Enum('Subdomain', 'None') | False | - | - 
## ContainerResourceSpec
####  Parent types: 
- [ContainerSpec](#containerspec)
- [DCBaseUpdateStrategy](#dcbaseupdatestrategy)
- [DCCustomStrategy](#dccustomstrategy)
- [DCRecreateStrategy](#dcrecreatestrategy)
- [DCRollingStrategy](#dcrollingstrategy)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
limits | [ContainerResourceEachSpec](#containerresourceeachspec) | False | - | - 
requests | [ContainerResourceEachSpec](#containerresourceeachspec) | False | - | - 
## PolicyBindingRoleBinding
#### Parents: 
- [RoleBindingXF](#rolebindingxf)
####  Parent types: 
- [PolicyBinding](#policybinding)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
metadata | Nullable&lt;Map&lt;String, String&gt;&gt; | False | - | - 
name | SystemIdentifier | False | - | - 
ns | Identifier | False | - | - 
roleRef | [RoleRef](#roleref) | False | &lt;unknown transformation&gt; | - 
subjects | NonEmpty&lt;List&lt;[RoleSubject](#rolesubject)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
## LifeCycle
####  Parent types: 
- [ContainerSpec](#containerspec)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
postStart | Nullable&lt;[LifeCycleProbe](#lifecycleprobe)&gt; | False | - | - 
preStop | Nullable&lt;[LifeCycleProbe](#lifecycleprobe)&gt; | False | - | - 
## RoleBinding
#### Parents: 
- [RoleBindingBase](#rolebindingbase)
- [RoleBindingXF](#rolebindingxf)
#### Metadata
```
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | SystemIdentifier | True | False | - 
roleRef | [RoleRef](#roleref) | False | &lt;unknown transformation&gt; | - 
subjects | NonEmpty&lt;List&lt;[RoleSubject](#rolesubject)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
## MatchLabelsSelector
#### Parents: 
- [BaseSelector](#baseselector)
####  Parent types: 
- [DaemonSet](#daemonset)
- [Deployment](#deployment)
- [Job](#job)
- [PersistentVolumeClaim](#persistentvolumeclaim)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
matchLabels | Map&lt;String, String&gt; | False | - | - 
## PolicyRule
####  Parent types: 
- [ClusterRole](#clusterrole)
- [Role](#role)
- [RoleBase](#rolebase)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
apiGroups | NonEmpty&lt;List&lt;String&gt;&gt; | False | - | - 
attributeRestrictions | Nullable&lt;String&gt; | False | - | - 
nonResourceURLs | Nullable&lt;List&lt;String&gt;&gt; | False | - | - 
resourceNames | Nullable&lt;List&lt;String&gt;&gt; | False | - | - 
resources | NonEmpty&lt;List&lt;NonEmpty&lt;String&gt;&gt;&gt; | False | - | - 
verbs | NonEmpty&lt;List&lt;Enum('get', 'list', 'create', 'update', 'delete', 'deletecollection', 'watch')&gt;&gt; | False | - | - 
## ContainerEnvContainerResourceSpec
#### Parents: 
- [ContainerEnvBaseSpec](#containerenvbasespec)
####  Parent types: 
- [ContainerSpec](#containerspec)
- [DCCustomParams](#dccustomparams)
- [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
containerName | Nullable&lt;Identifier&gt; | False | - | - 
divisor | Nullable&lt;NonEmpty&lt;String&gt;&gt; | False | - | - 
name | EnvString | False | - | - 
resource | Enum('limits.cpu', 'limits.memory', 'requests.cpu', 'requests.memory') | False | - | - 
## PodVolumeSecretSpec
#### Parents: 
- [PodVolumeItemMapper](#podvolumeitemmapper)
- [PodVolumeBaseSpec](#podvolumebasespec)
####  Parent types: 
- [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
defaultMode | Nullable&lt;Positive&lt;Integer&gt;&gt; | False | - | - 
item_map | Nullable&lt;Map&lt;String, String&gt;&gt; | False | - | - 
name | Identifier | False | - | - 
secret_name | Identifier | False | - | - 
