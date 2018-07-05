## TLSCredentials

```
TLSCredentials (abstract type):
  parents: Secret
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    secrets:              Map<String, String>
    tls_cert:             String
    tls_key:              String
    type:                 NonEmpty<String>

```
## Service

```
Service:
  children: ClusterIPService, AWSLoadBalancerService
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
   *ports:                NonEmpty<List<ServicePort>>
   *selector:             NonEmpty<Map<String, String>>
    sessionAffinity:      Nullable<Enum(u'ClientIP', u'None')>

```
## DockerCredentials

```
DockerCredentials (abstract type):
  parents: Secret
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    dockers:              Map<String, Map<String, String>>
    secrets:              Map<String, String>
    type:                 NonEmpty<String>

```
## DplBaseUpdateStrategy

```
DplBaseUpdateStrategy:
  children: DplRecreateStrategy, DplRollingUpdateStrategy
  parent types: Deployment
  properties:

```
## Role

```
Role (abstract type):
  parents: RoleBase
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    rules:                NonEmpty<List<PolicyRule>>

```
## Group

```
Group (abstract type):
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    users:                NonEmpty<List<UserIdentifier>>

```
## RouteTLS

```
RouteTLS (abstract type):
  parent types: Route
  properties:
    caCertificate:        Nullable<NonEmpty<String>>
    certificate:          Nullable<NonEmpty<String>>
    destinationCACertificate: Nullable<NonEmpty<String>>
    insecureEdgeTerminationPolicy: Enum(u'Allow', u'Disable', u'Redirect')
    key:                  Nullable<NonEmpty<String>>
    termination:          Enum(u'edge', u'reencrypt', u'passthrough')

```
## SCCRunAsUser

```
SCCRunAsUser (abstract type):
  parent types: SecurityContextConstraints
  properties:
    type:                 Enum(u'MustRunAs', u'RunAsAny', u'MustRunAsRange', u'MustRunAsNonRoot')
    uid:                  Nullable<Positive<NonZero<Integer>>>
    uidRangeMax:          Nullable<Positive<NonZero<Integer>>>
    uidRangeMin:          Nullable<Positive<NonZero<Integer>>>

```
## PersistentVolumeClaim

```
PersistentVolumeClaim (abstract type):
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    accessModes:          List<Enum(u'ReadWriteOnce', u'ReadOnlyMany', u'ReadWriteMany')>
    request:              Memory
    selector:             Nullable<BaseSelector>
   *volumeName:           Nullable<Identifier>

```
## PodVolumePVCSpec

```
PodVolumePVCSpec (abstract type):
  parents: PodVolumeBaseSpec
  parent types: PodTemplateSpec
  properties:
    claimName:            Identifier
    name:                 Identifier

```
## DCConfigChangeTrigger

```
DCConfigChangeTrigger (abstract type):
  parents: DCTrigger
  parent types: DeploymentConfig
  properties:

```
## SecurityContext

```
SecurityContext (abstract type):
  parent types: ContainerSpec, PodTemplateSpec
  properties:
    fsGroup:              Nullable<Integer>
    privileged:           Nullable<Boolean>
    runAsNonRoot:         Nullable<Boolean>
    runAsUser:            Nullable<Integer>
    supplementalGroups:   Nullable<List<Integer>>

```
## Project

```
Project (abstract type):
  parents: Namespace
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier

```
## PersistentVolume

```
PersistentVolume (abstract type):
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    accessModes:          List<Enum(u'ReadWriteOnce', u'ReadOnlyMany', u'ReadWriteMany')>
    awsElasticBlockStore: Nullable<AWSElasticBlockStore>
    capacity:             Memory
    claimRef:             Nullable<PersistentVolumeRef>
    persistentVolumeReclaimPolicy: Nullable<Enum(u'Retain', u'Recycle', u'Delete')>

```
## DeploymentConfig

```
DeploymentConfig (abstract type):
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    minReadySeconds:      Nullable<Positive<NonZero<Integer>>>
    paused:               Nullable<Boolean>
    pod_template:         PodTemplateSpec
    replicas:             Positive<NonZero<Integer>>
    revisionHistoryLimit: Nullable<Positive<NonZero<Integer>>>
    selector:             Nullable<Map<String, String>>
    strategy:             DCBaseUpdateStrategy
    test:                 Boolean
    triggers:             List<DCTrigger>

```
## ContainerPort

```
ContainerPort (abstract type):
  parent types: ContainerSpec
  properties:
    containerPort:        Positive<NonZero<Integer>>
    hostIP:               Nullable<IP>
    hostPort:             Nullable<Positive<NonZero<Integer>>>
    name:                 Nullable<String>
    protocol:             Enum(u'TCP', u'UDP')

```
## DCImageChangeTrigger

```
DCImageChangeTrigger (abstract type):
  parents: DCTrigger
  parent types: DeploymentConfig
  properties:

```
## RoleRef

```
RoleRef (abstract type):
  parent types: ClusterRoleBinding, PolicyBindingRoleBinding, RoleBinding, RoleBindingBase
  properties:
    name:                 Nullable<SystemIdentifier>
    ns:                   Nullable<Identifier>

```
## LifeCycleHTTP

```
LifeCycleHTTP (abstract type):
  parents: LifeCycleProbe
  parent types: LifeCycle
  properties:
    path:                 NonEmpty<Path>
    port:                 Positive<NonZero<Integer>>
    scheme:               Nullable<Enum(u'HTTP', u'HTTPS')>

```
## PodVolumeItemMapper

```
PodVolumeItemMapper:
  parents: PodVolumeBaseSpec
  children: PodVolumeConfigMapSpec, PodVolumeSecretSpec
  parent types: PodTemplateSpec
  properties:
    item_map:             Nullable<Map<String, String>>
    name:                 Identifier

```
## DaemonSet

```
DaemonSet (abstract type):
  parents: SelectorsPreProcessMixin
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    pod_template:         PodTemplateSpec
   *selector:             Nullable<BaseSelector>

```
## DCBaseUpdateStrategy

```
DCBaseUpdateStrategy:
  children: DCRecreateStrategy, DCRollingStrategy, DCCustomStrategy
  parent types: DeploymentConfig
  properties:
    activeDeadlineSeconds: Nullable<Positive<NonZero<Integer>>>
    annotations:          Map<String, String>
    labels:               Map<String, String>
    resources:            Nullable<ContainerResourceSpec>

```
## Namespace

```
Namespace (abstract type):
  children: Project
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier

```
## ContainerEnvSpec

```
ContainerEnvSpec (abstract type):
  parents: ContainerEnvBaseSpec
  parent types: ContainerSpec, DCCustomParams, DCLifecycleNewPod
  properties:
    name:                 EnvString
    value:                String

```
## PodVolumeConfigMapSpec

```
PodVolumeConfigMapSpec (abstract type):
  parents: PodVolumeItemMapper, PodVolumeBaseSpec
  parent types: PodTemplateSpec
  properties:
    defaultMode:          Nullable<Positive<Integer>>
    item_map:             Nullable<Map<String, String>>
    map_name:             Identifier
    name:                 Identifier

```
## MatchExpression

```
MatchExpression (abstract type):
  parent types: MatchExpressionsSelector
  properties:
    key:                  NonEmpty<String>
    operator:             Enum(u'In', u'NotIn', u'Exists', u'DoesNotExist')
    values:               Nullable<List<String>>

```
## SCCSELinux

```
SCCSELinux (abstract type):
  parent types: SecurityContextConstraints
  properties:
    level:                Nullable<String>
    role:                 Nullable<String>
    strategy:             Nullable<Enum(u'MustRunAs', u'RunAsAny')>
    type:                 Nullable<String>
    user:                 Nullable<String>

```
## ClusterRoleBinding

```
ClusterRoleBinding (abstract type):
  parents: RoleBindingBase, RoleBindingXF
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
   *roleRef:              RoleRef
   *subjects:             NonEmpty<List<RoleSubject>>

```
## AWSLoadBalancerService

```
AWSLoadBalancerService (abstract type):
  parents: Service
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    aws-load-balancer-backend-protocol: Nullable<Identifier>
    aws-load-balancer-ssl-cert: Nullable<ARN>
    externalTrafficPolicy: Nullable<Enum(u'Cluster', u'Local')>
   *ports:                NonEmpty<List<ServicePort>>
   *selector:             NonEmpty<Map<String, String>>
    sessionAffinity:      Nullable<Enum(u'ClientIP', u'None')>

```
## Job

```
Job (abstract type):
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    activeDeadlineSeconds: Nullable<Positive<Integer>>
    completions:          Nullable<Positive<NonZero<Integer>>>
    manualSelector:       Nullable<Boolean>
    parallelism:          Nullable<Positive<NonZero<Integer>>>
    pod_template:         PodTemplateSpec
    selector:             Nullable<BaseSelector>

```
## RouteDestService

```
RouteDestService (abstract type):
  parents: RouteDest
  parent types: Route
  properties:
    name:                 Identifier
    weight:               Positive<NonZero<Integer>>

```
## DCRecreateStrategy

```
DCRecreateStrategy (abstract type):
  parents: DCBaseUpdateStrategy
  parent types: DeploymentConfig
  properties:
    activeDeadlineSeconds: Nullable<Positive<NonZero<Integer>>>
    annotations:          Map<String, String>
    customParams:         Nullable<DCCustomParams>
    labels:               Map<String, String>
    recreateParams:       Nullable<DCRecreateParams>
    resources:            Nullable<ContainerResourceSpec>

```
## DplRollingUpdateStrategy

```
DplRollingUpdateStrategy (abstract type):
  parents: DplBaseUpdateStrategy
  parent types: Deployment
  properties:
    maxSurge:             SurgeSpec
    maxUnavailable:       SurgeSpec

```
## ContainerSpec

```
ContainerSpec (abstract type):
  parents: EnvironmentPreProcessMixin
  parent types: PodTemplateSpec
  properties:
    name (identifier):    Identifier
    args:                 Nullable<List<String>>
    command:              Nullable<List<String>>
   *env:                  Nullable<List<ContainerEnvBaseSpec>>
    image:                NonEmpty<String>
    imagePullPolicy:      Nullable<Enum(u'Always', u'IfNotPresent')>
    kind:                 Nullable<Enum(u'DockerImage')>
    lifecycle:            Nullable<LifeCycle>
    livenessProbe:        Nullable<ContainerProbeBaseSpec>
   *ports:                Nullable<List<ContainerPort>>
    readinessProbe:       Nullable<ContainerProbeBaseSpec>
    resources:            Nullable<ContainerResourceSpec>
    securityContext:      Nullable<SecurityContext>
    terminationMessagePath: Nullable<NonEmpty<Path>>
   *volumeMounts:         Nullable<List<ContainerVolumeMountSpec>>

```
## DplRecreateStrategy

```
DplRecreateStrategy (abstract type):
  parents: DplBaseUpdateStrategy
  parent types: Deployment
  properties:

```
## DCTrigger

```
DCTrigger:
  children: DCConfigChangeTrigger, DCImageChangeTrigger
  parent types: DeploymentConfig
  properties:

```
## ContainerEnvSecretSpec

```
ContainerEnvSecretSpec (abstract type):
  parents: ContainerEnvBaseSpec
  parent types: ContainerSpec, DCCustomParams, DCLifecycleNewPod
  properties:
    key:                  NonEmpty<String>
    name:                 EnvString
    secret_name:          Identifier

```
## MatchExpressionsSelector

```
MatchExpressionsSelector (abstract type):
  parents: BaseSelector
  parent types: DaemonSet, Deployment, Job, PersistentVolumeClaim
  properties:
    matchExpressions:     NonEmpty<List<MatchExpression>>

```
## ContainerProbeBaseSpec

```
ContainerProbeBaseSpec:
  children: ContainerProbeTCPPortSpec, ContainerProbeHTTPSpec
  parent types: ContainerSpec
  properties:
    failureThreshold:     Nullable<Positive<NonZero<Integer>>>
    initialDelaySeconds:  Nullable<Positive<Integer>>
    periodSeconds:        Nullable<Positive<NonZero<Integer>>>
    successThreshold:     Nullable<Positive<NonZero<Integer>>>
    timeoutSeconds:       Nullable<Positive<NonZero<Integer>>>

```
## PodVolumeEmptyDirSpec

```
PodVolumeEmptyDirSpec (abstract type):
  parents: PodVolumeBaseSpec
  parent types: PodTemplateSpec
  properties:
    name:                 Identifier

```
## PolicyBinding

```
PolicyBinding (abstract type):
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    ColonIdentifier
   *roleBindings:         List<PolicyBindingRoleBinding>

```
## ConfigMap

```
ConfigMap (abstract type):
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    files:                Map<String, String>

```
## SCCGroups

```
SCCGroups (abstract type):
  parent types: SecurityContextConstraints
  properties:
    ranges:               Nullable<List<SCCGroupRange>>
    type:                 Nullable<Enum(u'MustRunAs', u'RunAsAny')>

```
## DCCustomStrategy

```
DCCustomStrategy (abstract type):
  parents: DCBaseUpdateStrategy
  parent types: DeploymentConfig
  properties:
    activeDeadlineSeconds: Nullable<Positive<NonZero<Integer>>>
    annotations:          Map<String, String>
    customParams:         DCCustomParams
    labels:               Map<String, String>
    resources:            Nullable<ContainerResourceSpec>

```
## ContainerResourceEachSpec

```
ContainerResourceEachSpec (abstract type):
  parent types: ContainerResourceSpec
  properties:
   *cpu:                  Nullable<Positive<NonZero<Number>>>
    memory:               Nullable<Memory>

```
## StorageClass

```
StorageClass (abstract type):
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    parameters:           Map<String, String>
    provisioner:          String

```
## DCRollingParams

```
DCRollingParams (abstract type):
  parent types: DCRollingStrategy
  properties:
    intervalSeconds:      Nullable<Positive<NonZero<Integer>>>
    maxSurge:             SurgeSpec
    maxUnavailable:       SurgeSpec
    post:                 Nullable<DCLifecycleHook>
    pre:                  Nullable<DCLifecycleHook>
    timeoutSeconds:       Nullable<Positive<NonZero<Integer>>>
    updatePeriodSeconds:  Nullable<Positive<NonZero<Integer>>>

```
## SCCGroupRange

```
SCCGroupRange (abstract type):
  parent types: SCCGroups
  properties:
    max:                  Positive<NonZero<Integer>>
    min:                  Positive<NonZero<Integer>>

```
## DCCustomParams

```
DCCustomParams (abstract type):
  parents: EnvironmentPreProcessMixin
  parent types: DCCustomStrategy, DCRecreateStrategy, DCRollingStrategy
  properties:
    command:              Nullable<List<String>>
   *environment:          Nullable<List<ContainerEnvBaseSpec>>
    image:                NonEmpty<String>

```
## ContainerVolumeMountSpec

```
ContainerVolumeMountSpec (abstract type):
  parent types: ContainerSpec, DCLifecycleNewPod
  properties:
    name:                 Identifier
    path:                 NonEmpty<Path>
    readOnly:             Nullable<Boolean>

```
## LifeCycleProbe

```
LifeCycleProbe:
  children: LifeCycleExec, LifeCycleHTTP
  parent types: LifeCycle
  properties:

```
## SASecretSubject

```
SASecretSubject (abstract type):
  parent types: ServiceAccount
  properties:
    kind:                 Nullable<CaseIdentifier>
    name:                 Nullable<Identifier>
    ns:                   Nullable<Identifier>

```
## PodTemplateSpec

```
PodTemplateSpec (abstract type):
  parent types: DaemonSet, Deployment, DeploymentConfig, Job, ReplicationController
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    containers:           NonEmpty<List<ContainerSpec>>
    dnsPolicy:            Nullable<Enum(u'ClusterFirst')>
    hostIPC:              Nullable<Boolean>
    hostNetwork:          Nullable<Boolean>
    hostPID:              Nullable<Boolean>
   *imagePullSecrets:     Nullable<List<PodImagePullSecret>>
    name:                 Nullable<Identifier>
    nodeSelector:         Nullable<Map<String, String>>
    restartPolicy:        Nullable<Enum(u'Always', u'OnFailure', u'Never')>
    securityContext:      Nullable<SecurityContext>
   *serviceAccountName:   Nullable<Identifier>
      (serviceAccount)
    terminationGracePeriodSeconds: Nullable<Positive<Integer>>
    volumes:              Nullable<List<PodVolumeBaseSpec>>

```
## User

```
User (abstract type):
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    UserIdentifier
    fullName:             Nullable<String>
    identities:           NonEmpty<List<NonEmpty<String>>>

```
## ContainerEnvConfigMapSpec

```
ContainerEnvConfigMapSpec (abstract type):
  parents: ContainerEnvBaseSpec
  parent types: ContainerSpec, DCCustomParams, DCLifecycleNewPod
  properties:
    key:                  NonEmpty<String>
    map_name:             Identifier
    name:                 EnvString

```
## LifeCycleExec

```
LifeCycleExec (abstract type):
  parents: LifeCycleProbe
  parent types: LifeCycle
  properties:
    command:              NonEmpty<List<String>>

```
## DCRollingStrategy

```
DCRollingStrategy (abstract type):
  parents: DCBaseUpdateStrategy
  parent types: DeploymentConfig
  properties:
    activeDeadlineSeconds: Nullable<Positive<NonZero<Integer>>>
    annotations:          Map<String, String>
    customParams:         Nullable<DCCustomParams>
    labels:               Map<String, String>
    resources:            Nullable<ContainerResourceSpec>
    rollingParams:        Nullable<DCRollingParams>

```
## RouteDest

```
RouteDest:
  children: RouteDestService
  parent types: Route
  properties:
    weight:               Positive<NonZero<Integer>>

```
## ContainerEnvPodFieldSpec

```
ContainerEnvPodFieldSpec (abstract type):
  parents: ContainerEnvBaseSpec
  parent types: ContainerSpec, DCCustomParams, DCLifecycleNewPod
  properties:
    apiVersion:           Nullable<Enum(u'v1')>
    fieldPath:            Enum(u'metadata.name', u'metadata.namespace', u'metadata.labels', u'metadata.annotations', u'spec.nodeName', u'spec.serviceAccountName', u'status.podIP')
    name:                 EnvString

```
## ServiceAccount

```
ServiceAccount (abstract type):
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
   *imagePullSecrets:     Nullable<List<SAImgPullSecretSubject>>
   *secrets:              Nullable<List<SASecretSubject>>

```
## PodVolumeBaseSpec

```
PodVolumeBaseSpec:
  children: PodVolumeHostSpec, PodVolumeItemMapper, PodVolumePVCSpec, PodVolumeEmptyDirSpec, PodVolumeConfigMapSpec, PodVolumeSecretSpec
  parent types: PodTemplateSpec
  properties:
    name:                 Identifier

```
## ClusterRole

```
ClusterRole (abstract type):
  parents: RoleBase
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    rules:                NonEmpty<List<PolicyRule>>

```
## DCLifecycleHook

```
DCLifecycleHook (abstract type):
  parent types: DCRecreateParams, DCRollingParams
  properties:
    execNewPod:           Nullable<DCLifecycleNewPod>
    failurePolicy:        Enum(u'Abort', u'Retry', u'Ignore')
    tagImages:            Nullable<DCTagImages>

```
## ClusterIPService

```
ClusterIPService (abstract type):
  parents: Service
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    clusterIP:            Nullable<IPv4>
   *ports:                NonEmpty<List<ServicePort>>
   *selector:             NonEmpty<Map<String, String>>
    sessionAffinity:      Nullable<Enum(u'ClientIP', u'None')>

```
## PersistentVolumeRef

```
PersistentVolumeRef (abstract type):
  parent types: PersistentVolume
  properties:
    apiVersion:           Nullable<String>
    kind:                 Nullable<CaseIdentifier>
    name:                 Nullable<Identifier>
    ns:                   Nullable<Identifier>

```
## DCLifecycleNewPod

```
DCLifecycleNewPod (abstract type):
  parents: EnvironmentPreProcessMixin
  parent types: DCLifecycleHook
  properties:
    command:              NonEmpty<List<String>>
    containerName:        Identifier
   *env:                  Nullable<List<ContainerEnvBaseSpec>>
    volumeMounts:         Nullable<List<ContainerVolumeMountSpec>>
    volumes:              Nullable<List<Identifier>>

```
## ContainerProbeTCPPortSpec

```
ContainerProbeTCPPortSpec (abstract type):
  parents: ContainerProbeBaseSpec
  parent types: ContainerSpec
  properties:
    failureThreshold:     Nullable<Positive<NonZero<Integer>>>
    initialDelaySeconds:  Nullable<Positive<Integer>>
    periodSeconds:        Nullable<Positive<NonZero<Integer>>>
   *port:                 Positive<NonZero<Integer>>
    successThreshold:     Nullable<Positive<NonZero<Integer>>>
    timeoutSeconds:       Nullable<Positive<NonZero<Integer>>>

```
## ContainerEnvBaseSpec

```
ContainerEnvBaseSpec:
  children: ContainerEnvSpec, ContainerEnvConfigMapSpec, ContainerEnvSecretSpec, ContainerEnvPodFieldSpec, ContainerEnvContainerResourceSpec
  parent types: ContainerSpec, DCCustomParams, DCLifecycleNewPod
  properties:
    name:                 EnvString

```
## PodVolumeHostSpec

```
PodVolumeHostSpec (abstract type):
  parents: PodVolumeBaseSpec
  parent types: PodTemplateSpec
  properties:
    name:                 Identifier
    path:                 String

```
## DCRecreateParams

```
DCRecreateParams (abstract type):
  parent types: DCRecreateStrategy
  properties:
    mid:                  Nullable<DCLifecycleHook>
    post:                 Nullable<DCLifecycleHook>
    pre:                  Nullable<DCLifecycleHook>
    timeoutSeconds:       Nullable<Positive<NonZero<Integer>>>

```
## DCTagImages

```
DCTagImages (abstract type):
  parent types: DCLifecycleHook
  properties:
    containerName:        Identifier
    toApiVersion:         Nullable<String>
    toFieldPath:          Nullable<String>
    toKind:               Nullable<Enum(u'Deployment', u'DeploymentConfig', u'ImageStreamTag')>
    toName:               Nullable<Identifier>
    toNamespace:          Nullable<Identifier>
    toResourceVersion:    Nullable<String>
    toUid:                Nullable<String>

```
## Secret

```
Secret (abstract type):
  children: DockerCredentials, TLSCredentials
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    secrets:              Map<String, String>
    type:                 NonEmpty<String>

```
## RouteDestPort

```
RouteDestPort (abstract type):
  parent types: Route
  properties:
    targetPort:           Identifier

```
## BaseSelector

```
BaseSelector:
  children: MatchLabelsSelector, MatchExpressionsSelector
  parent types: DaemonSet, Deployment, Job, PersistentVolumeClaim
  properties:

```
## ContainerProbeHTTPSpec

```
ContainerProbeHTTPSpec (abstract type):
  parents: ContainerProbeBaseSpec
  parent types: ContainerSpec
  properties:
    failureThreshold:     Nullable<Positive<NonZero<Integer>>>
    host:                 Nullable<Domain>
    initialDelaySeconds:  Nullable<Positive<Integer>>
    path:                 NonEmpty<Path>
    periodSeconds:        Nullable<Positive<NonZero<Integer>>>
   *port:                 Positive<NonZero<Integer>>
    scheme:               Nullable<Enum(u'HTTP', u'HTTPS')>
    successThreshold:     Nullable<Positive<NonZero<Integer>>>
    timeoutSeconds:       Nullable<Positive<NonZero<Integer>>>

```
## ServicePort

```
ServicePort (abstract type):
  parent types: AWSLoadBalancerService, ClusterIPService, Service
  properties:
    name:                 Nullable<Identifier>
    port:                 Positive<NonZero<Integer>>
    protocol:             Enum(u'TCP', u'UDP')
    targetPort:           OneOf<Positive<NonZero<Integer>>, Identifier>

```
## AWSElasticBlockStore

```
AWSElasticBlockStore (abstract type):
  parent types: PersistentVolume
  properties:
    fsType:               Enum(u'ext4')
    volumeID:             AWSVolID

```
## ReplicationController

```
ReplicationController (abstract type):
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    minReadySeconds:      Nullable<Positive<NonZero<Integer>>>
    pod_template:         PodTemplateSpec
    replicas:             Positive<NonZero<Integer>>
    selector:             Nullable<Map<String, String>>

```
## SAImgPullSecretSubject

```
SAImgPullSecretSubject (abstract type):
  parent types: ServiceAccount
  properties:
    name:                 Identifier

```
## Deployment

```
Deployment (abstract type):
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    minReadySeconds:      Nullable<Positive<NonZero<Integer>>>
    paused:               Nullable<Boolean>
    pod_template:         PodTemplateSpec
    progressDeadlineSeconds: Nullable<Positive<NonZero<Integer>>>
    replicas:             Positive<NonZero<Integer>>
    revisionHistoryLimit: Nullable<Positive<NonZero<Integer>>>
    selector:             Nullable<BaseSelector>
    strategy:             Nullable<DplBaseUpdateStrategy>

```
## PodImagePullSecret

```
PodImagePullSecret (abstract type):
  parent types: PodTemplateSpec
  properties:
    name:                 Identifier

```
## RoleSubject

```
RoleSubject (abstract type):
  parent types: ClusterRoleBinding, PolicyBindingRoleBinding, RoleBinding, RoleBindingBase
  properties:
    kind:                 CaseIdentifier
    name:                 String
    ns:                   Nullable<Identifier>

```
## SecurityContextConstraints

```
SecurityContextConstraints (abstract type):
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    allowHostDirVolumePlugin: Boolean
    allowHostIPC:         Boolean
    allowHostNetwork:     Boolean
    allowHostPID:         Boolean
    allowHostPorts:       Boolean
    allowPrivilegedContainer: Boolean
    allowedCapabilities:  Nullable<List<String>>
    defaultAddCapabilities: Nullable<List<String>>
    fsGroup:              Nullable<SCCGroups>
    groups:               List<SystemIdentifier>
    priority:             Nullable<Positive<Integer>>
    readOnlyRootFilesystem: Boolean
    requiredDropCapabilities: Nullable<List<String>>
    runAsUser:            Nullable<SCCRunAsUser>
    seLinuxContext:       Nullable<SCCSELinux>
    seccompProfiles:      Nullable<List<String>>
    supplementalGroups:   Nullable<SCCGroups>
    users:                List<SystemIdentifier>
    volumes:              List<Enum(u'configMap', u'downwardAPI', u'emptyDir', u'hostPath', u'nfs', u'persistentVolumeClaim', u'secret', u'*')>

```
## Route

```
Route (abstract type):
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    host:                 Domain
    port:                 RouteDestPort
    tls:                  Nullable<RouteTLS>
    to:                   NonEmpty<List<RouteDest>>
    wildcardPolicy:       Enum(u'Subdomain', u'None')

```
## ContainerResourceSpec

```
ContainerResourceSpec (abstract type):
  parent types: ContainerSpec, DCBaseUpdateStrategy, DCCustomStrategy, DCRecreateStrategy, DCRollingStrategy
  properties:
    limits:               ContainerResourceEachSpec
    requests:             ContainerResourceEachSpec

```
## PolicyBindingRoleBinding

```
PolicyBindingRoleBinding (abstract type):
  parents: RoleBindingXF
  parent types: PolicyBinding
  properties:
    metadata:             Nullable<Map<String, String>>
    name:                 SystemIdentifier
    ns:                   Identifier
   *roleRef:              RoleRef
   *subjects:             NonEmpty<List<RoleSubject>>

```
## LifeCycle

```
LifeCycle (abstract type):
  parent types: ContainerSpec
  properties:
    postStart:            Nullable<LifeCycleProbe>
    preStop:              Nullable<LifeCycleProbe>

```
## RoleBinding

```
RoleBinding (abstract type):
  parents: RoleBindingBase, RoleBindingXF
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    SystemIdentifier
   *roleRef:              RoleRef
   *subjects:             NonEmpty<List<RoleSubject>>

```
## MatchLabelsSelector

```
MatchLabelsSelector (abstract type):
  parents: BaseSelector
  parent types: DaemonSet, Deployment, Job, PersistentVolumeClaim
  properties:
    matchLabels:          Map<String, String>

```
## PolicyRule

```
PolicyRule (abstract type):
  parent types: ClusterRole, Role, RoleBase
  properties:
    apiGroups:            NonEmpty<List<String>>
    attributeRestrictions: Nullable<String>
    nonResourceURLs:      Nullable<List<String>>
    resourceNames:        Nullable<List<String>>
    resources:            NonEmpty<List<NonEmpty<String>>>
    verbs:                NonEmpty<List<Enum(u'get', u'list', u'create', u'update', u'delete', u'deletecollection', u'watch')>>

```
## ContainerEnvContainerResourceSpec

```
ContainerEnvContainerResourceSpec (abstract type):
  parents: ContainerEnvBaseSpec
  parent types: ContainerSpec, DCCustomParams, DCLifecycleNewPod
  properties:
    containerName:        Nullable<Identifier>
    divisor:              Nullable<NonEmpty<String>>
    name:                 EnvString
    resource:             Enum(u'limits.cpu', u'limits.memory', u'requests.cpu', u'requests.memory')

```
## PodVolumeSecretSpec

```
PodVolumeSecretSpec (abstract type):
  parents: PodVolumeItemMapper, PodVolumeBaseSpec
  parent types: PodTemplateSpec
  properties:
    defaultMode:          Nullable<Positive<Integer>>
    item_map:             Nullable<Map<String, String>>
    name:                 Identifier
    secret_name:          Identifier

```
