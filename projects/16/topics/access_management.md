# Resource Access Management

[&#8629; All topics][topics-overview]

Services in the ELIXIR Cloud that may potentially give access to sensitive data
(particularly [GA4GH Data Repository Service (DRS)][ga4gh-drs] implementations)
or those that consume a non-trivial amount of compute resources (particularly
[GA4GH Task Execution Service (TES)][ga4gh-tes]) need some means of restricting
which user can access which resource.

The [GA4GH Passport][ga4hg-passport] specification provides a [JSON Web Token
(JWT)][jwt] scope that can store claims (also referred to as _visas_) that can
be used to check with data custodians whether the bearer of a token should be
granted access to a particular resource. As this process is so far only
well defined for giving access to data sets, i.e., the structure of the visas
for this purpose is specified and the necessary service calls required to
ascertain a token bearers privileges are outlined, this topic will focus on
implementing GA4GH Passport visa-based resource access management for DRS
services.

In ELIXIR Cloud, we are developing/maintaing two DRS implementations,
[RDSDS][rdsds] and [DRS-Filer][drs-filer], but since the former is externally
developed at the EBI, we should rather focus on implementing resource access
management in DRS-Filer. However, this requires to first enable general token
validation in the [FOCA][foca] package.

Tentative outline of the topic:

1. Refactor token validation in FOCA to replace the security decorator with
  such that it is compatible with [Connexion 2.0+][connexion] [security handling][connexion-security]
2. Create a service call schema for retrieving and validating visas.
3. Update the DRS-Filer object registration model to allow provision of
  required schemas for a given object.
4. Implement service call schema developed in step 2.

[connexion]: <https://github.com/zalando/connexion>
[connexion-security]: <https://connexion.readthedocs.io/en/latest/security.html>
[drs-filer]: <https://github.com/elixir-cloud-aai/drs-filer>
[foca]: <https://github.com/elixir-cloud-aai/foca>
[ga4gh-drs]: <https://github.com/ga4gh/data-repository-service-schemas>
[ga4gh-tes]: <https://github.com/ga4gh/task-execution-schemas>
[ga4gh-passport]: <https://github.com/ga4gh-duri/ga4gh-duri.github.io/blob/master/researcher_ids/ga4gh_passport_v1.md#passport>
[jwt]: <https://jwt.io/>
[rdsds]: <https://github.com/EMBL-EBI-TSI/RDSDS>
[topics-overview]: ../README.md#topics
