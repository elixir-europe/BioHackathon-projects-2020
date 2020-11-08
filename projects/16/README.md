# Project 16: The ELIXIR Cloud

![logo-banner][logo-banner]

_The **ELIXIR Cloud** brings analysis to the data_ through a community
standards-powered, international and highly interoperable cloud computing
network.

For more background, please see the [dedicated section](#background) or check
out the poster or presentation below:

| Poster | Presentation |
| --- | --- |
| [![thumb_poster][thumb_poster]][poster] | [![thumb_presentation][thumb_presentation]][presentation] |

## Topics

> _Have a pick or BYO!_

Depending on your background, skill set and other team members, possible areas
to work on for the BH20 hackathon include:

* Implement a [**FAIR service registry**][topic-service-registry]
* Design and implement a pub/sub [**CI/CD strategy**][topic-ci-cd]
* Run [**CWL conformance tests**][cwl-tests]
* Implement [**resource access management**][topic-access-management] for data
  and compute
* Implement routines for [**refreshing authorization
  tokens**][topic-token-refreshal]
* Conduct [**interoperability tests**][topic-interoperability] with other GA4GH
  Cloud implementations and portals
* Address [**open issues**][project-board] for any ELIXIR Cloud
  repository

If you have any other ideas, we are very happy to hear them! :)

Here are some topics for inspiration:

* Design a real-world use case showcasing the power of federated data analysis
  Cloud implementations and portals
* Write FAIR documentation for end users, developers and/or system admins
* Implement and/or improve deployment recipes for existing services
* Design and implement for the entire service stack

## Join the team

> _The more, the merrier!_

### Audience

A wide range of contributors with diverse backgrounds and skill sets is needed
to make the ELIXIR Cloud a success! From planning to coordinating to
implementing to promoting to testing to adopting - many tasks, small and big,
are available for **YOUR** specific background, during or after the hackathon.

Some of the more obvious keywords, audiences and skill sets that fit well with
the project and the hackathon goals are listed below, but please don't let it
discourage you from reaching out if your specific role or skill set is not
listed!

#### Keywords

* **Compute Platform** / Data Platform / Tools Platform / Interoperability
  Platform
* GA4GH partnership, EOSC-life, Containers
* Federated Human Data / Human Copy Number Variation / Marine Metagenomics /
  Rare Disease

#### Backgrounds

* Development
* Devops
* Tool/worfklow development
* Bioinformatics
* Security / AAI

#### Some useful skills

* Microservices, REST/HTTP APIs, OpenAPI, Python, Flask, Java, Spring Boot
* Miocro-frontends, web components, React
* Containers, Kubernetes, OpenShift
* CI/CD
* OIDC, OAuth2, JWT
* FAIR, documentation, rST, markdown, writing, outreach, training

### Where to start

1. Please join our project channel `#16_ga4ghcloud` on the official BH20 Slack
  space:  
  [![Chat][badge-chat-bh20]][chat-bh20]

2. Please let us know your GitHub handle. You are also
  encouraged to add your name, email address, ORCID &  GitHub handle to the
  [team](#team) section.

3. Please also have a look at our [contribution
  guidelines][contributing-guidelines] designed to make it easy for everyone to
  work together.

4. Importantly, please mind and abide by hackathon's [Code of
  Conduct][coc-bh20], as well as [ours][coc-elixir-cloud], to make sure
  everyone feels welcome and appreciated.

5. Let us know what [topic(s)](#topics) you would like to work on, and we will
  try to assemble a subteam and distribute issues. Alternatively, pick one or
  more issues from the common [project board][project-board] and assign
  yourself.

**_Start hacking! :)_**

## Team

> _United we stand, divided we fall!_

* [Alex Kanitz](alexander.kanitz@unibas.ch)
  (**co-lead**;
  [GitHub](https://github.com/uniqueg),
  [ORCID](https://orcid.org/0000-0002-3468-0652)) <corresponding author>
* [Jonathan Tedds](jonathan.tedds@elixir-europe.org)
  (**co-lead**;
  [GitHub](https://github.com/jtedds),
  [ORCID](https://orcid.org/0000-0003-2829-4584))
* [Michael R. Crusoe](mrc@commonwl.org)
  ([GitHub](https://github.com/mr-c),
  [ORCID](https://orcid.org/0000-0002-2961-9670))
* Marius Dieckmann
  ([GitHub](https://github.com/mariusdieckmann))

## Stay involved

> _Haven't had enough?_

Regardless of whether you have contributed to the project during the hackathon
or you hacked for one or more of the other amazing projects: if you are
interested in the ELIXIR Cloud, **_the ELIXIR Cloud is interesting in YOU!_**

Please have a look [here][contributing] for some more info and reach out to us,
e.g., through our Slack space:

[![Chat][badge-chat-elixir-cloud]][chat-elixir-cloud]

## Background

> _What's practice without theory?!_

### The ELIXIR Cloud & AAI Ecosystem

Championed by the [ELIXIR Compute Platform][elixir-compute], the [**ELIXIR
Cloud & AAI Ecosystem**][elixir-cloud] is a cross-platform effort within the
ELIXIR universe, and is a [Driver Project][ga4gh-drivers] of the [Global
Alliance for Genomics and Health (GA4GH)][ga4gh]. We are aligning with
international partners to deliver cloud-based population-scale genomic and
phenotypic data analysis to the biomedical research and healthcare community.

### The ELIXIR Cloud

The exponential increase in the amounts of data generated in the biomedical
sector as well as the vast computational resources required to analyse and
integrate them, present veritable barriers to the advancement of the biomedical
sciences. The sensitivity of health-related data further requires sophisticated
security measures to be put in place, which are difficult to implement and
maintain in a world of fragmented IT infrastructure as is typically found
across hospitals, research centers and industry. 

To help overcome these obstacles, the [Global Alliance for Genomics and Health
(GA4GH)][ga4gh], an internationally backed standard-setting organization
bringing together opinion leaders in academia and industry, has proposed a set
of _Cloud API specifications_ for enabling the adoption of [FAIR
principles][fair] for data, workflows and infrastructure. Based on these
specifications, the [ELIXIR Cloud & AAI][elixir-cloud] ecosystem is developing
the ELIXIR Cloud, a highly interoperable, federated cloud computing environment
that will allow authenticated users to execute language-agnostic large-scale
data analysis workflows across participating nodes.

To this end, we develop guidelines for consistent OAuth2-based authentication
and authorization regimes, implementations for each of the four [GA4GH
Cloud][ga4gh-cloud] standards, tools and services to enable federation at the
workflow and task level, as well as client applications that operationalise the
ELIXIR Cloud to end users.

**Incremental rollout of the ELIXIR Cloud to end users is planned to commence
in 2021.**

![vision][vision]

**Vision of an interoperable GA4GH-powered Cloud.** Each box represents a
cloud-native microservice or collection of microservices that can be readily
deployed on different infrastructures at, e.g., research institutes, compute
centers, hospitals or companies, and added to the network.

## Numbers

> _In case you were wondering..._

* **Number of expected hacking days**: 365 / year :)
* **Project Number:** 16
* **EasyChair Number:** 25

[badge-chat-bh20]: <https://img.shields.io/static/v1?label=chat&labelColor=00366a&message=bh20&color=a50044>
[badge-chat-elixir-cloud]: <https://img.shields.io/static/v1?label=chat&labelColor=ffcb00&message=ELIXIR%20Cloud&color=f95b45>
[chat-bh20]: <https://join.slack.com/t/biohackeu20/shared_invite/zt-i9i156if-L1H_6gLKK181NDPSe3fwkQ>
[chat-elixir-cloud]: <https://join.slack.com/t/elixir-cloud/shared_invite/enQtNzA3NTQ5Mzg2NjQ3LTZjZGI1OGQ5ZTRiOTRkY2ExMGUxNmQyODAxMDdjM2EyZDQ1YWM0ZGFjOTJhNzg5NjE0YmJiZTZhZDVhOWE4MWM>
[coc-bh20]: <https://elixir-europe.org/events/code-of-conduct>
[coc-elixir-cloud]: <https://github.com/elixir-cloud-aai/elixir-cloud-aai/blob/dev/CODE_OF_CONDUCT.md>
[contributing]: <https://github.com/elixir-cloud-aai/elixir-cloud-aai/blob/dev/CONTRIBUTING.md>
[contributing-guidelines]: <https://github.com/elixir-cloud-aai/elixir-cloud-aai/blob/dev/resources/contributing_guidelines.md>
[cwl-tests]: topics/cwl_conformance_tests.md
[elixir-cloud]: <https://github.com/elixir-cloud-aai/elixir-cloud-aai>
[elixir-compute]: <https://elixir-europe.org/platforms/compute>
[fair]: <https://www.go-fair.org/>
[ga4gh]: <https://ga4gh.org/>
[ga4gh-cloud]: <https://www.ga4gh.org/work_stream/cloud/>
[ga4gh-drivers]: <https://www.ga4gh.org/how-we-work/driver-projects/>
[logo-banner]: images/logo-banner.png
[poster]: <https://drive.google.com/file/d/1f23CfP1tjNJfuPXi20siKMFffO8dj4GO>
[presentation]: <https://drive.google.com/file/d/16QR0UHVMLfhIU85H2Ii0QPhWr6TpRkuN>
[project-board]: <https://github.com/orgs/elixir-cloud-aai/projects/4>
[thumb_poster]: images/thumb_poster.png
[thumb_presentation]: images/thumb_presentation.png
[topic-access-management]: topics/access_management.md
[topic-ci-cd]: topics/ci_cd.md
[topic-interoperability]: topics/interoperability.md
[topic-service-registry]: topics/service_registry.md
[topic-token-refreshal]: topics/token_refreshal.md
[topic-use-case]: topics/use_case.md
[vision]: images/vision_interoperability.png
