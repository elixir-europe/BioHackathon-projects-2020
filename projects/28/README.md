# Project 28: Beacon for clinical and translational data’

## Abstract

The Global Alliance for Genomics and Health (GA4GH) Beacon Project has shown its great potential in federated discovery of genomic data. It is originally implemented as a tool to share aggregated information (the “existence“) of Single Nucleotide Polymorphisms (SNP) in distributed genomic data collections. This has been later on extended to other types of genomic variants such as structural variants (the “Beacon+”). The ELIXIR team across several nodes has developed a reference implementation of the Beacon protocol.
 
The Beacon protocol has evolved towards more complex applications with increased functionality. The v2 extension of the Beacon protocol will allow the query for additional data beyond genome variants, using a proposed filters extension. Such filters (“Beacon v2 Filters“) are thought to be prefixed attributes, where the (public or private) prefix becomes the basis of scoping the value to the correct database value. This enables the possibility to implement the protocol to share aggregated information of data types such as clinical/phenotypic data and other OMICs data (e.g. transcriptomic data). 
 
In this biohackathon, we will focus on example implementation of “Beacon for clinical/phenotypic data” and “Beacon for transcriptomic data” using the above-mentioned extension. A set of APIs will be implemented to facilitate linking of local data collections of clinical/phenotypic data as well as other OMICs datatypes to the Beacon network.  Public data sources such as the TCGA (https://portal.gdc.cancer.gov/) and ICGC (https://dcc.icgc.org/) will be used to define the initial sets of filters as well as testing data. This will be a good opportunity to strengthen the community as well as consolidate cross-resource collaboration between different institutions to facilitate the standardised sharing of aggregated information, which in turn will enhance the “Findability” of datasets.

## Topics

Cancer
 Compute Platfrom
 Federated Human Data
 Rare Disease

**Project Number:** 28



**EasyChair Number:** 44

## Team

### Lead(s)

Dr. Venkata Satagopam venkata.satagopam@elixir-luxembourg.org (corresponding author)

Dr. Salvador Capella salvador.capella@bsc.es

Dr. Jordi Rambla De Argila jordi.rambla@crg.eu

Dr. Wei Gu wei.gu@elixir-luxembourg.org

### Nominated participant(s)

Dr. Tim Beck 
 UKRI Innovation Fellow at Health Data Research UK
 Email: timbeck@leicester.ac.uk
 

## Expected outcomes

We look forward to the development of:
 Example implementation of API to report the existence and summary statistics of clinical/phenotypic information.
 Example implementation of API to report the existence of transcriptomics data (as an example of other OMICs data types)
 A set of core filters (with ontology links) based on the test datasets (public) that could be extended in the future by the community.
 We are planning to submit a manuscript on Biohackathon outcome. Between the potential achievements, we could find an extended and lasting collaboration between institutions as well as scientific contributions, exploring the deployment of joint multi-institutional services.

## Expected audience

Bioinformaticians and developers working in the areas of API development, ontology, clinical and transcriptomics data processing/analysis.
  
 By all means, organisers commit to the proposal with the participation and contribution of Beacon experts, developers, bioinformaticians for the event to ensure the presence of enough human resources and provide momentum during the biohackathon. 3 people from the University of Luxembourg 2 from BSC and 3 from CRG will participate in this Biohackathon topic.

**Number of expected hacking days**: 4 days

