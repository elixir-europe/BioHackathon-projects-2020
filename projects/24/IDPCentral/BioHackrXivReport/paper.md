---
title: 'Exploiting Bioschemas Markup to Populate IDPCentral'
tags:
  - Bioschemas
  - Intrinsically Disordered Proteins
authors:
  - name: Alasdair Gray
    orcid: 0000-0002-5711-4872
    affiliation: 1
  - name: Petros Papadopoulos
    orcid: 0000-0002-8110-7576
    affiliation: 1
  - name: Ivan Mičetić
    orcid: 0000-0003-1691-8425
    affiliation: 2
  - name: Andras Hatos
    orcid: 0000-0001-9224-9820
    affiliation: 2
affiliations:
 - name: Heriot-Watt University, Edinburgh, UK
   index: 1
 - name: University of Padua, Padua, Italy
   index: 2
date: 19 May 2021
bibliography: paper.bib
---

# Background

One of the goals of the ELIXIR Intrinsically Disordered Protein (IDP) [community](https://elixir-europe.org/communities/intrinsically-disordered-proteins) is create a registry called [IDPCentral](https://idpcentral.org/). The registry will aggregate the data contained in the community's specialist data sources such as [DisProt](https://disprot.org/) [@hatos_disprot_2020], [MobiDB](https://mobidb.bio.unipd.it/) [@piovesan_mobidb_2021], and [Protein Ensemble](https://proteinensemble.org/) [@lazar_ped_2021]. 

At the [ELIXIR BioHackathon-Europe 2020](https://elixir-europe.org/events/biohackathon-2020), we aimed to investigate the feasibility of populating IDPCentral using Bioschemas markup that has been deployed on the IDP community data sources. The benefit of using Bioschemas markup, which is embedded in the HTML web pages for each protein in the data source, is that a standard harvesting approach can be used for all data sources; rather than needing bespoke wrappers for each data source API. We expect to scrape the markup using the Bioschemas Markup Scraper and Extractor ([BMUSE](https://github.com/HW-SWeL/BMUSE)) tool that has been developed specifically to extract the markup embedded within web pages.

As well as populating the IDPCentral registry, we plan to consolidate the markup into a knowledge graph that can be queried to gain further insight into the IDPs. 

# Other main section on your manuscript level 1



# Discussion and/or Conclusion

We recommend to include some discussion or conclusion about your work. Feel free to modify the section title as it fits better to your manuscript.

# Future work

And maybe you want to add a sentence or two on how you plan to continue. Please keep reading to learn about citations and references.

For citations of references, we prefer the use of parenthesis, last name and year. If you use a citation manager, Elsevier – Harvard or American Psychological Association (APA) will work. If you are referencing web pages, software or so, please do so in the same way. Whenever possible, add authors and year. We have included a couple of citations along this document for you to get the idea. Please remember to always add DOI whenever available, if not possible, please provide alternative URLs. You will end up with an alphabetical order list by authors’ last name.

# Jupyter notebooks, GitHub repositories and data repositories

* Please add a list here
* Make sure you let us know which of these correspond to Jupyter notebooks. Although not supported yet, we plan to add features for them
* And remember, software and data need a license for them to be used by others, no license means no clear rules so nobody could legally use a non-licensed research object, whatever that object is

# Acknowledgements
Please always remember to acknowledge the BioHackathon, CodeFest, VoCamp, Sprint or similar where this work was (partially) developed.

# References

