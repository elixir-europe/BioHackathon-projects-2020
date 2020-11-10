# FAIR Service Registry

[&#8629; All topics][topics-overview]

Currently, available deployments for each service in the ELIXIR Cloud is listed
on [GitHub][cloud-resources], but the process is tedious and entries are
hopelessly outdated.

To improve on that experience, the GA4GH has a [Service Registry API
specification][ga4gh-registry] that we would like to implement and centrally
deploy for the ELIXIR Cloud. Apart from simple accounting, there are several
use cases for such a registry, as several services (e.g., the
[web portal][cwlab] to find which WES and TRS deployments are out there, or the
[task distribution logic][testribute] to find out which TES deployments are
available) would benefit from retrieving a list of live services on the fly.

The API specs for the ELIXIR Cloud registry ([dedicated repo][cloud-registry]
in the making) could also be extended for use cases that are specific to the
ELIXIR Cloud project, such as the pub/sub-based, decoupled [CI/CD
strategy][ci-cd].

Tentative list of work packages for this subproject:

* Desing schema(s) for `POST` and `PUT` endpoints for registering deployments
  for GA4GH implementations with the ELIXIR Cloud
* Implement `POST`/`PUT` endpoint(s)
* Implement `GET` endpoints
* Deploy service

[ci-cd]: ci_cd.md
[cloud-registry]: <https://github.com/elixir-cloud-aai/cloud-registry>
[cloud-resources]: <https://github.com/elixir-cloud-aai/elixir-cloud-aai/blob/dev/resources/resources.md>
[cwlab]: <https://github.com/CompEpigen/CWLab>
[ga4gh-registry]: <https://github.com/ga4gh-discovery/ga4gh-service-info>
[resources]: <https://github.com/elixir-cloud-aai/elixir-cloud-aai/blob/dev/resources/resources.md>
[testribute]: <https://github.com/ga4gh-discovery/ga4gh-service-info>
[topics-overview]: ../README.md#topics
