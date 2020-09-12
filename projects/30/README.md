# Project 30: Epidemiology and monitoring ontology for COVID-19

## Abstract

Epidemiological data is necessary to monitor public health, and to assess the impact of disease outbreaks and efficacy of mitigating interventions. In the context of an infectious disease outbreak it is imperative to have these data as FAIR as possible to facilitate rapid analysis to support timely evidence-based decision making. During the past virtual BioHackathon-COVID-19 we evaluated the availability of some epidemiological quantitative indicators in OBO ontologies and detected that while between the [Statistics ontology](http://stato-ontology.org/) and Epidemiology Ontology (EPO) we have many of the usual concepts described, essential classes are entirely missing for capturing these different indicators with the precision required, and also definition reconciliation needs to be done. Furthermore, we noticed that EPO is not maintained since its publication and has been deprecated from OBO Foundry [1]. Another issue that may be improved is the current absence of axioms and definition patterns that relate epidemiology (i.e., observations of a population) to clinical ontologies (i.e., observations on an individual). A formal model is needed to describe epidemiological data for monitoring events such as COVID-19 disease  as well as to capture information related to other disease outbreaks and future epidemics. The goal of the proposed project is to identify and structure the missing concepts, extending current ontologies or making a unified model combining them into single ontology. This infrastructure would enable the biomedical community to provide machine-readable quantitative epidemiological data and make it easier for scientists to find and share it, and to link patient data to infectivity, transmissibility and outcomes of SARS-CoV-2 infection in humans. Ultimately, it will facilitate surveillance, research, and policy-making in pandemics like COVID-19.


#### References

[1] Pesquita et al. The epidemiology ontology: an ontology for the semantic annotation of epidemiological resources, J Biomed Semantics. 2014; 5: 4. doi: [10.1186/2041-1480-5-4](10.1186/2041-1480-5-4)

### Goals

## Topics

* Covid-19
* Data Platform
* Federated Human Data
* Interoperability Platform

**Project Number:** 30



**EasyChair Number:** 49

## Team

### Lead(s)

 Núria Queralt-Rosinach [ n.queralt_rosinach@lumc.nl ], 
 Robert Hoehndorf [ robert.hoehndorf@kaust.edu.sa ], 
 Paul N. Schofield [ pns12@hermes.cam.ac.uk ], 
 Philippe Rocca-Serra [ philippe.rocca-serra@oerc.ox.ac.uk ]
 Rajaram Kaliyaperumal [ R.Kaliyaperumal@lumc.nl ]

### Nominated participant(s)

 Núria Queralt-Rosinach [ n.queralt_rosinach@lumc.nl ],
 Rajaram Kaliyaperumal [ R.Kaliyaperumal@lumc.nl ]

## Expected outcomes

Expected outcomes and prioritization: First to develop an epidemiology information model in OBO focused on quantitative indicators; Incorporate this model in an existing resource for the community.
 
 From the first list of epidemiological quantitative terms analyzed, our plan is to: 1) add new COVID-19 relevant content through manual extraction from publications in medrXiv and or case report forms 2) try to map these to existing OBO ontologies 3) refine the list of terms with epidemiologists 4) define and implement axiom patterns 5) contact ontology stakeholders to define what is missing and either to ask for extensions to existing ontologies or to build a new, logically well-formed, and accurate ontology in OBO. We plan to perform two rounds of work, a first round to focus on quantitative indicators and a second round to expand to other indicators such as [WHO indicators](https://www.who.int/healthinfo/indicators/2015/metadata/en/).

## Expected audience

Curators, epidemiologists, ontologists, biomedical scientists, FAIRData experts.

**Number of expected hacking days**: 4 days

