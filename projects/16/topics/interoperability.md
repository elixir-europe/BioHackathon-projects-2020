# Interoperability Tests

[&#8629; All topics][topics-overview]

One of the major design ideas for the [GA4GH Cloud][ga4gh-cloud] suite of APIs
is that they allow developers to implement microservices that do one thing
well. This focus on modularity further allows different implementations of
the APIs to interoperate via the defined schemas.

To realize ELIXIR Cloud's [vision][vision] of a network that is able to run
(almost) every workflow on (almost) any data and (almost) any compute
infrastructure, we need to validate that different GA4GH Cloud implementations
can indeed interoperate.

For convenience, here is a list of the GA4GH Cloud API standards with links
to the corresponding repositories:

* [Tool Registry Service (TRS)][ga4gh-trs]
* [Data Repository Service (TRS)][ga4gh-drs]
* [Workflow Execution Service (WES)][ga4gh-wes]
* [Task Execution Service (TES)][ga4gh-tes]

In this subproject, the following work packages could be worked on:

* Add or extend tests in our [interoperability tests][interop-tests]
  repository.
* Create a list of known GA4GH implementations and deployments/instances for
  each API standard.
* Create a 4-dimensional interoperability matrix covering all theoretical
  combinations of services.  
  Note that not all WES implementations make use of TES, so in these cases
  there will be only 3 dimensions.
* Create code to systematically generate, execute or interpret tests across
  vectors in the interoperability matrix.
* Find solutions on how we can store (and retrieve) test cases, test results
  and documentation for each vector in the interoperability matrix
  conveniently?

[ga4gh-cloud]: <https://www.ga4gh.org/work_stream/cloud/>
[ga4gh-drs]: <https://github.com/ga4gh/data-repository-service-schemas>
[ga4gh-tes]: <https://github.com/ga4gh/task-execution-schemas>
[ga4gh-trs]: <https://github.com/ga4gh/tool-registry-service-schemas>
[ga4gh-wes]: <https://github.com/ga4gh/workflow-execution-service-schemas>
[interop-tests]: <https://github.com/elixir-cloud-aai/interop-tests>
[topics-overview]: ../README.md#topics
[vision]: ../README.md#the-elixir-cloud
