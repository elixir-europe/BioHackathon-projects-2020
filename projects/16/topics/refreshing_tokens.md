# Refreshing Authorization Tokens

[&#8629; All topics][topics-overview]

Within in the ELIXIR Cloud, different services are authorized by passing around
[JSON Web Tokens][jwt], originating from a client application, to each service.
However, as these access tokens are typically short-lived and may expire before
a workflow run is completed, there is a need to handle the refreshment of
expired tokens. The [ELIXIR Cloud AAI guidelines][aai-guidelines] propose a
design for the token flow within the ELIXIR Cloud that includes the refreshment
of tokens by clients that received a response that indicates that a token may
be expired. However, this functionality has not yet been implemented.

Tentative outline of work packages for this subproject:

1. Read the [ELIXIR Cloud AAI guidelines][aai-guidelines] to familiarize
  yourself with the proposed token flow required for refreshing tokens.
2. Design and implement a generic solution that can be integrated into various
  services that act as clients for other services and therefore must be able
  to handle token refreshment (e.g., [cwl-WES][cwl-wes]). The functionality
  could be added as utility to the [FOCA][foca] repository so that it can be
  easily imported and reused in any such service.

[aai-guidelines]: <https://github.com/elixir-cloud-aai/elixir-aai-guidelines>
[cwl-wes]: <https://github.com/elixir-cloud-aai/cwl-WES>
[foca]: <https://github.com/elixir-cloud-aai/foca>
[jwt]: <https://jwt.io/>
[topics-overview]: ../README.md#topics
