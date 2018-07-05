## TLSCredentials
#### Parents: [Secret](#secret)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
secrets | Map<String, String> | False | False | - 
tls_cert | String | False | False | - 
tls_key | String | False | False | - 
type | NonEmpty<String> | False | False | - 
## Service
####  Children: [ClusterIPService](#clusteripservice), [AWSLoadBalancerService](#awsloadbalancerservice)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
ports | NonEmpty<List<ServicePort>> | False | True | - 
selector | NonEmpty<Map<String, String>> | False | True | - 
sessionAffinity | Nullable<Enum(u'ClientIP', u'None')> | False | False | - 
## DockerCredentials
#### Parents: [Secret](#secret)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
dockers | Map<String, Map<String, String>> | False | False | - 
secrets | Map<String, String> | False | False | - 
type | NonEmpty<String> | False | False | - 
## DplBaseUpdateStrategy
####  Children: [DplRecreateStrategy](#dplrecreatestrategy), [DplRollingUpdateStrategy](#dplrollingupdatestrategy)
####  Parent types: [Deployment](#deployment)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
## Role
#### Parents: [RoleBase](#rolebase)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
rules | NonEmpty<List<PolicyRule>> | False | False | - 
## Group
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
users | NonEmpty<List<UserIdentifier>> | False | False | - 
## RouteTLS
####  Parent types: [Route](#route)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
caCertificate | Nullable<NonEmpty<String>> | False | False | - 
certificate | Nullable<NonEmpty<String>> | False | False | - 
destinationCACertificate | Nullable<NonEmpty<String>> | False | False | - 
insecureEdgeTerminationPolicy | Enum(u'Allow', u'Disable', u'Redirect') | False | False | - 
key | Nullable<NonEmpty<String>> | False | False | - 
termination | Enum(u'edge', u'reencrypt', u'passthrough') | False | False | - 
## SCCRunAsUser
####  Parent types: [SecurityContextConstraints](#securitycontextconstraints)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
type | Enum(u'MustRunAs', u'RunAsAny', u'MustRunAsRange', u'MustRunAsNonRoot') | False | False | - 
uid | Nullable<Positive<NonZero<Integer>>> | False | False | - 
uidRangeMax | Nullable<Positive<NonZero<Integer>>> | False | False | - 
uidRangeMin | Nullable<Positive<NonZero<Integer>>> | False | False | - 
## PersistentVolumeClaim
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
accessModes | List<Enum(u'ReadWriteOnce', u'ReadOnlyMany', u'ReadWriteMany')> | False | False | - 
request | Memory | False | False | - 
selector | Nullable<BaseSelector> | False | False | - 
volumeName | Nullable<Identifier> | False | True | - 
## PodVolumePVCSpec
#### Parents: [PodVolumeBaseSpec](#podvolumebasespec)
####  Parent types: [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
claimName | Identifier | False | False | - 
name | Identifier | False | False | - 
## DCConfigChangeTrigger
#### Parents: [DCTrigger](#dctrigger)
####  Parent types: [DeploymentConfig](#deploymentconfig)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
## SecurityContext
####  Parent types: [ContainerSpec](#containerspec), [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
fsGroup | Nullable<Integer> | False | False | - 
privileged | Nullable<Boolean> | False | False | - 
runAsNonRoot | Nullable<Boolean> | False | False | - 
runAsUser | Nullable<Integer> | False | False | - 
supplementalGroups | Nullable<List<Integer>> | False | False | - 
## Project
#### Parents: [Namespace](#namespace)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
## PersistentVolume
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
accessModes | List<Enum(u'ReadWriteOnce', u'ReadOnlyMany', u'ReadWriteMany')> | False | False | - 
awsElasticBlockStore | Nullable<AWSElasticBlockStore> | False | False | - 
capacity | Memory | False | False | - 
claimRef | Nullable<PersistentVolumeRef> | False | False | - 
persistentVolumeReclaimPolicy | Nullable<Enum(u'Retain', u'Recycle', u'Delete')> | False | False | - 
## DeploymentConfig
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
minReadySeconds | Nullable<Positive<NonZero<Integer>>> | False | False | - 
paused | Nullable<Boolean> | False | False | - 
pod_template | PodTemplateSpec | False | False | - 
replicas | Positive<NonZero<Integer>> | False | False | - 
revisionHistoryLimit | Nullable<Positive<NonZero<Integer>>> | False | False | - 
selector | Nullable<Map<String, String>> | False | False | - 
strategy | DCBaseUpdateStrategy | False | False | - 
test | Boolean | False | False | - 
triggers | List<DCTrigger> | False | False | - 
## ContainerPort
####  Parent types: [ContainerSpec](#containerspec)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
containerPort | Positive<NonZero<Integer>> | False | False | - 
hostIP | Nullable<IP> | False | False | - 
hostPort | Nullable<Positive<NonZero<Integer>>> | False | False | - 
name | Nullable<String> | False | False | - 
protocol | Enum(u'TCP', u'UDP') | False | False | - 
## DCImageChangeTrigger
#### Parents: [DCTrigger](#dctrigger)
####  Parent types: [DeploymentConfig](#deploymentconfig)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
## RoleRef
####  Parent types: [ClusterRoleBinding](#clusterrolebinding), [PolicyBindingRoleBinding](#policybindingrolebinding), [RoleBindingBase](#rolebindingbase), [RoleBinding](#rolebinding)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Nullable<SystemIdentifier> | False | False | - 
ns | Nullable<Identifier> | False | False | - 
## LifeCycleHTTP
#### Parents: [LifeCycleProbe](#lifecycleprobe)
####  Parent types: [LifeCycle](#lifecycle)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
path | NonEmpty<Path> | False | False | - 
port | Positive<NonZero<Integer>> | False | False | - 
scheme | Nullable<Enum(u'HTTP', u'HTTPS')> | False | False | - 
## PodVolumeItemMapper
#### Parents: [PodVolumeBaseSpec](#podvolumebasespec)
####  Children: [PodVolumeConfigMapSpec](#podvolumeconfigmapspec), [PodVolumeSecretSpec](#podvolumesecretspec)
####  Parent types: [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
item_map | Nullable<Map<String, String>> | False | False | - 
name | Identifier | False | False | - 
## DaemonSet
#### Parents: [SelectorsPreProcessMixin](#selectorspreprocessmixin)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
pod_template | PodTemplateSpec | False | False | - 
selector | Nullable<BaseSelector> | False | True | - 
## DCBaseUpdateStrategy
####  Children: [DCRecreateStrategy](#dcrecreatestrategy), [DCRollingStrategy](#dcrollingstrategy), [DCCustomStrategy](#dccustomstrategy)
####  Parent types: [DeploymentConfig](#deploymentconfig)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
activeDeadlineSeconds | Nullable<Positive<NonZero<Integer>>> | False | False | - 
annotations | Map<String, String> | False | False | - 
labels | Map<String, String> | False | False | - 
resources | Nullable<ContainerResourceSpec> | False | False | - 
## Namespace
####  Children: [Project](#project)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
## ContainerEnvSpec
#### Parents: [ContainerEnvBaseSpec](#containerenvbasespec)
####  Parent types: [ContainerSpec](#containerspec), [DCCustomParams](#dccustomparams), [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | EnvString | False | False | - 
value | String | False | False | - 
## PodVolumeConfigMapSpec
#### Parents: [PodVolumeItemMapper](#podvolumeitemmapper), [PodVolumeBaseSpec](#podvolumebasespec)
####  Parent types: [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
defaultMode | Nullable<Positive<Integer>> | False | False | - 
item_map | Nullable<Map<String, String>> | False | False | - 
map_name | Identifier | False | False | - 
name | Identifier | False | False | - 
## MatchExpression
####  Parent types: [MatchExpressionsSelector](#matchexpressionsselector)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
key | NonEmpty<String> | False | False | - 
operator | Enum(u'In', u'NotIn', u'Exists', u'DoesNotExist') | False | False | - 
values | Nullable<List<String>> | False | False | - 
## SCCSELinux
####  Parent types: [SecurityContextConstraints](#securitycontextconstraints)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
level | Nullable<String> | False | False | - 
role | Nullable<String> | False | False | - 
strategy | Nullable<Enum(u'MustRunAs', u'RunAsAny')> | False | False | - 
type | Nullable<String> | False | False | - 
user | Nullable<String> | False | False | - 
## ClusterRoleBinding
#### Parents: [RoleBindingBase](#rolebindingbase), [RoleBindingXF](#rolebindingxf)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
roleRef | RoleRef | False | True | - 
subjects | NonEmpty<List<RoleSubject>> | False | True | - 
## AWSLoadBalancerService
#### Parents: [Service](#service)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
aws-load-balancer-backend-protocol | Nullable<Identifier> | False | False | - 
aws-load-balancer-ssl-cert | Nullable<ARN> | False | False | - 
externalTrafficPolicy | Nullable<Enum(u'Cluster', u'Local')> | False | False | - 
ports | NonEmpty<List<ServicePort>> | False | True | - 
selector | NonEmpty<Map<String, String>> | False | True | - 
sessionAffinity | Nullable<Enum(u'ClientIP', u'None')> | False | False | - 
## Job
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
activeDeadlineSeconds | Nullable<Positive<Integer>> | False | False | - 
completions | Nullable<Positive<NonZero<Integer>>> | False | False | - 
manualSelector | Nullable<Boolean> | False | False | - 
parallelism | Nullable<Positive<NonZero<Integer>>> | False | False | - 
pod_template | PodTemplateSpec | False | False | - 
selector | Nullable<BaseSelector> | False | False | - 
## RouteDestService
#### Parents: [RouteDest](#routedest)
####  Parent types: [Route](#route)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | False | False | - 
weight | Positive<NonZero<Integer>> | False | False | - 
## DCRecreateStrategy
#### Parents: [DCBaseUpdateStrategy](#dcbaseupdatestrategy)
####  Parent types: [DeploymentConfig](#deploymentconfig)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
activeDeadlineSeconds | Nullable<Positive<NonZero<Integer>>> | False | False | - 
annotations | Map<String, String> | False | False | - 
customParams | Nullable<DCCustomParams> | False | False | - 
labels | Map<String, String> | False | False | - 
recreateParams | Nullable<DCRecreateParams> | False | False | - 
resources | Nullable<ContainerResourceSpec> | False | False | - 
## DplRollingUpdateStrategy
#### Parents: [DplBaseUpdateStrategy](#dplbaseupdatestrategy)
####  Parent types: [Deployment](#deployment)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
maxSurge | SurgeSpec | False | False | - 
maxUnavailable | SurgeSpec | False | False | - 
## ContainerSpec
#### Parents: [EnvironmentPreProcessMixin](#environmentpreprocessmixin)
####  Parent types: [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
args | Nullable<List<String>> | False | False | - 
command | Nullable<List<String>> | False | False | - 
env | Nullable<List<ContainerEnvBaseSpec>> | False | True | - 
image | NonEmpty<String> | False | False | - 
imagePullPolicy | Nullable<Enum(u'Always', u'IfNotPresent')> | False | False | - 
kind | Nullable<Enum(u'DockerImage')> | False | False | - 
lifecycle | Nullable<LifeCycle> | False | False | - 
livenessProbe | Nullable<ContainerProbeBaseSpec> | False | False | - 
ports | Nullable<List<ContainerPort>> | False | True | - 
readinessProbe | Nullable<ContainerProbeBaseSpec> | False | False | - 
resources | Nullable<ContainerResourceSpec> | False | False | - 
securityContext | Nullable<SecurityContext> | False | False | - 
terminationMessagePath | Nullable<NonEmpty<Path>> | False | False | - 
volumeMounts | Nullable<List<ContainerVolumeMountSpec>> | False | True | - 
## DplRecreateStrategy
#### Parents: [DplBaseUpdateStrategy](#dplbaseupdatestrategy)
####  Parent types: [Deployment](#deployment)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
## DCTrigger
####  Children: [DCConfigChangeTrigger](#dcconfigchangetrigger), [DCImageChangeTrigger](#dcimagechangetrigger)
####  Parent types: [DeploymentConfig](#deploymentconfig)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
## ContainerEnvSecretSpec
#### Parents: [ContainerEnvBaseSpec](#containerenvbasespec)
####  Parent types: [ContainerSpec](#containerspec), [DCCustomParams](#dccustomparams), [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
key | NonEmpty<String> | False | False | - 
name | EnvString | False | False | - 
secret_name | Identifier | False | False | - 
## MatchExpressionsSelector
#### Parents: [BaseSelector](#baseselector)
####  Parent types: [DaemonSet](#daemonset), [Deployment](#deployment), [Job](#job), [PersistentVolumeClaim](#persistentvolumeclaim)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
matchExpressions | NonEmpty<List<MatchExpression>> | False | False | - 
## ContainerProbeBaseSpec
####  Children: [ContainerProbeTCPPortSpec](#containerprobetcpportspec), [ContainerProbeHTTPSpec](#containerprobehttpspec)
####  Parent types: [ContainerSpec](#containerspec)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
failureThreshold | Nullable<Positive<NonZero<Integer>>> | False | False | - 
initialDelaySeconds | Nullable<Positive<Integer>> | False | False | - 
periodSeconds | Nullable<Positive<NonZero<Integer>>> | False | False | - 
successThreshold | Nullable<Positive<NonZero<Integer>>> | False | False | - 
timeoutSeconds | Nullable<Positive<NonZero<Integer>>> | False | False | - 
## PodVolumeEmptyDirSpec
#### Parents: [PodVolumeBaseSpec](#podvolumebasespec)
####  Parent types: [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | False | False | - 
## PolicyBinding
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | ColonIdentifier | True | False | - 
roleBindings | List<PolicyBindingRoleBinding> | False | True | - 
## ConfigMap
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
files | Map<String, String> | False | False | - 
## SCCGroups
####  Parent types: [SecurityContextConstraints](#securitycontextconstraints)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
ranges | Nullable<List<SCCGroupRange>> | False | False | - 
type | Nullable<Enum(u'MustRunAs', u'RunAsAny')> | False | False | - 
## DCCustomStrategy
#### Parents: [DCBaseUpdateStrategy](#dcbaseupdatestrategy)
####  Parent types: [DeploymentConfig](#deploymentconfig)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
activeDeadlineSeconds | Nullable<Positive<NonZero<Integer>>> | False | False | - 
annotations | Map<String, String> | False | False | - 
customParams | DCCustomParams | False | False | - 
labels | Map<String, String> | False | False | - 
resources | Nullable<ContainerResourceSpec> | False | False | - 
## ContainerResourceEachSpec
####  Parent types: [ContainerResourceSpec](#containerresourcespec)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
cpu | Nullable<Positive<NonZero<Number>>> | False | True | - 
memory | Nullable<Memory> | False | False | - 
## StorageClass
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
parameters | Map<String, String> | False | False | - 
provisioner | String | False | False | - 
## DCRollingParams
####  Parent types: [DCRollingStrategy](#dcrollingstrategy)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
intervalSeconds | Nullable<Positive<NonZero<Integer>>> | False | False | - 
maxSurge | SurgeSpec | False | False | - 
maxUnavailable | SurgeSpec | False | False | - 
post | Nullable<DCLifecycleHook> | False | False | - 
pre | Nullable<DCLifecycleHook> | False | False | - 
timeoutSeconds | Nullable<Positive<NonZero<Integer>>> | False | False | - 
updatePeriodSeconds | Nullable<Positive<NonZero<Integer>>> | False | False | - 
## SCCGroupRange
####  Parent types: [SCCGroups](#sccgroups)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
max | Positive<NonZero<Integer>> | False | False | - 
min | Positive<NonZero<Integer>> | False | False | - 
## DCCustomParams
#### Parents: [EnvironmentPreProcessMixin](#environmentpreprocessmixin)
####  Parent types: [DCCustomStrategy](#dccustomstrategy), [DCRecreateStrategy](#dcrecreatestrategy), [DCRollingStrategy](#dcrollingstrategy)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
command | Nullable<List<String>> | False | False | - 
environment | Nullable<List<ContainerEnvBaseSpec>> | False | True | - 
image | NonEmpty<String> | False | False | - 
## ContainerVolumeMountSpec
####  Parent types: [ContainerSpec](#containerspec), [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | False | False | - 
path | NonEmpty<Path> | False | False | - 
readOnly | Nullable<Boolean> | False | False | - 
## LifeCycleProbe
####  Children: [LifeCycleExec](#lifecycleexec), [LifeCycleHTTP](#lifecyclehttp)
####  Parent types: [LifeCycle](#lifecycle)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
## SASecretSubject
####  Parent types: [ServiceAccount](#serviceaccount)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
kind | Nullable<CaseIdentifier> | False | False | - 
name | Nullable<Identifier> | False | False | - 
ns | Nullable<Identifier> | False | False | - 
## PodTemplateSpec
####  Parent types: [DaemonSet](#daemonset), [DeploymentConfig](#deploymentconfig), [Deployment](#deployment), [Job](#job), [ReplicationController](#replicationcontroller)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
containers | NonEmpty<List<ContainerSpec>> | False | False | - 
dnsPolicy | Nullable<Enum(u'ClusterFirst')> | False | False | - 
hostIPC | Nullable<Boolean> | False | False | - 
hostNetwork | Nullable<Boolean> | False | False | - 
hostPID | Nullable<Boolean> | False | False | - 
imagePullSecrets | Nullable<List<PodImagePullSecret>> | False | True | - 
name | Nullable<Identifier> | False | False | - 
nodeSelector | Nullable<Map<String, String>> | False | False | - 
restartPolicy | Nullable<Enum(u'Always', u'OnFailure', u'Never')> | False | False | - 
securityContext | Nullable<SecurityContext> | False | False | - 
serviceAccountName | Nullable<Identifier> | False | True | [serviceAccount](#serviceaccount) 
terminationGracePeriodSeconds | Nullable<Positive<Integer>> | False | False | - 
volumes | Nullable<List<PodVolumeBaseSpec>> | False | False | - 
## User
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | UserIdentifier | True | False | - 
fullName | Nullable<String> | False | False | - 
identities | NonEmpty<List<NonEmpty<String>>> | False | False | - 
## ContainerEnvConfigMapSpec
#### Parents: [ContainerEnvBaseSpec](#containerenvbasespec)
####  Parent types: [ContainerSpec](#containerspec), [DCCustomParams](#dccustomparams), [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
key | NonEmpty<String> | False | False | - 
map_name | Identifier | False | False | - 
name | EnvString | False | False | - 
## LifeCycleExec
#### Parents: [LifeCycleProbe](#lifecycleprobe)
####  Parent types: [LifeCycle](#lifecycle)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
command | NonEmpty<List<String>> | False | False | - 
## DCRollingStrategy
#### Parents: [DCBaseUpdateStrategy](#dcbaseupdatestrategy)
####  Parent types: [DeploymentConfig](#deploymentconfig)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
activeDeadlineSeconds | Nullable<Positive<NonZero<Integer>>> | False | False | - 
annotations | Map<String, String> | False | False | - 
customParams | Nullable<DCCustomParams> | False | False | - 
labels | Map<String, String> | False | False | - 
resources | Nullable<ContainerResourceSpec> | False | False | - 
rollingParams | Nullable<DCRollingParams> | False | False | - 
## RouteDest
####  Children: [RouteDestService](#routedestservice)
####  Parent types: [Route](#route)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
weight | Positive<NonZero<Integer>> | False | False | - 
## ContainerEnvPodFieldSpec
#### Parents: [ContainerEnvBaseSpec](#containerenvbasespec)
####  Parent types: [ContainerSpec](#containerspec), [DCCustomParams](#dccustomparams), [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
apiVersion | Nullable<Enum(u'v1')> | False | False | - 
fieldPath | Enum(u'metadata.name', u'metadata.namespace', u'metadata.labels', u'metadata.annotations', u'spec.nodeName', u'spec.serviceAccountName', u'status.podIP') | False | False | - 
name | EnvString | False | False | - 
## ServiceAccount
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
imagePullSecrets | Nullable<List<SAImgPullSecretSubject>> | False | True | - 
secrets | Nullable<List<SASecretSubject>> | False | True | - 
## PodVolumeBaseSpec
####  Children: [PodVolumeHostSpec](#podvolumehostspec), [PodVolumeItemMapper](#podvolumeitemmapper), [PodVolumePVCSpec](#podvolumepvcspec), [PodVolumeEmptyDirSpec](#podvolumeemptydirspec), [PodVolumeConfigMapSpec](#podvolumeconfigmapspec), [PodVolumeSecretSpec](#podvolumesecretspec)
####  Parent types: [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | False | False | - 
## ClusterRole
#### Parents: [RoleBase](#rolebase)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
rules | NonEmpty<List<PolicyRule>> | False | False | - 
## DCLifecycleHook
####  Parent types: [DCRecreateParams](#dcrecreateparams), [DCRollingParams](#dcrollingparams)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
execNewPod | Nullable<DCLifecycleNewPod> | False | False | - 
failurePolicy | Enum(u'Abort', u'Retry', u'Ignore') | False | False | - 
tagImages | Nullable<DCTagImages> | False | False | - 
## ClusterIPService
#### Parents: [Service](#service)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
clusterIP | Nullable<IPv4> | False | False | - 
ports | NonEmpty<List<ServicePort>> | False | True | - 
selector | NonEmpty<Map<String, String>> | False | True | - 
sessionAffinity | Nullable<Enum(u'ClientIP', u'None')> | False | False | - 
## PersistentVolumeRef
####  Parent types: [PersistentVolume](#persistentvolume)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
apiVersion | Nullable<String> | False | False | - 
kind | Nullable<CaseIdentifier> | False | False | - 
name | Nullable<Identifier> | False | False | - 
ns | Nullable<Identifier> | False | False | - 
## DCLifecycleNewPod
#### Parents: [EnvironmentPreProcessMixin](#environmentpreprocessmixin)
####  Parent types: [DCLifecycleHook](#dclifecyclehook)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
command | NonEmpty<List<String>> | False | False | - 
containerName | Identifier | False | False | - 
env | Nullable<List<ContainerEnvBaseSpec>> | False | True | - 
volumeMounts | Nullable<List<ContainerVolumeMountSpec>> | False | False | - 
volumes | Nullable<List<Identifier>> | False | False | - 
## ContainerProbeTCPPortSpec
#### Parents: [ContainerProbeBaseSpec](#containerprobebasespec)
####  Parent types: [ContainerSpec](#containerspec)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
failureThreshold | Nullable<Positive<NonZero<Integer>>> | False | False | - 
initialDelaySeconds | Nullable<Positive<Integer>> | False | False | - 
periodSeconds | Nullable<Positive<NonZero<Integer>>> | False | False | - 
port | Positive<NonZero<Integer>> | False | True | - 
successThreshold | Nullable<Positive<NonZero<Integer>>> | False | False | - 
timeoutSeconds | Nullable<Positive<NonZero<Integer>>> | False | False | - 
## ContainerEnvBaseSpec
####  Children: [ContainerEnvSpec](#containerenvspec), [ContainerEnvConfigMapSpec](#containerenvconfigmapspec), [ContainerEnvSecretSpec](#containerenvsecretspec), [ContainerEnvPodFieldSpec](#containerenvpodfieldspec), [ContainerEnvContainerResourceSpec](#containerenvcontainerresourcespec)
####  Parent types: [ContainerSpec](#containerspec), [DCCustomParams](#dccustomparams), [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | EnvString | False | False | - 
## PodVolumeHostSpec
#### Parents: [PodVolumeBaseSpec](#podvolumebasespec)
####  Parent types: [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | False | False | - 
path | String | False | False | - 
## DCRecreateParams
####  Parent types: [DCRecreateStrategy](#dcrecreatestrategy)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
mid | Nullable<DCLifecycleHook> | False | False | - 
post | Nullable<DCLifecycleHook> | False | False | - 
pre | Nullable<DCLifecycleHook> | False | False | - 
timeoutSeconds | Nullable<Positive<NonZero<Integer>>> | False | False | - 
## DCTagImages
####  Parent types: [DCLifecycleHook](#dclifecyclehook)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
containerName | Identifier | False | False | - 
toApiVersion | Nullable<String> | False | False | - 
toFieldPath | Nullable<String> | False | False | - 
toKind | Nullable<Enum(u'Deployment', u'DeploymentConfig', u'ImageStreamTag')> | False | False | - 
toName | Nullable<Identifier> | False | False | - 
toNamespace | Nullable<Identifier> | False | False | - 
toResourceVersion | Nullable<String> | False | False | - 
toUid | Nullable<String> | False | False | - 
## Secret
####  Children: [DockerCredentials](#dockercredentials), [TLSCredentials](#tlscredentials)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
secrets | Map<String, String> | False | False | - 
type | NonEmpty<String> | False | False | - 
## RouteDestPort
####  Parent types: [Route](#route)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
targetPort | Identifier | False | False | - 
## BaseSelector
####  Children: [MatchLabelsSelector](#matchlabelsselector), [MatchExpressionsSelector](#matchexpressionsselector)
####  Parent types: [DaemonSet](#daemonset), [Deployment](#deployment), [Job](#job), [PersistentVolumeClaim](#persistentvolumeclaim)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
## ContainerProbeHTTPSpec
#### Parents: [ContainerProbeBaseSpec](#containerprobebasespec)
####  Parent types: [ContainerSpec](#containerspec)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
failureThreshold | Nullable<Positive<NonZero<Integer>>> | False | False | - 
host | Nullable<Domain> | False | False | - 
initialDelaySeconds | Nullable<Positive<Integer>> | False | False | - 
path | NonEmpty<Path> | False | False | - 
periodSeconds | Nullable<Positive<NonZero<Integer>>> | False | False | - 
port | Positive<NonZero<Integer>> | False | True | - 
scheme | Nullable<Enum(u'HTTP', u'HTTPS')> | False | False | - 
successThreshold | Nullable<Positive<NonZero<Integer>>> | False | False | - 
timeoutSeconds | Nullable<Positive<NonZero<Integer>>> | False | False | - 
## ServicePort
####  Parent types: [AWSLoadBalancerService](#awsloadbalancerservice), [ClusterIPService](#clusteripservice), [Service](#service)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Nullable<Identifier> | False | False | - 
port | Positive<NonZero<Integer>> | False | False | - 
protocol | Enum(u'TCP', u'UDP') | False | False | - 
targetPort | OneOf<Positive<NonZero<Integer>>, Identifier> | False | False | - 
## AWSElasticBlockStore
####  Parent types: [PersistentVolume](#persistentvolume)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
fsType | Enum(u'ext4') | False | False | - 
volumeID | AWSVolID | False | False | - 
## ReplicationController
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
minReadySeconds | Nullable<Positive<NonZero<Integer>>> | False | False | - 
pod_template | PodTemplateSpec | False | False | - 
replicas | Positive<NonZero<Integer>> | False | False | - 
selector | Nullable<Map<String, String>> | False | False | - 
## SAImgPullSecretSubject
####  Parent types: [ServiceAccount](#serviceaccount)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | False | False | - 
## Deployment
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
minReadySeconds | Nullable<Positive<NonZero<Integer>>> | False | False | - 
paused | Nullable<Boolean> | False | False | - 
pod_template | PodTemplateSpec | False | False | - 
progressDeadlineSeconds | Nullable<Positive<NonZero<Integer>>> | False | False | - 
replicas | Positive<NonZero<Integer>> | False | False | - 
revisionHistoryLimit | Nullable<Positive<NonZero<Integer>>> | False | False | - 
selector | Nullable<BaseSelector> | False | False | - 
strategy | Nullable<DplBaseUpdateStrategy> | False | False | - 
## PodImagePullSecret
####  Parent types: [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | False | False | - 
## RoleSubject
####  Parent types: [ClusterRoleBinding](#clusterrolebinding), [PolicyBindingRoleBinding](#policybindingrolebinding), [RoleBindingBase](#rolebindingbase), [RoleBinding](#rolebinding)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
kind | CaseIdentifier | False | False | - 
name | String | False | False | - 
ns | Nullable<Identifier> | False | False | - 
## SecurityContextConstraints
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
allowHostDirVolumePlugin | Boolean | False | False | - 
allowHostIPC | Boolean | False | False | - 
allowHostNetwork | Boolean | False | False | - 
allowHostPID | Boolean | False | False | - 
allowHostPorts | Boolean | False | False | - 
allowPrivilegedContainer | Boolean | False | False | - 
allowedCapabilities | Nullable<List<String>> | False | False | - 
defaultAddCapabilities | Nullable<List<String>> | False | False | - 
fsGroup | Nullable<SCCGroups> | False | False | - 
groups | List<SystemIdentifier> | False | False | - 
priority | Nullable<Positive<Integer>> | False | False | - 
readOnlyRootFilesystem | Boolean | False | False | - 
requiredDropCapabilities | Nullable<List<String>> | False | False | - 
runAsUser | Nullable<SCCRunAsUser> | False | False | - 
seLinuxContext | Nullable<SCCSELinux> | False | False | - 
seccompProfiles | Nullable<List<String>> | False | False | - 
supplementalGroups | Nullable<SCCGroups> | False | False | - 
users | List<SystemIdentifier> | False | False | - 
volumes | List<Enum(u'configMap', u'downwardAPI', u'emptyDir', u'hostPath', u'nfs', u'persistentVolumeClaim', u'secret', u'*')> | False | False | - 
## Route
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | Identifier | True | False | - 
host | Domain | False | False | - 
port | RouteDestPort | False | False | - 
tls | Nullable<RouteTLS> | False | False | - 
to | NonEmpty<List<RouteDest>> | False | False | - 
wildcardPolicy | Enum(u'Subdomain', u'None') | False | False | - 
## ContainerResourceSpec
####  Parent types: [ContainerSpec](#containerspec), [DCBaseUpdateStrategy](#dcbaseupdatestrategy), [DCCustomStrategy](#dccustomstrategy), [DCRecreateStrategy](#dcrecreatestrategy), [DCRollingStrategy](#dcrollingstrategy)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
limits | ContainerResourceEachSpec | False | False | - 
requests | ContainerResourceEachSpec | False | False | - 
## PolicyBindingRoleBinding
#### Parents: [RoleBindingXF](#rolebindingxf)
####  Parent types: [PolicyBinding](#policybinding)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
metadata | Nullable<Map<String, String>> | False | False | - 
name | SystemIdentifier | False | False | - 
ns | Identifier | False | False | - 
roleRef | RoleRef | False | True | - 
subjects | NonEmpty<List<RoleSubject>> | False | True | - 
## LifeCycle
####  Parent types: [ContainerSpec](#containerspec)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
postStart | Nullable<LifeCycleProbe> | False | False | - 
preStop | Nullable<LifeCycleProbe> | False | False | - 
## RoleBinding
#### Parents: [RoleBindingBase](#rolebindingbase), [RoleBindingXF](#rolebindingxf)
```
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
```
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
name | SystemIdentifier | True | False | - 
roleRef | RoleRef | False | True | - 
subjects | NonEmpty<List<RoleSubject>> | False | True | - 
## MatchLabelsSelector
#### Parents: [BaseSelector](#baseselector)
####  Parent types: [DaemonSet](#daemonset), [Deployment](#deployment), [Job](#job), [PersistentVolumeClaim](#persistentvolumeclaim)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
matchLabels | Map<String, String> | False | False | - 
## PolicyRule
####  Parent types: [ClusterRole](#clusterrole), [RoleBase](#rolebase), [Role](#role)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
apiGroups | NonEmpty<List<String>> | False | False | - 
attributeRestrictions | Nullable<String> | False | False | - 
nonResourceURLs | Nullable<List<String>> | False | False | - 
resourceNames | Nullable<List<String>> | False | False | - 
resources | NonEmpty<List<NonEmpty<String>>> | False | False | - 
verbs | NonEmpty<List<Enum(u'get', u'list', u'create', u'update', u'delete', u'deletecollection', u'watch')>> | False | False | - 
## ContainerEnvContainerResourceSpec
#### Parents: [ContainerEnvBaseSpec](#containerenvbasespec)
####  Parent types: [ContainerSpec](#containerspec), [DCCustomParams](#dccustomparams), [DCLifecycleNewPod](#dclifecyclenewpod)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
containerName | Nullable<Identifier> | False | False | - 
divisor | Nullable<NonEmpty<String>> | False | False | - 
name | EnvString | False | False | - 
resource | Enum(u'limits.cpu', u'limits.memory', u'requests.cpu', u'requests.memory') | False | False | - 
## PodVolumeSecretSpec
#### Parents: [PodVolumeItemMapper](#podvolumeitemmapper), [PodVolumeBaseSpec](#podvolumebasespec)
####  Parent types: [PodTemplateSpec](#podtemplatespec)
####  Properties:

Name | Type | Identifier | Abstract | Mapping
---- | ---- | ---------- | -------- | -------
defaultMode | Nullable<Positive<Integer>> | False | False | - 
item_map | Nullable<Map<String, String>> | False | False | - 
name | Identifier | False | False | - 
secret_name | Identifier | False | False | - 
