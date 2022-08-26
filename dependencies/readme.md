
# HELM version : >= v3.8.2

That is complete solution to deploy application into kubernetes and which can be used inside cicd tools like Jenkins or something like that. It is one-time installation however it should be upgraded once you have upgraded Kubernetes version.

| key | value |
|--|--|
| dependency | Istio Service Mesh or Metrics |

**TYPE OF DEPLOYMENT**
- deployIstio = To install Istio Service Mesh
- deployMetrics = To install Metrics metrics collection

## **How to deploy dependencies into kubernetes**

    ./deploy [DEPLOYMENT-TYPE]


**Here is to deploy with real world variable**

    ./deploy deployIstio
