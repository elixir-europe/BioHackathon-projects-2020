# CI/CD Strategy

**Topic coordinator:** Marius Dieckmann

[&#8629; All topics][topics-overview]

The goal of this topic is to design and implement a decoupled CI/CD strategy
that allows:

* Service developers to focus on implementing changes, building and pushing
  updated images
* System administrators/devops to focus on delivering those changes to the
  instances of that service they are maintaining

These requirements suggest a "pub/sub" strategy where the publishing of new
container images for a given stage/branch (e.g., production, dev, demo)
automatically triggers delivery at subscribed deployments. Such a setup would
grant individual nodes of the ELIXIR Cloud network full autonomy over the
services they are deploying and maintaining, without the need for central
coordination or the involvement of service developers in the deployment/upgrade
process.

To achieve this, a contract would need to be specified on how container images
should be named. A subscription service setting and managing web hooks (e.g.,
in Docker Hub) and callbacks to deployments (e.g., Kubernetes, OpenShift) could
be implemented in the [ELIXIR Cloud service registry][topic-service-registry],
which could act as a broker in the following manner: A service registering in
the registry (e.g., a production WES instance) could specify whether it wants
to subscribe to updates of the service. If so, the service registry would set
up a web hook in the container registry that would lead to a callback to the
service registry everytime a change to the corresponding container image is
made. The service registry would then forward this signal to the deployment,
which can then trigger its CD pipeline to deliver the update. To clarify which
changes to the service should be broadcast to which services, a contract on the
precise image tags to be used has to be agreed upon and honored by each party
(developer/CI endpoint, service registry/broker, devop/CD starting point).

A tentative outline of the steps involved in this topic:

1. Write schema/specification for tag names, that should adhere to semantic
  versioning][sem-ver]. A possible starting point could be:
  `<api-version>-<stage>-<timestamp>`, where `<api-version>` is the version of
  the GA4GH API specs the service is implementing, `<stage>` is the deployment
  type (e.g,. `production`, `staging`, `development`, `demo`)^, and
  `<timestamp>` is a date, e.g., of the form `YYMMDD-HHMMSS`. An example image
  name, including the full tage could be:
  `elixircloud/cwl-wes:1.1-demo-201108-195630`  
  ^ Allowed values for stages should be enumerated in the schema
2. Write an example CI configuration (e.g., Travis) that builds images with the
  tag names defined in step 1. for the different stages defined.
3. Research possible, ideally free, solutions how Kubernetes/OpenShift clusters
  can accept accept callbacks to trigger service upgrades and decide for
  solution. Some starting points:  
  <https://itnext.io/setting-up-push-to-deploy-kubernetes-workflow-with-github-and-keel-43173d996587>  
  <https://codelabs.developers.google.com/codelabs/cloud-spinnaker-kubernetes-cd/#0>  
  <https://medium.com/google-cloud/continuous-deployment-to-cloud-run-services-based-on-a-new-container-image-bccd776b7357>
4. Draft schema extension for GA4GH Service API to allow subscribing to
  image updates and endpoint accepting calls from container registry web hook
5. Based on step 4., implement setting container registry web hooks and
  callbacks to deployments along solution decided for in step 3.
6. Write an example deployment upgrade script/configuration for Kubernetes or
  OpenShift that is triggered in response to an incoming callback implemented
  in step 5.

[project-overview]: ../README.md
[sem-ver]: <https://semver.org>
[topic-service-registry]: service_registry.md
[topics-overview]: ../README.md#topics
