# Project 24: Exploiting Bioschemas Markup in Community Registries

## Abstract

Bioschemas has the potential to automate the collection of content from the long-tail of scientific resources for community registries such as FAIRDARE for the plant community or Orphanet for the Rare Disease community. This can be achieved by scraping structured markup from the web resources and depositing it with the community registry. This provides a single mechanism to collect data from hundreds of sources with minimal effort from the resource provider; they only need to maintain a website in which schema markup is embedded. However, it requires the registry provider to be able to scrape content from the web and exploit this in their catalogue.

In this hackathon, we will work with the registry providers from the ELIXIR Bioschemas Strategic Implementation Study community resources, Orphanet, FAIRDARE, and IDPCentral, together with other registry providers, e.g. bio.tools, PubChem, FAIRsharing, etc. We will exploit existing markup deployed through earlier hackathon activities – there are currently 80 resources known to deploy Bioschemas markup on over 11 million web pages (https://bioschemas.org/liveDeploys/ – March 2020) – together with the BMUSE scraper (https://app.swaggerhub.com/apis/kcmcleod/Scraper/) to scrape structured markup for the different resource registries.

## Topics

- Bioschemas
- Interoperability Platform
- Intrinsically Disordered Community
- Plant Sciences
- Rare Disease

**Project Number:** 24



**EasyChair Number:** 38

## Team

### Lead(s)

Alasdair Gray A.J.G.Gray@hw.ac.uk

### Nominated participant(s)

- Petros Papadopoulos <p.papadopoulos@hw.ac.uk>
- Ivan Micetic <ivan.micetic@unipd.it>

## Expected outcomes

Bioschemas markup crawled
 Markup fed into community aggregators
 Markup improving search results

## Expected audience

Community registry providers
 - FAIRDARE: Cyril Pommier
 - IDPCentral: Ivan Micetic, Andras Hatos
 - Orphanet: Marc Hanauer, David Lagorce, Céline Rousselot
 
 Scraper expertise: Petros Papadopoulos

**Number of expected hacking days**: 4

# Hacking Plan

## Day 1 Monday

### IDPCentral

Aim to scrape data from 3 IDP sources and interlink into a prototype IDPCentral registry. Data will be merged based on their UniProt accession number.

Data model for the merged data will be based around the Bioschemas [Protein](https://bioschemas.org/profiles/Protein) and [SequenceAnnotation](https://bioschemas.org/SequenceAnnotation) models. Each statement in the model will have provenance data tracked using a similar model to Wikidata. The data model will also allow for the multiplicity of data coming from multiple sources but being slightly different.

Tasks:
- Ivan to understand why BMUSE is not pulling all pages
- Petros to work on fixes for BMUSE
- Andras to develop UI over a mongo data store that would contain the data according to the above model.
- Alasdair to work on a conversion script to transform the page centric scraped data into the Bioschemas Knowledge Graph

### Dundee Microscopy Database

Josh will work on embedding markup within the database and checking that it can be crawled using BMUSE.

the database contains a lot of cross links to ELIXIR resources and would be useful for enabling links to visual evidence for a concept.

Tasks:
- Embed markup in a page and deploy on S3
- Create test sitemap
- Test BMUSE can scrape deployed content.
