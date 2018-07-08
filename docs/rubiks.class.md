# Rubiks Object Index

This document is automatically generated using the command `docgen` and describe all the object and types that can be used inside Rubiks to configure your cluster


# Table of contents

- [Formats](#formats)
  - [Base64](#base64)
  - [Command](#command)
  - [Confidential](#confidential)
  - [JSON](#json)
  - [YAML](#yaml)
- [Types](#types)
  - [ARN](#arn)
  - [Boolean](#boolean)
  - [CaseIdentifier](#caseidentifier)
  - [ColonIdentifier](#colonidentifier)
  - [Domain](#domain)
  - [Enum](#enum)
  - [IP](#ip)
  - [IPv4](#ipv4)
  - [Identifier](#identifier)
  - [Integer](#integer)
  - [Number](#number)
  - [Path](#path)
  - [String](#string)
  - [SurgeSpec](#surgespec)
  - [SystemIdentifier](#systemidentifier)
- [Objects](#objects)
  - [AWSElasticBlockStore](#awselasticblockstore)
  - [AWSLoadBalancerService](#awsloadbalancerservice)
  - [BaseSelector](#baseselector)
  - [ClusterIPService](#clusteripservice)
  - [ClusterRole](#clusterrole)
  - [ClusterRoleBinding](#clusterrolebinding)
  - [ConfigMap](#configmap)
  - [ContainerEnvBaseSpec](#containerenvbasespec)
  - [ContainerEnvConfigMapSpec](#containerenvconfigmapspec)
  - [ContainerEnvContainerResourceSpec](#containerenvcontainerresourcespec)
  - [ContainerEnvPodFieldSpec](#containerenvpodfieldspec)
  - [ContainerEnvSecretSpec](#containerenvsecretspec)
  - [ContainerEnvSpec](#containerenvspec)
  - [ContainerPort](#containerport)
  - [ContainerProbeBaseSpec](#containerprobebasespec)
  - [ContainerProbeHTTPSpec](#containerprobehttpspec)
  - [ContainerProbeTCPPortSpec](#containerprobetcpportspec)
  - [ContainerResourceEachSpec](#containerresourceeachspec)
  - [ContainerResourceSpec](#containerresourcespec)
  - [ContainerSpec](#containerspec)
  - [ContainerVolumeMountSpec](#containervolumemountspec)
  - [DCBaseUpdateStrategy](#dcbaseupdatestrategy)
  - [DCConfigChangeTrigger](#dcconfigchangetrigger)
  - [DCCustomParams](#dccustomparams)
  - [DCCustomStrategy](#dccustomstrategy)
  - [DCImageChangeTrigger](#dcimagechangetrigger)
  - [DCLifecycleHook](#dclifecyclehook)
  - [DCLifecycleNewPod](#dclifecyclenewpod)
  - [DCRecreateParams](#dcrecreateparams)
  - [DCRecreateStrategy](#dcrecreatestrategy)
  - [DCRollingParams](#dcrollingparams)
  - [DCRollingStrategy](#dcrollingstrategy)
  - [DCTagImages](#dctagimages)
  - [DCTrigger](#dctrigger)
  - [DaemonSet](#daemonset)
  - [Deployment](#deployment)
  - [DeploymentConfig](#deploymentconfig)
  - [DockerCredentials](#dockercredentials)
  - [DplBaseUpdateStrategy](#dplbaseupdatestrategy)
  - [DplRecreateStrategy](#dplrecreatestrategy)
  - [DplRollingUpdateStrategy](#dplrollingupdatestrategy)
  - [Group](#group)
  - [Job](#job)
  - [LifeCycle](#lifecycle)
  - [LifeCycleExec](#lifecycleexec)
  - [LifeCycleHTTP](#lifecyclehttp)
  - [LifeCycleProbe](#lifecycleprobe)
  - [MatchExpression](#matchexpression)
  - [MatchExpressionsSelector](#matchexpressionsselector)
  - [MatchLabelsSelector](#matchlabelsselector)
  - [Namespace](#namespace)
  - [PersistentVolume](#persistentvolume)
  - [PersistentVolumeClaim](#persistentvolumeclaim)
  - [PersistentVolumeRef](#persistentvolumeref)
  - [PodImagePullSecret](#podimagepullsecret)
  - [PodTemplateSpec](#podtemplatespec)
  - [PodVolumeBaseSpec](#podvolumebasespec)
  - [PodVolumeConfigMapSpec](#podvolumeconfigmapspec)
  - [PodVolumeEmptyDirSpec](#podvolumeemptydirspec)
  - [PodVolumeHostSpec](#podvolumehostspec)
  - [PodVolumeItemMapper](#podvolumeitemmapper)
  - [PodVolumePVCSpec](#podvolumepvcspec)
  - [PodVolumeSecretSpec](#podvolumesecretspec)
  - [PolicyBinding](#policybinding)
  - [PolicyBindingRoleBinding](#policybindingrolebinding)
  - [PolicyRule](#policyrule)
  - [Project](#project)
  - [ReplicationController](#replicationcontroller)
  - [Role](#role)
  - [RoleBinding](#rolebinding)
  - [RoleRef](#roleref)
  - [RoleSubject](#rolesubject)
  - [Route](#route)
  - [RouteDest](#routedest)
  - [RouteDestPort](#routedestport)
  - [RouteDestService](#routedestservice)
  - [RouteTLS](#routetls)
  - [SAImgPullSecretSubject](#saimgpullsecretsubject)
  - [SASecretSubject](#sasecretsubject)
  - [SCCGroupRange](#sccgrouprange)
  - [SCCGroups](#sccgroups)
  - [SCCRunAsUser](#sccrunasuser)
  - [SCCSELinux](#sccselinux)
  - [Secret](#secret)
  - [SecurityContext](#securitycontext)
  - [SecurityContextConstraints](#securitycontextconstraints)
  - [Service](#service)
  - [ServiceAccount](#serviceaccount)
  - [ServicePort](#serviceport)
  - [StorageClass](#storageclass)
  - [TLSCredentials](#tlscredentials)
  - [User](#user)

# Formats

## Base64

TODO: Description is still missing from the class docstring.
Stay tuned to have more hint about this variable.

## Command

TODO: Description is still missing from the class docstring.
Stay tuned to have more hint about this variable.

## Confidential

TODO: Description is still missing from the class docstring.
Stay tuned to have more hint about this variable.

## JSON

TODO: Description is still missing from the class docstring.
Stay tuned to have more hint about this variable.

## YAML

TODO: Description is still missing from the class docstring.
Stay tuned to have more hint about this variable.


# Types

## ARN


Amazon Resource Names (ARNs) uniquely identify AWS resources.

The following are the general formats for ARNs; the specific components and values used depend on the AWS service.

```
arn:partition:service:region:account-id:resource
arn:partition:service:region:account-id:resourcetype/resource
arn:partition:service:region:account-id:resourcetype:resource
```

**partition**

The partition that the resource is in. For standard AWS regions, the partition is aws. If you have resources in other partitions, the partition is aws-partitionname. For example, the partition for resources in the China (Beijing) region is aws-cn.

**service**

The service namespace that identifies the AWS product (for example, Amazon S3, IAM, or Amazon RDS). For a list of namespaces, see AWS Service Namespaces.

**region**

The region the resource resides in. Note that the ARNs for some resources do not require a region, so this component might be omitted.

**account**

The ID of the AWS account that owns the resource, without the hyphens. For example, 123456789012. Note that the ARNs for some resources don't require an account number, so this component might be omitted.

**resource, resourcetype:resource, or resourcetype/resource**

The content of this part of the ARN varies by service. It often includes an indicator of the type of resource—for example, an IAM user or Amazon RDS database —followed by a slash (/) or a colon (:), followed by the resource name itself. Some services allow paths for resource names, as described in Paths in ARNs.


## Boolean


Boolean, or boolean logic, is a subset of algebra used for creating true/false statements.
Boolean expressions use the operators AND, OR, XOR, and NOT to compare values and return a true or false result.


## CaseIdentifier

TODO: Description is still missing from the class docstring.
Stay tuned to have more hint about this variable.

## ColonIdentifier

TODO: Description is still missing from the class docstring.
Stay tuned to have more hint about this variable.

## Domain

TODO: Description is still missing from the class docstring.
Stay tuned to have more hint about this variable.

## Enum


Enum, short for "enumerated," is a data type that consists of predefined values. A constant or variable defined as an enum can store one of the values listed in the enum declaration.

**Example**

`Enum('Value1', 'Value2', 'Value3')`


## IP

TODO: Description is still missing from the class docstring.
Stay tuned to have more hint about this variable.

## IPv4

TODO: Description is still missing from the class docstring.
Stay tuned to have more hint about this variable.

## Identifier

TODO: Description is still missing from the class docstring.
Stay tuned to have more hint about this variable.

## Integer


An integer is a whole number (not a fraction) that can be positive, negative, or zero.
Therefore, the numbers 10, 0, -25, and 5,148 are all integers. Unlike floating point numbers, integers cannot have decimal places.


## Number


An integer is a whole number (not a fraction) that can be positive, negative, floating or zero.


## Path

TODO: Description is still missing from the class docstring.
Stay tuned to have more hint about this variable.

## String

TODO: Description is still missing from the class docstring.
Stay tuned to have more hint about this variable.

## SurgeSpec

TODO: Description is still missing from the class docstring.
Stay tuned to have more hint about this variable.

## SystemIdentifier

TODO: Description is still missing from the class docstring.
Stay tuned to have more hint about this variable.


# Objects

## AWSElasticBlockStore
###  Parent types: 
- [PersistentVolume](#persistentvolume)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
fsType | [Enum](#enum)('ext4') | False | - | - 
volumeID | [AWSVolID](#awsvolid) | False | - | - 
## AWSLoadBalancerService
### Parents: 
- [Service](#service)
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
aws-load-balancer-backend-protocol | [Nullable](#nullable)&lt;[Identifier](#identifier)&gt; | False | - | - 
aws-load-balancer-ssl-cert | [Nullable](#nullable)&lt;[ARN](#arn)&gt; | False | - | - 
externalTrafficPolicy | [Nullable](#nullable)&lt;[Enum](#enum)('Cluster', 'Local')&gt; | False | - | - 
ports | [NonEmpty](#nonempty)&lt;[List](#list)&lt;[ServicePort](#serviceport)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
selector | [NonEmpty](#nonempty)&lt;[Map](#map)&lt;[String](#string), [String](#string)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
sessionAffinity | [Nullable](#nullable)&lt;[Enum](#enum)('ClientIP', 'None')&gt; | False | - | - 
## BaseSelector
###  Children: 
- [MatchLabelsSelector](#matchlabelsselector)
- [MatchExpressionsSelector](#matchexpressionsselector)
###  Parent types: 
- [DaemonSet](#daemonset)
- [Deployment](#deployment)
- [Job](#job)
- [PersistentVolumeClaim](#persistentvolumeclaim)
## ClusterIPService
### Parents: 
- [Service](#service)
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
clusterIP | [Nullable](#nullable)&lt;[IPv4](#ipv4)&gt; | False | - | - 
ports | [NonEmpty](#nonempty)&lt;[List](#list)&lt;[ServicePort](#serviceport)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
selector | [NonEmpty](#nonempty)&lt;[Map](#map)&lt;[String](#string), [String](#string)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
sessionAffinity | [Nullable](#nullable)&lt;[Enum](#enum)('ClientIP', 'None')&gt; | False | - | - 
## ClusterRole
### Parents: 
- [RoleBase](#rolebase)
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
rules | [NonEmpty](#nonempty)&lt;[List](#list)&lt;[PolicyRule](#policyrule)&gt;&gt; | False | - | - 
## ClusterRoleBinding
### Parents: 
- [RoleBindingBase](#rolebindingbase)
- [RoleBindingXF](#rolebindingxf)
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
roleRef | [RoleRef](#roleref) | False | &lt;unknown transformation&gt; | - 
subjects | [NonEmpty](#nonempty)&lt;[List](#list)&lt;[RoleSubject](#rolesubject)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
## ConfigMap
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
files | [Map](#map)&lt;[String](#string), [String](#string)&gt; | False | - | - 
## ContainerEnvBaseSpec
###  Children: 
- [ContainerEnvSpec](#containerenvspec)
- [ContainerEnvConfigMapSpec](#containerenvconfigmapspec)
- [ContainerEnvSecretSpec](#containerenvsecretspec)
- [ContainerEnvPodFieldSpec](#containerenvpodfieldspec)
- [ContainerEnvContainerResourceSpec](#containerenvcontainerresourcespec)
###  Parent types: 
- [ContainerSpec](#containerspec)
- [DCCustomParams](#dccustomparams)
- [DCLifecycleNewPod](#dclifecyclenewpod)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [EnvString](#envstring) | False | - | - 
## ContainerEnvConfigMapSpec
### Parents: 
- [ContainerEnvBaseSpec](#containerenvbasespec)
###  Parent types: 
- [ContainerSpec](#containerspec)
- [DCCustomParams](#dccustomparams)
- [DCLifecycleNewPod](#dclifecyclenewpod)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
key | [NonEmpty](#nonempty)&lt;[String](#string)&gt; | False | - | - 
map_name | [Identifier](#identifier) | False | - | - 
name | [EnvString](#envstring) | False | - | - 
## ContainerEnvContainerResourceSpec
### Parents: 
- [ContainerEnvBaseSpec](#containerenvbasespec)
###  Parent types: 
- [ContainerSpec](#containerspec)
- [DCCustomParams](#dccustomparams)
- [DCLifecycleNewPod](#dclifecyclenewpod)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
containerName | [Nullable](#nullable)&lt;[Identifier](#identifier)&gt; | False | - | - 
divisor | [Nullable](#nullable)&lt;[NonEmpty](#nonempty)&lt;[String](#string)&gt;&gt; | False | - | - 
name | [EnvString](#envstring) | False | - | - 
resource | [Enum](#enum)('limits.cpu', 'limits.memory', 'requests.cpu', 'requests.memory') | False | - | - 
## ContainerEnvPodFieldSpec
### Parents: 
- [ContainerEnvBaseSpec](#containerenvbasespec)
###  Parent types: 
- [ContainerSpec](#containerspec)
- [DCCustomParams](#dccustomparams)
- [DCLifecycleNewPod](#dclifecyclenewpod)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
apiVersion | [Nullable](#nullable)&lt;[Enum](#enum)('v1')&gt; | False | - | - 
fieldPath | [Enum](#enum)('metadata.name', 'metadata.namespace', 'metadata.labels', 'metadata.annotations', 'spec.nodeName', 'spec.serviceAccountName', 'status.podIP') | False | - | - 
name | [EnvString](#envstring) | False | - | - 
## ContainerEnvSecretSpec
### Parents: 
- [ContainerEnvBaseSpec](#containerenvbasespec)
###  Parent types: 
- [ContainerSpec](#containerspec)
- [DCCustomParams](#dccustomparams)
- [DCLifecycleNewPod](#dclifecyclenewpod)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
key | [NonEmpty](#nonempty)&lt;[String](#string)&gt; | False | - | - 
name | [EnvString](#envstring) | False | - | - 
secret_name | [Identifier](#identifier) | False | - | - 
## ContainerEnvSpec
### Parents: 
- [ContainerEnvBaseSpec](#containerenvbasespec)
###  Parent types: 
- [ContainerSpec](#containerspec)
- [DCCustomParams](#dccustomparams)
- [DCLifecycleNewPod](#dclifecyclenewpod)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [EnvString](#envstring) | False | - | - 
value | [String](#string) | False | - | - 
## ContainerPort
###  Parent types: 
- [ContainerSpec](#containerspec)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
containerPort | [Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt; | False | - | - 
hostIP | [Nullable](#nullable)&lt;[IP](#ip)&gt; | False | - | - 
hostPort | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
name | [Nullable](#nullable)&lt;[String](#string)&gt; | False | - | - 
protocol | [Enum](#enum)('TCP', 'UDP') | False | - | - 
## ContainerProbeBaseSpec
###  Children: 
- [ContainerProbeTCPPortSpec](#containerprobetcpportspec)
- [ContainerProbeHTTPSpec](#containerprobehttpspec)
###  Parent types: 
- [ContainerSpec](#containerspec)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
failureThreshold | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
initialDelaySeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[Integer](#integer)&gt;&gt; | False | - | - 
periodSeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
successThreshold | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
timeoutSeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
## ContainerProbeHTTPSpec
### Parents: 
- [ContainerProbeBaseSpec](#containerprobebasespec)
###  Parent types: 
- [ContainerSpec](#containerspec)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
failureThreshold | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
host | [Nullable](#nullable)&lt;[Domain](#domain)&gt; | False | - | - 
initialDelaySeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[Integer](#integer)&gt;&gt; | False | - | - 
path | [NonEmpty](#nonempty)&lt;[Path](#path)&gt; | False | - | - 
periodSeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
port | [Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
scheme | [Nullable](#nullable)&lt;[Enum](#enum)('HTTP', 'HTTPS')&gt; | False | - | - 
successThreshold | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
timeoutSeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
## ContainerProbeTCPPortSpec
### Parents: 
- [ContainerProbeBaseSpec](#containerprobebasespec)
###  Parent types: 
- [ContainerSpec](#containerspec)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
failureThreshold | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
initialDelaySeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[Integer](#integer)&gt;&gt; | False | - | - 
periodSeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
port | [Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
successThreshold | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
timeoutSeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
## ContainerResourceEachSpec
###  Parent types: 
- [ContainerResourceSpec](#containerresourcespec)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
cpu | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Number](#number)&gt;&gt;&gt; | False | &lt;unknown transformation&gt; | - 
memory | [Nullable](#nullable)&lt;[Memory](#memory)&gt; | False | - | - 
## ContainerResourceSpec
###  Parent types: 
- [ContainerSpec](#containerspec)
- [DCBaseUpdateStrategy](#dcbaseupdatestrategy)
- [DCCustomStrategy](#dccustomstrategy)
- [DCRecreateStrategy](#dcrecreatestrategy)
- [DCRollingStrategy](#dcrollingstrategy)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
limits | [ContainerResourceEachSpec](#containerresourceeachspec) | False | - | - 
requests | [ContainerResourceEachSpec](#containerresourceeachspec) | False | - | - 
## ContainerSpec
### Parents: 
- [EnvironmentPreProcessMixin](#environmentpreprocessmixin)
###  Parent types: 
- [PodTemplateSpec](#podtemplatespec)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
args | [Nullable](#nullable)&lt;[List](#list)&lt;[String](#string)&gt;&gt; | False | - | - 
command | [Nullable](#nullable)&lt;[List](#list)&lt;[String](#string)&gt;&gt; | False | - | - 
env | [Nullable](#nullable)&lt;[List](#list)&lt;[ContainerEnvBaseSpec](#containerenvbasespec)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
image | [NonEmpty](#nonempty)&lt;[String](#string)&gt; | False | - | - 
imagePullPolicy | [Nullable](#nullable)&lt;[Enum](#enum)('Always', 'IfNotPresent')&gt; | False | - | - 
kind | [Nullable](#nullable)&lt;[Enum](#enum)('DockerImage')&gt; | False | - | - 
lifecycle | [Nullable](#nullable)&lt;[LifeCycle](#lifecycle)&gt; | False | - | - 
livenessProbe | [Nullable](#nullable)&lt;[ContainerProbeBaseSpec](#containerprobebasespec)&gt; | False | - | - 
ports | [Nullable](#nullable)&lt;[List](#list)&lt;[ContainerPort](#containerport)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
readinessProbe | [Nullable](#nullable)&lt;[ContainerProbeBaseSpec](#containerprobebasespec)&gt; | False | - | - 
resources | [Nullable](#nullable)&lt;[ContainerResourceSpec](#containerresourcespec)&gt; | False | - | - 
securityContext | [Nullable](#nullable)&lt;[SecurityContext](#securitycontext)&gt; | False | - | - 
terminationMessagePath | [Nullable](#nullable)&lt;[NonEmpty](#nonempty)&lt;[Path](#path)&gt;&gt; | False | - | - 
volumeMounts | [Nullable](#nullable)&lt;[List](#list)&lt;[ContainerVolumeMountSpec](#containervolumemountspec)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
## ContainerVolumeMountSpec
###  Parent types: 
- [ContainerSpec](#containerspec)
- [DCLifecycleNewPod](#dclifecyclenewpod)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | False | - | - 
path | [NonEmpty](#nonempty)&lt;[Path](#path)&gt; | False | - | - 
readOnly | [Nullable](#nullable)&lt;[Boolean](#boolean)&gt; | False | - | - 
## DCBaseUpdateStrategy
###  Children: 
- [DCRecreateStrategy](#dcrecreatestrategy)
- [DCRollingStrategy](#dcrollingstrategy)
- [DCCustomStrategy](#dccustomstrategy)
###  Parent types: 
- [DeploymentConfig](#deploymentconfig)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
activeDeadlineSeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
annotations | [Map](#map)&lt;[String](#string), [String](#string)&gt; | False | - | - 
labels | [Map](#map)&lt;[String](#string), [String](#string)&gt; | False | - | - 
resources | [Nullable](#nullable)&lt;[ContainerResourceSpec](#containerresourcespec)&gt; | False | - | - 
## DCConfigChangeTrigger
### Parents: 
- [DCTrigger](#dctrigger)
###  Parent types: 
- [DeploymentConfig](#deploymentconfig)
## DCCustomParams
### Parents: 
- [EnvironmentPreProcessMixin](#environmentpreprocessmixin)
###  Parent types: 
- [DCCustomStrategy](#dccustomstrategy)
- [DCRecreateStrategy](#dcrecreatestrategy)
- [DCRollingStrategy](#dcrollingstrategy)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
command | [Nullable](#nullable)&lt;[List](#list)&lt;[String](#string)&gt;&gt; | False | - | - 
environment | [Nullable](#nullable)&lt;[List](#list)&lt;[ContainerEnvBaseSpec](#containerenvbasespec)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
image | [NonEmpty](#nonempty)&lt;[String](#string)&gt; | False | - | - 
## DCCustomStrategy
### Parents: 
- [DCBaseUpdateStrategy](#dcbaseupdatestrategy)
###  Parent types: 
- [DeploymentConfig](#deploymentconfig)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
activeDeadlineSeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
annotations | [Map](#map)&lt;[String](#string), [String](#string)&gt; | False | - | - 
customParams | [DCCustomParams](#dccustomparams) | False | - | - 
labels | [Map](#map)&lt;[String](#string), [String](#string)&gt; | False | - | - 
resources | [Nullable](#nullable)&lt;[ContainerResourceSpec](#containerresourcespec)&gt; | False | - | - 
## DCImageChangeTrigger
### Parents: 
- [DCTrigger](#dctrigger)
###  Parent types: 
- [DeploymentConfig](#deploymentconfig)
## DCLifecycleHook
###  Parent types: 
- [DCRecreateParams](#dcrecreateparams)
- [DCRollingParams](#dcrollingparams)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
execNewPod | [Nullable](#nullable)&lt;[DCLifecycleNewPod](#dclifecyclenewpod)&gt; | False | - | - 
failurePolicy | [Enum](#enum)('Abort', 'Retry', 'Ignore') | False | - | - 
tagImages | [Nullable](#nullable)&lt;[DCTagImages](#dctagimages)&gt; | False | - | - 
## DCLifecycleNewPod
### Parents: 
- [EnvironmentPreProcessMixin](#environmentpreprocessmixin)
###  Parent types: 
- [DCLifecycleHook](#dclifecyclehook)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
command | [NonEmpty](#nonempty)&lt;[List](#list)&lt;[String](#string)&gt;&gt; | False | - | - 
containerName | [Identifier](#identifier) | False | - | - 
env | [Nullable](#nullable)&lt;[List](#list)&lt;[ContainerEnvBaseSpec](#containerenvbasespec)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
volumeMounts | [Nullable](#nullable)&lt;[List](#list)&lt;[ContainerVolumeMountSpec](#containervolumemountspec)&gt;&gt; | False | - | - 
volumes | [Nullable](#nullable)&lt;[List](#list)&lt;[Identifier](#identifier)&gt;&gt; | False | - | - 
## DCRecreateParams
###  Parent types: 
- [DCRecreateStrategy](#dcrecreatestrategy)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
mid | [Nullable](#nullable)&lt;[DCLifecycleHook](#dclifecyclehook)&gt; | False | - | - 
post | [Nullable](#nullable)&lt;[DCLifecycleHook](#dclifecyclehook)&gt; | False | - | - 
pre | [Nullable](#nullable)&lt;[DCLifecycleHook](#dclifecyclehook)&gt; | False | - | - 
timeoutSeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
## DCRecreateStrategy
### Parents: 
- [DCBaseUpdateStrategy](#dcbaseupdatestrategy)
###  Parent types: 
- [DeploymentConfig](#deploymentconfig)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
activeDeadlineSeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
annotations | [Map](#map)&lt;[String](#string), [String](#string)&gt; | False | - | - 
customParams | [Nullable](#nullable)&lt;[DCCustomParams](#dccustomparams)&gt; | False | - | - 
labels | [Map](#map)&lt;[String](#string), [String](#string)&gt; | False | - | - 
recreateParams | [Nullable](#nullable)&lt;[DCRecreateParams](#dcrecreateparams)&gt; | False | - | - 
resources | [Nullable](#nullable)&lt;[ContainerResourceSpec](#containerresourcespec)&gt; | False | - | - 
## DCRollingParams
###  Parent types: 
- [DCRollingStrategy](#dcrollingstrategy)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
intervalSeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
maxSurge | [SurgeSpec](#surgespec) | False | - | - 
maxUnavailable | [SurgeSpec](#surgespec) | False | - | - 
post | [Nullable](#nullable)&lt;[DCLifecycleHook](#dclifecyclehook)&gt; | False | - | - 
pre | [Nullable](#nullable)&lt;[DCLifecycleHook](#dclifecyclehook)&gt; | False | - | - 
timeoutSeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
updatePeriodSeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
## DCRollingStrategy
### Parents: 
- [DCBaseUpdateStrategy](#dcbaseupdatestrategy)
###  Parent types: 
- [DeploymentConfig](#deploymentconfig)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
activeDeadlineSeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
annotations | [Map](#map)&lt;[String](#string), [String](#string)&gt; | False | - | - 
customParams | [Nullable](#nullable)&lt;[DCCustomParams](#dccustomparams)&gt; | False | - | - 
labels | [Map](#map)&lt;[String](#string), [String](#string)&gt; | False | - | - 
resources | [Nullable](#nullable)&lt;[ContainerResourceSpec](#containerresourcespec)&gt; | False | - | - 
rollingParams | [Nullable](#nullable)&lt;[DCRollingParams](#dcrollingparams)&gt; | False | - | - 
## DCTagImages
###  Parent types: 
- [DCLifecycleHook](#dclifecyclehook)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
containerName | [Identifier](#identifier) | False | - | - 
toApiVersion | [Nullable](#nullable)&lt;[String](#string)&gt; | False | - | - 
toFieldPath | [Nullable](#nullable)&lt;[String](#string)&gt; | False | - | - 
toKind | [Nullable](#nullable)&lt;[Enum](#enum)('Deployment', 'DeploymentConfig', 'ImageStreamTag')&gt; | False | - | - 
toName | [Nullable](#nullable)&lt;[Identifier](#identifier)&gt; | False | - | - 
toNamespace | [Nullable](#nullable)&lt;[Identifier](#identifier)&gt; | False | - | - 
toResourceVersion | [Nullable](#nullable)&lt;[String](#string)&gt; | False | - | - 
toUid | [Nullable](#nullable)&lt;[String](#string)&gt; | False | - | - 
## DCTrigger
###  Children: 
- [DCConfigChangeTrigger](#dcconfigchangetrigger)
- [DCImageChangeTrigger](#dcimagechangetrigger)
###  Parent types: 
- [DeploymentConfig](#deploymentconfig)
## DaemonSet
### Parents: 
- [SelectorsPreProcessMixin](#selectorspreprocessmixin)
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
pod_template | [PodTemplateSpec](#podtemplatespec) | False | - | - 
selector | [Nullable](#nullable)&lt;[BaseSelector](#baseselector)&gt; | False | &lt;unknown transformation&gt; | - 
## [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)


A Deployment controller provides declarative updates for Pods and ReplicaSets.

You describe a desired state in a Deployment object, and the Deployment controller changes the actual state to the desired state at a controlled rate.
You can define Deployments to create new ReplicaSets, or to remove existing Deployments and adopt all their resources with new Deployments.

### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
minReadySeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
paused | [Nullable](#nullable)&lt;[Boolean](#boolean)&gt; | False | - | - 
pod_template | [PodTemplateSpec](#podtemplatespec) | False | - | - 
progressDeadlineSeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
replicas | [Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt; | False | - | - 
revisionHistoryLimit | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
selector | [Nullable](#nullable)&lt;[BaseSelector](#baseselector)&gt; | False | - | - 
strategy | [Nullable](#nullable)&lt;[DplBaseUpdateStrategy](#dplbaseupdatestrategy)&gt; | False | - | - 
## DeploymentConfig
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
minReadySeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
paused | [Nullable](#nullable)&lt;[Boolean](#boolean)&gt; | False | - | - 
pod_template | [PodTemplateSpec](#podtemplatespec) | False | - | - 
replicas | [Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt; | False | - | - 
revisionHistoryLimit | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
selector | [Nullable](#nullable)&lt;[Map](#map)&lt;[String](#string), [String](#string)&gt;&gt; | False | - | - 
strategy | [DCBaseUpdateStrategy](#dcbaseupdatestrategy) | False | - | - 
test | [Boolean](#boolean) | False | - | - 
triggers | [List](#list)&lt;[DCTrigger](#dctrigger)&gt; | False | - | - 
## DockerCredentials
### Parents: 
- [Secret](#secret)
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
dockers | [Map](#map)&lt;[String](#string), [Map](#map)&lt;[String](#string), [String](#string)&gt;&gt; | False | - | - 
secrets | [Map](#map)&lt;[String](#string), [String](#string)&gt; | False | - | - 
type | [NonEmpty](#nonempty)&lt;[String](#string)&gt; | False | - | - 
## DplBaseUpdateStrategy
###  Children: 
- [DplRecreateStrategy](#dplrecreatestrategy)
- [DplRollingUpdateStrategy](#dplrollingupdatestrategy)
###  Parent types: 
- [Deployment](#deployment)
## DplRecreateStrategy
### Parents: 
- [DplBaseUpdateStrategy](#dplbaseupdatestrategy)
###  Parent types: 
- [Deployment](#deployment)
## DplRollingUpdateStrategy
### Parents: 
- [DplBaseUpdateStrategy](#dplbaseupdatestrategy)
###  Parent types: 
- [Deployment](#deployment)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
maxSurge | [SurgeSpec](#surgespec) | False | - | - 
maxUnavailable | [SurgeSpec](#surgespec) | False | - | - 
## Group
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
users | [NonEmpty](#nonempty)&lt;[List](#list)&lt;[UserIdentifier](#useridentifier)&gt;&gt; | False | - | - 
## Job
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
activeDeadlineSeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[Integer](#integer)&gt;&gt; | False | - | - 
completions | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
manualSelector | [Nullable](#nullable)&lt;[Boolean](#boolean)&gt; | False | - | - 
parallelism | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
pod_template | [PodTemplateSpec](#podtemplatespec) | False | - | - 
selector | [Nullable](#nullable)&lt;[BaseSelector](#baseselector)&gt; | False | - | - 
## LifeCycle
###  Parent types: 
- [ContainerSpec](#containerspec)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
postStart | [Nullable](#nullable)&lt;[LifeCycleProbe](#lifecycleprobe)&gt; | False | - | - 
preStop | [Nullable](#nullable)&lt;[LifeCycleProbe](#lifecycleprobe)&gt; | False | - | - 
## LifeCycleExec
### Parents: 
- [LifeCycleProbe](#lifecycleprobe)
###  Parent types: 
- [LifeCycle](#lifecycle)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
command | [NonEmpty](#nonempty)&lt;[List](#list)&lt;[String](#string)&gt;&gt; | False | - | - 
## LifeCycleHTTP
### Parents: 
- [LifeCycleProbe](#lifecycleprobe)
###  Parent types: 
- [LifeCycle](#lifecycle)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
path | [NonEmpty](#nonempty)&lt;[Path](#path)&gt; | False | - | - 
port | [Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt; | False | - | - 
scheme | [Nullable](#nullable)&lt;[Enum](#enum)('HTTP', 'HTTPS')&gt; | False | - | - 
## LifeCycleProbe
###  Children: 
- [LifeCycleExec](#lifecycleexec)
- [LifeCycleHTTP](#lifecyclehttp)
###  Parent types: 
- [LifeCycle](#lifecycle)
## MatchExpression
###  Parent types: 
- [MatchExpressionsSelector](#matchexpressionsselector)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
key | [NonEmpty](#nonempty)&lt;[String](#string)&gt; | False | - | - 
operator | [Enum](#enum)('In', 'NotIn', 'Exists', 'DoesNotExist') | False | - | - 
values | [Nullable](#nullable)&lt;[List](#list)&lt;[String](#string)&gt;&gt; | False | - | - 
## MatchExpressionsSelector
### Parents: 
- [BaseSelector](#baseselector)
###  Parent types: 
- [DaemonSet](#daemonset)
- [Deployment](#deployment)
- [Job](#job)
- [PersistentVolumeClaim](#persistentvolumeclaim)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
matchExpressions | [NonEmpty](#nonempty)&lt;[List](#list)&lt;[MatchExpression](#matchexpression)&gt;&gt; | False | - | - 
## MatchLabelsSelector
### Parents: 
- [BaseSelector](#baseselector)
###  Parent types: 
- [DaemonSet](#daemonset)
- [Deployment](#deployment)
- [Job](#job)
- [PersistentVolumeClaim](#persistentvolumeclaim)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
matchLabels | [Map](#map)&lt;[String](#string), [String](#string)&gt; | False | - | - 
## Namespace
###  Children: 
- [Project](#project)
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
## PersistentVolume
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
accessModes | [List](#list)&lt;[Enum](#enum)('ReadWriteOnce', 'ReadOnlyMany', 'ReadWriteMany')&gt; | False | - | - 
awsElasticBlockStore | [Nullable](#nullable)&lt;[AWSElasticBlockStore](#awselasticblockstore)&gt; | False | - | - 
capacity | [Memory](#memory) | False | - | - 
claimRef | [Nullable](#nullable)&lt;[PersistentVolumeRef](#persistentvolumeref)&gt; | False | - | - 
persistentVolumeReclaimPolicy | [Nullable](#nullable)&lt;[Enum](#enum)('Retain', 'Recycle', 'Delete')&gt; | False | - | - 
## PersistentVolumeClaim
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
accessModes | [List](#list)&lt;[Enum](#enum)('ReadWriteOnce', 'ReadOnlyMany', 'ReadWriteMany')&gt; | False | - | - 
request | [Memory](#memory) | False | - | - 
selector | [Nullable](#nullable)&lt;[BaseSelector](#baseselector)&gt; | False | - | - 
volumeName | [Nullable](#nullable)&lt;[Identifier](#identifier)&gt; | False | &lt;unknown transformation&gt; | - 
## PersistentVolumeRef
###  Parent types: 
- [PersistentVolume](#persistentvolume)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
apiVersion | [Nullable](#nullable)&lt;[String](#string)&gt; | False | - | - 
kind | [Nullable](#nullable)&lt;[CaseIdentifier](#caseidentifier)&gt; | False | - | - 
name | [Nullable](#nullable)&lt;[Identifier](#identifier)&gt; | False | - | - 
ns | [Nullable](#nullable)&lt;[Identifier](#identifier)&gt; | False | - | - 
## PodImagePullSecret
###  Parent types: 
- [PodTemplateSpec](#podtemplatespec)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | False | - | - 
## PodTemplateSpec
###  Parent types: 
- [DaemonSet](#daemonset)
- [Deployment](#deployment)
- [DeploymentConfig](#deploymentconfig)
- [Job](#job)
- [ReplicationController](#replicationcontroller)
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
containers | [NonEmpty](#nonempty)&lt;[List](#list)&lt;[ContainerSpec](#containerspec)&gt;&gt; | False | - | - 
dnsPolicy | [Nullable](#nullable)&lt;[Enum](#enum)('ClusterFirst')&gt; | False | - | - 
hostIPC | [Nullable](#nullable)&lt;[Boolean](#boolean)&gt; | False | - | - 
hostNetwork | [Nullable](#nullable)&lt;[Boolean](#boolean)&gt; | False | - | - 
hostPID | [Nullable](#nullable)&lt;[Boolean](#boolean)&gt; | False | - | - 
imagePullSecrets | [Nullable](#nullable)&lt;[List](#list)&lt;[PodImagePullSecret](#podimagepullsecret)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
name | [Nullable](#nullable)&lt;[Identifier](#identifier)&gt; | False | - | - 
nodeSelector | [Nullable](#nullable)&lt;[Map](#map)&lt;[String](#string), [String](#string)&gt;&gt; | False | - | - 
restartPolicy | [Nullable](#nullable)&lt;[Enum](#enum)('Always', 'OnFailure', 'Never')&gt; | False | - | - 
securityContext | [Nullable](#nullable)&lt;[SecurityContext](#securitycontext)&gt; | False | - | - 
serviceAccountName | [Nullable](#nullable)&lt;[Identifier](#identifier)&gt; | False | &lt;unknown transformation&gt; | [serviceAccount](#serviceaccount) 
terminationGracePeriodSeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[Integer](#integer)&gt;&gt; | False | - | - 
volumes | [Nullable](#nullable)&lt;[List](#list)&lt;[PodVolumeBaseSpec](#podvolumebasespec)&gt;&gt; | False | - | - 
## PodVolumeBaseSpec
###  Children: 
- [PodVolumeHostSpec](#podvolumehostspec)
- [PodVolumeItemMapper](#podvolumeitemmapper)
- [PodVolumePVCSpec](#podvolumepvcspec)
- [PodVolumeEmptyDirSpec](#podvolumeemptydirspec)
- [PodVolumeConfigMapSpec](#podvolumeconfigmapspec)
- [PodVolumeSecretSpec](#podvolumesecretspec)
###  Parent types: 
- [PodTemplateSpec](#podtemplatespec)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | False | - | - 
## PodVolumeConfigMapSpec
### Parents: 
- [PodVolumeItemMapper](#podvolumeitemmapper)
- [PodVolumeBaseSpec](#podvolumebasespec)
###  Parent types: 
- [PodTemplateSpec](#podtemplatespec)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
defaultMode | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[Integer](#integer)&gt;&gt; | False | - | - 
item_map | [Nullable](#nullable)&lt;[Map](#map)&lt;[String](#string), [String](#string)&gt;&gt; | False | - | - 
map_name | [Identifier](#identifier) | False | - | - 
name | [Identifier](#identifier) | False | - | - 
## PodVolumeEmptyDirSpec
### Parents: 
- [PodVolumeBaseSpec](#podvolumebasespec)
###  Parent types: 
- [PodTemplateSpec](#podtemplatespec)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | False | - | - 
## PodVolumeHostSpec
### Parents: 
- [PodVolumeBaseSpec](#podvolumebasespec)
###  Parent types: 
- [PodTemplateSpec](#podtemplatespec)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | False | - | - 
path | [String](#string) | False | - | - 
## PodVolumeItemMapper
### Parents: 
- [PodVolumeBaseSpec](#podvolumebasespec)
###  Children: 
- [PodVolumeConfigMapSpec](#podvolumeconfigmapspec)
- [PodVolumeSecretSpec](#podvolumesecretspec)
###  Parent types: 
- [PodTemplateSpec](#podtemplatespec)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
item_map | [Nullable](#nullable)&lt;[Map](#map)&lt;[String](#string), [String](#string)&gt;&gt; | False | - | - 
name | [Identifier](#identifier) | False | - | - 
## PodVolumePVCSpec
### Parents: 
- [PodVolumeBaseSpec](#podvolumebasespec)
###  Parent types: 
- [PodTemplateSpec](#podtemplatespec)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
claimName | [Identifier](#identifier) | False | - | - 
name | [Identifier](#identifier) | False | - | - 
## PodVolumeSecretSpec
### Parents: 
- [PodVolumeItemMapper](#podvolumeitemmapper)
- [PodVolumeBaseSpec](#podvolumebasespec)
###  Parent types: 
- [PodTemplateSpec](#podtemplatespec)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
defaultMode | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[Integer](#integer)&gt;&gt; | False | - | - 
item_map | [Nullable](#nullable)&lt;[Map](#map)&lt;[String](#string), [String](#string)&gt;&gt; | False | - | - 
name | [Identifier](#identifier) | False | - | - 
secret_name | [Identifier](#identifier) | False | - | - 
## PolicyBinding
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [ColonIdentifier](#colonidentifier) | True | - | - 
roleBindings | [List](#list)&lt;[PolicyBindingRoleBinding](#policybindingrolebinding)&gt; | False | &lt;unknown transformation&gt; | - 
## PolicyBindingRoleBinding
### Parents: 
- [RoleBindingXF](#rolebindingxf)
###  Parent types: 
- [PolicyBinding](#policybinding)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
metadata | [Nullable](#nullable)&lt;[Map](#map)&lt;[String](#string), [String](#string)&gt;&gt; | False | - | - 
name | [SystemIdentifier](#systemidentifier) | False | - | - 
ns | [Identifier](#identifier) | False | - | - 
roleRef | [RoleRef](#roleref) | False | &lt;unknown transformation&gt; | - 
subjects | [NonEmpty](#nonempty)&lt;[List](#list)&lt;[RoleSubject](#rolesubject)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
## PolicyRule
###  Parent types: 
- [ClusterRole](#clusterrole)
- [Role](#role)
- [RoleBase](#rolebase)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
apiGroups | [NonEmpty](#nonempty)&lt;[List](#list)&lt;[String](#string)&gt;&gt; | False | - | - 
attributeRestrictions | [Nullable](#nullable)&lt;[String](#string)&gt; | False | - | - 
nonResourceURLs | [Nullable](#nullable)&lt;[List](#list)&lt;[String](#string)&gt;&gt; | False | - | - 
resourceNames | [Nullable](#nullable)&lt;[List](#list)&lt;[String](#string)&gt;&gt; | False | - | - 
resources | [NonEmpty](#nonempty)&lt;[List](#list)&lt;[NonEmpty](#nonempty)&lt;[String](#string)&gt;&gt;&gt; | False | - | - 
verbs | [NonEmpty](#nonempty)&lt;[List](#list)&lt;[Enum](#enum)('get', 'list', 'create', 'update', 'delete', 'deletecollection', 'watch')&gt;&gt; | False | - | - 
## Project
### Parents: 
- [Namespace](#namespace)
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
## ReplicationController
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
minReadySeconds | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
pod_template | [PodTemplateSpec](#podtemplatespec) | False | - | - 
replicas | [Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt; | False | - | - 
selector | [Nullable](#nullable)&lt;[Map](#map)&lt;[String](#string), [String](#string)&gt;&gt; | False | - | - 
## Role
### Parents: 
- [RoleBase](#rolebase)
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
rules | [NonEmpty](#nonempty)&lt;[List](#list)&lt;[PolicyRule](#policyrule)&gt;&gt; | False | - | - 
## RoleBinding
### Parents: 
- [RoleBindingBase](#rolebindingbase)
- [RoleBindingXF](#rolebindingxf)
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [SystemIdentifier](#systemidentifier) | True | - | - 
roleRef | [RoleRef](#roleref) | False | &lt;unknown transformation&gt; | - 
subjects | [NonEmpty](#nonempty)&lt;[List](#list)&lt;[RoleSubject](#rolesubject)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
## RoleRef
###  Parent types: 
- [ClusterRoleBinding](#clusterrolebinding)
- [PolicyBindingRoleBinding](#policybindingrolebinding)
- [RoleBinding](#rolebinding)
- [RoleBindingBase](#rolebindingbase)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Nullable](#nullable)&lt;[SystemIdentifier](#systemidentifier)&gt; | False | - | - 
ns | [Nullable](#nullable)&lt;[Identifier](#identifier)&gt; | False | - | - 
## RoleSubject
###  Parent types: 
- [ClusterRoleBinding](#clusterrolebinding)
- [PolicyBindingRoleBinding](#policybindingrolebinding)
- [RoleBinding](#rolebinding)
- [RoleBindingBase](#rolebindingbase)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
kind | [CaseIdentifier](#caseidentifier) | False | - | - 
name | [String](#string) | False | - | - 
ns | [Nullable](#nullable)&lt;[Identifier](#identifier)&gt; | False | - | - 
## Route
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
host | [Domain](#domain) | False | - | - 
port | [RouteDestPort](#routedestport) | False | - | - 
tls | [Nullable](#nullable)&lt;[RouteTLS](#routetls)&gt; | False | - | - 
to | [NonEmpty](#nonempty)&lt;[List](#list)&lt;[RouteDest](#routedest)&gt;&gt; | False | - | - 
wildcardPolicy | [Enum](#enum)('Subdomain', 'None') | False | - | - 
## RouteDest
###  Children: 
- [RouteDestService](#routedestservice)
###  Parent types: 
- [Route](#route)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
weight | [Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt; | False | - | - 
## RouteDestPort
###  Parent types: 
- [Route](#route)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
targetPort | [Identifier](#identifier) | False | - | - 
## RouteDestService
### Parents: 
- [RouteDest](#routedest)
###  Parent types: 
- [Route](#route)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | False | - | - 
weight | [Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt; | False | - | - 
## RouteTLS
###  Parent types: 
- [Route](#route)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
caCertificate | [Nullable](#nullable)&lt;[NonEmpty](#nonempty)&lt;[String](#string)&gt;&gt; | False | - | - 
certificate | [Nullable](#nullable)&lt;[NonEmpty](#nonempty)&lt;[String](#string)&gt;&gt; | False | - | - 
destinationCACertificate | [Nullable](#nullable)&lt;[NonEmpty](#nonempty)&lt;[String](#string)&gt;&gt; | False | - | - 
insecureEdgeTerminationPolicy | [Enum](#enum)('Allow', 'Disable', 'Redirect') | False | - | - 
key | [Nullable](#nullable)&lt;[NonEmpty](#nonempty)&lt;[String](#string)&gt;&gt; | False | - | - 
termination | [Enum](#enum)('edge', 'reencrypt', 'passthrough') | False | - | - 
## SAImgPullSecretSubject
###  Parent types: 
- [ServiceAccount](#serviceaccount)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | False | - | - 
## SASecretSubject
###  Parent types: 
- [ServiceAccount](#serviceaccount)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
kind | [Nullable](#nullable)&lt;[CaseIdentifier](#caseidentifier)&gt; | False | - | - 
name | [Nullable](#nullable)&lt;[Identifier](#identifier)&gt; | False | - | - 
ns | [Nullable](#nullable)&lt;[Identifier](#identifier)&gt; | False | - | - 
## SCCGroupRange
###  Parent types: 
- [SCCGroups](#sccgroups)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
max | [Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt; | False | - | - 
min | [Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt; | False | - | - 
## SCCGroups
###  Parent types: 
- [SecurityContextConstraints](#securitycontextconstraints)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
ranges | [Nullable](#nullable)&lt;[List](#list)&lt;[SCCGroupRange](#sccgrouprange)&gt;&gt; | False | - | - 
type | [Nullable](#nullable)&lt;[Enum](#enum)('MustRunAs', 'RunAsAny')&gt; | False | - | - 
## SCCRunAsUser
###  Parent types: 
- [SecurityContextConstraints](#securitycontextconstraints)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
type | [Enum](#enum)('MustRunAs', 'RunAsAny', 'MustRunAsRange', 'MustRunAsNonRoot') | False | - | - 
uid | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
uidRangeMax | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
uidRangeMin | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;&gt; | False | - | - 
## SCCSELinux
###  Parent types: 
- [SecurityContextConstraints](#securitycontextconstraints)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
level | [Nullable](#nullable)&lt;[String](#string)&gt; | False | - | - 
role | [Nullable](#nullable)&lt;[String](#string)&gt; | False | - | - 
strategy | [Nullable](#nullable)&lt;[Enum](#enum)('MustRunAs', 'RunAsAny')&gt; | False | - | - 
type | [Nullable](#nullable)&lt;[String](#string)&gt; | False | - | - 
user | [Nullable](#nullable)&lt;[String](#string)&gt; | False | - | - 
## Secret
###  Children: 
- [DockerCredentials](#dockercredentials)
- [TLSCredentials](#tlscredentials)
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
secrets | [Map](#map)&lt;[String](#string), [String](#string)&gt; | False | - | - 
type | [NonEmpty](#nonempty)&lt;[String](#string)&gt; | False | - | - 
## SecurityContext
###  Parent types: 
- [ContainerSpec](#containerspec)
- [PodTemplateSpec](#podtemplatespec)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
fsGroup | [Nullable](#nullable)&lt;[Integer](#integer)&gt; | False | - | - 
privileged | [Nullable](#nullable)&lt;[Boolean](#boolean)&gt; | False | - | - 
runAsNonRoot | [Nullable](#nullable)&lt;[Boolean](#boolean)&gt; | False | - | - 
runAsUser | [Nullable](#nullable)&lt;[Integer](#integer)&gt; | False | - | - 
supplementalGroups | [Nullable](#nullable)&lt;[List](#list)&lt;[Integer](#integer)&gt;&gt; | False | - | - 
## SecurityContextConstraints
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
allowHostDirVolumePlugin | [Boolean](#boolean) | False | - | - 
allowHostIPC | [Boolean](#boolean) | False | - | - 
allowHostNetwork | [Boolean](#boolean) | False | - | - 
allowHostPID | [Boolean](#boolean) | False | - | - 
allowHostPorts | [Boolean](#boolean) | False | - | - 
allowPrivilegedContainer | [Boolean](#boolean) | False | - | - 
allowedCapabilities | [Nullable](#nullable)&lt;[List](#list)&lt;[String](#string)&gt;&gt; | False | - | - 
defaultAddCapabilities | [Nullable](#nullable)&lt;[List](#list)&lt;[String](#string)&gt;&gt; | False | - | - 
fsGroup | [Nullable](#nullable)&lt;[SCCGroups](#sccgroups)&gt; | False | - | - 
groups | [List](#list)&lt;[SystemIdentifier](#systemidentifier)&gt; | False | - | - 
priority | [Nullable](#nullable)&lt;[Positive](#positive)&lt;[Integer](#integer)&gt;&gt; | False | - | - 
readOnlyRootFilesystem | [Boolean](#boolean) | False | - | - 
requiredDropCapabilities | [Nullable](#nullable)&lt;[List](#list)&lt;[String](#string)&gt;&gt; | False | - | - 
runAsUser | [Nullable](#nullable)&lt;[SCCRunAsUser](#sccrunasuser)&gt; | False | - | - 
seLinuxContext | [Nullable](#nullable)&lt;[SCCSELinux](#sccselinux)&gt; | False | - | - 
seccompProfiles | [Nullable](#nullable)&lt;[List](#list)&lt;[String](#string)&gt;&gt; | False | - | - 
supplementalGroups | [Nullable](#nullable)&lt;[SCCGroups](#sccgroups)&gt; | False | - | - 
users | [List](#list)&lt;[SystemIdentifier](#systemidentifier)&gt; | False | - | - 
volumes | [List](#list)&lt;[Enum](#enum)('configMap', 'downwardAPI', 'emptyDir', 'hostPath', 'nfs', 'persistentVolumeClaim', 'secret', '*')&gt; | False | - | - 
## Service
###  Children: 
- [ClusterIPService](#clusteripservice)
- [AWSLoadBalancerService](#awsloadbalancerservice)
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
ports | [NonEmpty](#nonempty)&lt;[List](#list)&lt;[ServicePort](#serviceport)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
selector | [NonEmpty](#nonempty)&lt;[Map](#map)&lt;[String](#string), [String](#string)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
sessionAffinity | [Nullable](#nullable)&lt;[Enum](#enum)('ClientIP', 'None')&gt; | False | - | - 
## ServiceAccount
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
imagePullSecrets | [Nullable](#nullable)&lt;[List](#list)&lt;[SAImgPullSecretSubject](#saimgpullsecretsubject)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
secrets | [Nullable](#nullable)&lt;[List](#list)&lt;[SASecretSubject](#sasecretsubject)&gt;&gt; | False | &lt;unknown transformation&gt; | - 
## ServicePort
###  Parent types: 
- [AWSLoadBalancerService](#awsloadbalancerservice)
- [ClusterIPService](#clusteripservice)
- [Service](#service)
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Nullable](#nullable)&lt;[Identifier](#identifier)&gt; | False | - | - 
port | [Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt; | False | - | - 
protocol | [Enum](#enum)('TCP', 'UDP') | False | - | - 
targetPort | [OneOf](#oneof)&lt;[Positive](#positive)&lt;[NonZero](#nonzero)&lt;[Integer](#integer)&gt;&gt;, [Identifier](#identifier)&gt; | False | - | - 
## StorageClass
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
parameters | [Map](#map)&lt;[String](#string), [String](#string)&gt; | False | - | - 
provisioner | [String](#string) | False | - | - 
## TLSCredentials
### Parents: 
- [Secret](#secret)
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [Identifier](#identifier) | True | - | - 
secrets | [Map](#map)&lt;[String](#string), [String](#string)&gt; | False | - | - 
tls_cert | [String](#string) | False | - | - 
tls_key | [String](#string) | False | - | - 
type | [NonEmpty](#nonempty)&lt;[String](#string)&gt; | False | - | - 
## User
### Metadata
Name | Format
---- | ------
annotations | [Map](#map)<[String](#string), [String](#string)>
labels | [Map](#map)<[String](#string), [String](#string)>
###  Properties:

Name | Type | Identifier | Type Transformation | Aliases
---- | ---- | ---------- | ------------------- | -------
name | [UserIdentifier](#useridentifier) | True | - | - 
fullName | [Nullable](#nullable)&lt;[String](#string)&gt; | False | - | - 
identities | [NonEmpty](#nonempty)&lt;[List](#list)&lt;[NonEmpty](#nonempty)&lt;[String](#string)&gt;&gt;&gt; | False | - | - 
