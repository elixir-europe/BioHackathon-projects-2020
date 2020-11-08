# Project 12: “Federated” query by agents

[OVERVIEW Google Slide Deck](https://docs.google.com/presentation/d/1SKxtUceSBcfwzozCJn0HN4jqHLtO1c8_TaF5ZqrtzCY/edit?usp=sharing)

### SPARQL Endpoints:

http://ldp.cbgp.upm.es:8890/sparql

<code><pre>
     PREFIX efo: <http://www.ebi.ac.uk/efo/efo.owl#>
     PREFIX sio: <http://semanticscience.org/resource/>
     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
     select *
     where {
      ?inf a efo:EFO_0001067
      ?inf sio:has-participant ?p .
     }
</pre></code>

http://fairdata.systems:8990/sparql  (yes, 8990!  Not the default for virtuoso!)

<code><pre>

PREFIX efo: <http://www.ebi.ac.uk/efo/efo.owl#>
PREFIX sio: <http://semanticscience.org/resource/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
select *
where {
       ?p a sio:pathogen .
       ?p sio:has-identifier ?id .
}
</pre></code>

## Abstract

The European Joint Programme on Rare Diseases (EJP-RD) is building an interoperability platform for registries and biobanks for rare diseases. RD registries are diverse in size, content, and form, and are widely dispersed throughout Europe, including several hundred small single-disease-focused registries being run by non-technical experts. Notably, this is among the most sensitive of all data, in particular because the rarity of the diseases make personal identification much easier to achieve with fewer data points. The EJP-RD technical platform consists of data entry/transformation tools, ...

## Topics

Containers
 Data Platform
 Federated Human Data
 GA4GH partnership
 Interoperability Platform
 Rare Disease

**Project Number:** 12



**EasyChair Number:** 19

## Team

### Lead(s)

Mark D Wilkinson (mark.wilkinson@upm.es)

### Nominated participant(s)

Mark D Wilkinson
 Pablo Alarcon

## Expected outcomes

Expected outcomes: Some of the strategy for achieving the goals has been planned within other similar projects, such as the Personal Health Train and Farm Data Train (where several of the Hackathon participants are involved in those projects). As such, we can anticipate having a working strawman prototype by the end of four days. This will then be evaluated (post-hackathon) by the other members of the technical architecture team of EJP, as well as by these peer communities, with the aim of reaching a final architecture proposal with at least one reference implementation, to put forward to the public by early 2021.

## Expected audience

Coders in Ruby or Python; experience with Linked Data, SPARQL, Docker, and ontologies; good grasp of HTTP Protocols.

**Number of expected hacking days**: 4

