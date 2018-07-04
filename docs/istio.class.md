# Istio Class definitions

At the moment most of the classes reflect the original data definition descibed inside istio documentation.

## [IstioRouteRule](https://istio.io/docs/reference/config/istio.networking.v1alpha3/)
```
IstioRouteRule:
IstioRouteRule:
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    destination:          Map<String, String>
    precedence:           Integer
    version:              String
```

## [IstioPort](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#Port)
```
IstioPort:
IstioPort:
  parent types: IstioServer, IstioServiceEntriesSpec
  properties:
    name:                 Nullable<String>
    number:               Integer
    protocol:             String
```

## [IstioServiceEntryEndpoint](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#ServiceEntry.Endpoint)
```
IstioServiceEntryEndpoint:
IstioServiceEntryEndpoint (abstract type):
  parent types: IstioServiceEntriesSpec
  properties:
    address:              String
    labels:               Nullable<Map<String, String>>
    ports:                Nullable<Map<String, Integer>>
```

## [IstioServiceEntriesSpec](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#ServiceEntry)
```
IstioServiceEntriesSpec:
IstioServiceEntriesSpec:
  parent types: IstioServiceEntries
  properties:
    addresses:            Nullable<List<String>>
    endpoints:            Nullable<List<IstioServiceEntryEndpoint>>
    hosts:                Nullable<List<Domain>>
    location:             Nullable<Enum(u'MESH_EXTERNAL', u'MESH_INTERNAL')>
    ports:                Nullable<IstioPort>
    resolution:           Nullable<Enum(u'NONE', u'STATIC', u'DNS')>
```

## [IstioServiceEntries](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#ServiceEntry)
```
IstioServiceEntries:
IstioServiceEntries:
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    spec:                 Nullable<IstioServiceEntriesSpec>
```

## [IstioVirtualServiceSpec](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#VirtualService)
```
IstioVirtualServiceSpec:
IstioVirtualServiceSpec:
  parent types: IstioVirtualService
  properties:
    gateways:             Nullable<List<String>>
    hosts:                Nullable<List<Domain>>
    http:                 Nullable<List<IstioHTTPRoute>>
```

## [IstioVirtualService](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#VirtualService)
```
IstioVirtualService:
IstioVirtualService:
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    spec:                 Nullable<IstioVirtualServiceSpec>
```

## [IstioConnectionPool]()
*TODO*: This one needs to be changed to reflect the structure reported into istio documentation
```
IstioConnectionPool:
IstioConnectionPool:
  parent types: IstioTrafficPolicy
  properties:
    connectTimeout:       Nullable<String>
    maxConnections:       Nullable<Integer>
```

## [IstioOutlierDetectionHTTPSettings](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#OutlierDetection.HTTPSettings)
```
IstioOutlierDetectionHTTPSettings:
IstioOutlierDetectionHTTPSettings:
  parent types: IstioOutlierDetection
  properties:
    baseEjectionTime:     Nullable<String>
    consecutiveErrors:    Nullable<Integer>
    interval:             Nullable<String>
    maxEjectionPercent:   Nullable<Integer>
```

## [IstioOutlierDetection](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#OutlierDetection)
```
IstioOutlierDetection:
IstioOutlierDetection:
  parent types: IstioPortTrafficPolicy, IstioTrafficPolicy
  properties:
    http:                 Nullable<IstioOutlierDetectionHTTPSettings>
```

## [IstioTLSSettings](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#TLSSettings)
```
IstioTLSSettings:
IstioTLSSettings:
  parent types: IstioPortTrafficPolicy, IstioTrafficPolicy
  properties:
    caCertificates:       Nullable<String>
    clientCertificate:    Nullable<String>
    mode:                 Nullable<Enum(u'DISABLE', u'SIMPLE', u'MUTUAL', u'ISTIO_MUTUAL')>
    privateKey:           Nullable<String>
    sni:                  Nullable<String>
    subjectAltNames:      Nullable<List<String>>
```

## [IstioConnectionPoolSettingsTCPSettings](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#ConnectionPoolSettings.TCPSettings)
```
IstioConnectionPoolSettingsTCPSettings:
IstioConnectionPoolSettingsTCPSettings:
  parent types: IstioConnectionPoolSettings
  properties:
    connectTimeout:       Nullable<String>
    maxConnections:       Nullable<String>
```

## [IstioConnectionPoolSettingsHTTPSettings](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#ConnectionPoolSettings.HTTPSettings)
```
IstioConnectionPoolSettingsHTTPSettings:
IstioConnectionPoolSettingsHTTPSettings:
  parent types: IstioConnectionPoolSettings
  properties:
    http1MaxPendingRequests: Nullable<Integer>
    http2MaxRequests:     Nullable<Integer>
    maxRequestsPerConnection: Nullable<Integer>
    maxRetries:           Nullable<Integer>
```

## [IstioConnectionPoolSettings](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#ConnectionPoolSettings)
```
IstioConnectionPoolSettings:
IstioConnectionPoolSettings:
  parent types: IstioPortTrafficPolicy
  properties:
    http:                 Nullable<IstioConnectionPoolSettingsHTTPSettings>
    tcp:                  Nullable<IstioConnectionPoolSettingsTCPSettings>
```

## [IstioPortTrafficPolicy](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#TrafficPolicy.PortTrafficPolicy)
```
IstioPortTrafficPolicy:
IstioPortTrafficPolicy:
  parent types: IstioTrafficPolicy
  properties:
    connectionPool:       Nullable<IstioConnectionPoolSettings>
    loadBalancer:         Nullable<IstioLoadBalancer>
    outlierDetection:     Nullable<IstioOutlierDetection>
    port:                 Nullable<IstioPortSelector>
    tls:                  Nullable<IstioTLSSettings>
```

## [IstioTrafficPolicy](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#TrafficPolicy)
```
IstioTrafficPolicy:
IstioTrafficPolicy:
  parent types: IstioDestinationRuleSpecs, IstioSubset
  properties:
    connectionPool:       Nullable<IstioConnectionPool>
    loadBalancer:         Nullable<IstioLoadBalancer>
    outlierDetection:     Nullable<IstioOutlierDetection>
    portLevelSettings:    Nullable<IstioPortTrafficPolicy>
    tls:                  Nullable<IstioTLSSettings>
```

## [IstioSubset](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#Subset)
```
IstioSubset:
IstioSubset:
  parent types: IstioDestinationRuleSpecs
  properties:
    labels:               Nullable<Map<String, String>>
    name:                 Nullable<String>
    trafficPolicy:        Nullable<IstioTrafficPolicy>
```

## [IstioDestinationRuleSpecs](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#DestinationRule)
```
IstioDestinationRuleSpecs:
IstioDestinationRuleSpecs:
  parent types: IstioDestinationRule
  properties:
    host:                 String
    subsets:              Nullable<List<IstioSubset>>
    trafficPolicy:        Nullable<IstioTrafficPolicy>
```

## [IstioDestinationRule](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#DestinationRule)
```
IstioDestinationRule:
IstioDestinationRule:
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    Identifier
    spec:                 Nullable<IstioDestinationRuleSpecs>
```

## [IstioHTTPFaultInjectionAbort](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#HTTPFaultInjection.Abort)
```
IstioHTTPFaultInjectionAbort:
IstioHTTPFaultInjectionAbort:
  parent types: IstioHTTPFaultInjection
  properties:
    httpStatus:           Integer
    percent:              Nullable<Integer>
```

## [IstioHTTPFaultInjectionDelay](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#HTTPFaultInjection.Delay)
```
IstioHTTPFaultInjectionDelay:
IstioHTTPFaultInjectionDelay:
  parent types: IstioHTTPFaultInjection
  properties:
    fixedDelay:           String
    percent:              Nullable<Positive<Integer>>
```

## [IstioHTTPFaultInjection](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#HTTPFaultInjection)
```
IstioHTTPFaultInjection:
IstioHTTPFaultInjection:
  parent types: IstioHTTPRoute
  properties:
    abort:                Nullable<IstioHTTPFaultInjectionAbort>
    delay:                Nullable<IstioHTTPFaultInjectionDelay>
```

## [IstioStringMatch](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#StringMatch)
```
IstioStringMatch:
IstioStringMatch:
  parent types: IstioHTTPMatchRequest
  properties:
    exact:                Nullable<String>
    prefix:               Nullable<String>
    regex:                Nullable<String>
```

## [IstioHTTPMatchRequest](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#HTTPMatchRequest)
```
IstioHTTPMatchRequest:
IstioHTTPMatchRequest:
  parent types: IstioHTTPRoute
  properties:
    authority:            Nullable<IstioStringMatch>
    gateways:             Nullable<List<String>>
    headers:              Nullable<Map<String, String>>
    method:               Nullable<IstioStringMatch>
    port:                 Nullable<Integer>
    scheme:               Nullable<IstioStringMatch>
    sourceLabels:         Nullable<Map<String, String>>
    uri:                  Nullable<IstioStringMatch>
```

## [IstioHTTPRetry](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#HTTPRetry)
```
IstioHTTPRetry:
IstioHTTPRetry:
  parent types: IstioHTTPRoute
  properties:
    attempts:             Nullable<Integer>
    perTryTimeout:        Nullable<String>
```

## [IstioHTTPRedirect](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#HTTPRedirect)
```
IstioHTTPRedirect:
IstioHTTPRedirect:
  parent types: IstioHTTPRoute
  properties:
    authority:            Nullable<String>
    uri:                  Nullable<String>
```

## [IstioHTTPRewrite](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#HTTPRewrite)
```
IstioHTTPRewrite:
IstioHTTPRewrite:
  parent types: IstioHTTPRoute
  properties:
    authority:            Nullable<String>
    uri:                  Nullable<String>
```

## [IstioPortSelector](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#PortSelector)
```
IstioPortSelector:
IstioPortSelector:
  parent types: IstioDestination, IstioPortTrafficPolicy
  properties:
    number:               Nullable<Integer>
```

## [IstioDestination](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#Destination)
```
IstioDestination:
IstioDestination:
  parent types: IstioDestinationWeight, IstioHTTPRoute
  properties:
    host:                 Nullable<String>
    port:                 Nullable<IstioPortSelector>
    subset:               Nullable<String>
```

## [IstioDestinationWeight](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#DestinationWeight)
```
IstioDestinationWeight:
IstioDestinationWeight:
  parent types: IstioHTTPRoute
  properties:
    destination:          Nullable<IstioDestination>
    weight:               Nullable<Integer>
```

## [IstioCorsPolicy](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#CorsPolicy)
```
IstioCorsPolicy:
IstioCorsPolicy:
  parent types: IstioHTTPRoute
  properties:
    allowCredentials:     Nullable<Boolean>
    allowHeaders:         Nullable<List<String>>
    allowMethods:         Nullable<List<String>>
    allowOrigin:          Nullable<List<String>>
    exposeHeaders:        Nullable<List<String>>
    maxAge:               Nullable<String>
```

## [IstioHTTPRoute](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#HTTPRoute)
```
IstioHTTPRoute:
IstioHTTPRoute:
  parent types: IstioVirtualServiceSpec
  properties:
    appendHeaders:        Nullable<Map<String, String>>
    corsPolicy:           Nullable<IstioCorsPolicy>
    fault:                Nullable<IstioHTTPFaultInjection>
    match:                Nullable<List<IstioHTTPMatchRequest>>
    mirror:               Nullable<IstioDestination>
    redirect:             Nullable<IstioHTTPRedirect>
    retries:              Nullable<IstioHTTPRetry>
    rewrite:              Nullable<IstioHTTPRewrite>
    route:                Nullable<List<IstioDestinationWeight>>
    timeout:              Nullable<String>
    websocketUpgrade:     Nullable<Boolean>
```

## [IstioServerTLSOptions](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#Server.TLSOptions)
```
IstioServerTLSOptions:
IstioServerTLSOptions:
  parent types: IstioServer
  properties:
    caCertificates:       Nullable<String>
    httpsRedirect:        Nullable<Boolean>
    mode:                 Nullable<Enum(u'PASSTHROUGH', u'SIMPLE', u'MUTUAL')>
    privateKey:           Nullable<String>
    serverCertificate:    Nullable<String>
    subjectAltNames:      Nullable<List<String>>
```

## [IstioServer](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#Server)
```
IstioServer:
IstioServer:
  parent types: IstioGatewaySpec
  properties:
    hosts:                Nullable<List<Domain>>
    port:                 Nullable<IstioPort>
    tls:                  Nullable<IstioServerTLSOptions>
```

## [IstioGatewaySpec](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#Gateway)
```
IstioGatewaySpec:
IstioGatewaySpec:
  parent types: IstioGateway
  properties:
    selector:             Nullable<Map<String, String>>
    servers:              List<IstioServer>
```

## [IstioGateway](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#Gateway)
```
IstioGateway:
IstioGateway:
  metadata:
    annotations:          Map<String, String>
    labels:               Map<String, String>
  properties:
    name (identifier):    String
    spec:                 IstioGatewaySpec
```

## [IstioLoadBalancer](https://istio.io/docs/reference/config/istio.networking.v1alpha3/#LoadBalancerSettings)
```
IstioLoadBalancer:
IstioLoadBalancer:
  parent types: IstioPortTrafficPolicy, IstioTrafficPolicy
  properties:
    consistentHash:       Nullable<Map<String, String>>
    simple:               Enum(u'LEAST_CONN', u'ROUND_ROBIN', u'RANDOM', u'PASSTHROUGH')
```
