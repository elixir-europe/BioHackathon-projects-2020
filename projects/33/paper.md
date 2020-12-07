---
title: 'Connecting molecular sequence to their voucher specimens'
tags:
  - Voucher Specimens
  - Collections
  - Herbarium
  - Museum
  - linking data
  - Accession numbers
authors:
  - name: Quentin Groom
    orcid: 0000-0002-0596-5376
    affiliation: 1
  - name: Mathias Dillen
    orcid: 0000-0002-3973-1252
    affiliation: 1
  - name: Pieter Huybrechts
    orcid: 0000-0002-6658-6062
    affiliation: 1
  - name: Rukaya Johaadien
    orcid: 0000-0002-2857-2276
    affiliation: 2
  - name: Niki Kyriakopoulou
    orcid: 
    affiliation: 3
  - name: Francisco Quevedo
    orcid: 0000-0002-8443-9832
    affiliation: 4
  - name: Maarten Trekels
    orcid: 0000-0001-8282-8765
    affiliation: 1
  - name: Wai Yee Wong
    orcid: 0000-0002-2329-2566
    affiliation: 5
affiliations:
 - name: Meise Botanic Garden, Nieuwelaan 38, 1860 Meise, Belgium
   index: 1
 - name: Institution 1, address, city, country
   index: 2
 - name: Institution 1, address, city, country
   index: 3
 - name: Institution 1, address, city, country
   index: 4
 - name: Institution 1, address, city, country
   index: 5   
date: 11 November 2020
bibliography: paper.bib
---

# 1. Introduction or Background

Add to this section a couple of paragraphs introducing the work done dring the BioHackathon, CodeFest, VoCamp or Sprint event. Please add references whenever needed, for instance [@Katayama:2010].

When sequencing DNA from an organism, it is standard practice to create voucher specimens [@PLEIJEL2008369; @10.1111/jai.12568]. This ensures that the results are repeatable and that the identification of the organism can be verified. It also means that other information, that perhaps do not fit within the data model for squaences can still be made available through the specimen. Moleculr sequence vouchers are often kept in herbaria and museums where they are curated and stored for the long-term. Similarly, DNA is also extracted from specimens having been collected some time ago. In both cases, it is important both to be able to know all the sequences extracted from a specimen and find the specimen from which the sequences have been extracted. Yet currently, connecting specimens to sequences is difficult without considerable manual detective work. To a researcher with expertise, specimens are identifiable by details of the collection event, such as date, location, collector, collector number and taxonomic name. But they may also be referenced by accession numbers. However, these fields are mostly just unformatted text strings in a database record and there is little-to-no consistency between these data in specimen and sequence databases.

Still, the situation does not have to be this way. Sequences in databases can have unique identifiers as do many specimens [@10.1093/database/bax003]. It would be possible to create bidirectional links to connect these data permanently and in a machine readable way. Ideally, this would be done when these database entries are created, but this will require changes to the data standards, databases and procedural change by researchers and their institutions. Yes, even if we can resolve the challenges of future data, there still remains a large lagacy of unconnected sequences that need connecting to their vouchers.

We propose to build a semi-automated workflow that will take specimen data from the Meise Herbarium and search for references to those same specimens in a DNA sequence database. This will be achieved by matching elements of the specimen and sequence data together, such as date, location, collector, collector number and taxonomic name. As none of these will be in the same format, we will need to find ways to match these data. For example, our herbarium has been working on connecting all its collectors to stable identifiers, such as ORCID IDs. If we are able to match person names on sequences to stable identities, such as ORCID IDs, we can narrow the search of specimens and sequence considerably. We can make use of the power of Wikidata as a broker of person identifiers, so that if we have one identifier in one database, we can use Wikidata to find other identifiers and use the full suite of identifiers to search the other database.

The outcome of the hackathon will be (1) recommendations on how specimen and sequence databases should be connected in the future (2) an analysis of the types of data available in databases suitable to find links and (3) the scripts implementing algorithms to match data. Ultimately, these outcomes will help any collection connect its data better and will support the Elixir goals of improving human and machine readable access to all data in the biological sciences.

# 2. Methodology

## 2.1. Finding candidate sequences

Queries were made to the ENA portal API attempting to collect sequence records which were potentially related to voucher specimens from the herbarium collection of Meise Botanic Garden (MeiseBG). Queries for samples were also tested, but these had very few results. Most sequences appeared unassociated with samples. We focused on the `specimen_voucher` data field, as others like `description` threw many false positives with our querying approach and rarely contained indicators of interest. All query work was done in R, a script called bh-apicalls.R available on github.

Different query approaches were tried. Initially, multiple queries were specified combining wild cards (*) and common terms associated with MeiseBG. The query values are listed below:

`*br)*`

`*br:*`

`*br<*`

`*br-*`

`*meise*`

`*gard.*belg*`

These values mostly utilize the common usage of MeiseBG’s Index Herbariorum code `BR`, adding punctuation characters to omit false positives as the queries are not case sensitive. The API also does not support regular expressions. To work around this, a query was made for the more generic `*b*` (i.e. all sequences with a b in their specimen_voucher field). A more generic any value query for this field (i.e. `*`) was attempted, but came with performance issues (both at the API response and the local memory side) and was thus abandoned. The results from this general “b” query were then mined using more specific regular expressions, including (other than those previously listed):

`br[0-9]{13}`

`br [0-9]{13}`

These fit the pattern of MeiseBG specimen barcodes, which are used as catalogue numbers. Regular expressions were also used to clear some false positives, in particular acronyms that contained BR but were not limited to it and hence contained other upper case characters (i.e. using negative grep for `[A-Z]BR`).

## 2.2. Mining the results for specimen properties

Both approaches yielded an eventual net result of ca. 8.398 sequences, 5.920 after throwing out some false positives. For all of these, an attempt was made to identify within the specimen_voucher string collection numbers and collector names. Also, separately the ENA provided `tax_id` - an NCBI taxon id - was matched to a GBIF backbone taxon ID using Wikidata as a broker. This was done using a series of SPARQL queries.

The collection numbers were extracted by splitting the specimen_voucher string into space-separated chunks. Out of each chunk containing at least one number, the numeric elements were extracted.

The collector names were identified by matching the last names of persons listed in MeiseBG’s collector table into the specimen_voucher string. Any positive result was withheld and the PIDs associated with that record in the collector table were added to the ENA sequence record.

## 2.3. Matching to specimen data

Subsequently, a matching process was set up, where a positive link between a specimen published to GBIF and an ENA sequence was withheld if there was a match between all of the following: 

taxon ID on ENA and taxonKey on GBIF
one of the numeric elements on ENA and the numeric element of recordNumber on GBIF
one of the PIDs connected to the ENA record and recordedByID on GBIF. 

The matching was performed locally using the GBIF-generated occurrence file of the Meise Botanic Garden Herbarium dataset (https://doi.org/10.15468/wrthhx). This way, API overhead was avoided and manipulations such as extracting only numeric elements was possible.

Through this process, 2.504 ENA sequences were connected to at least one GBIF record. This approach only looked at herbarium specimens on GBIF. Further work should be done to look into living accessions and unpublished specimens. A particular class is preserved specimens collected from accessions in the Garden. These are not published as they do not fit very well into the Darwin Core standard, given that they have two gathering events: the original gathering indicating its provenance and the secondary gathering from the area where it was cultivated.

The ENA sequences and their candidate voucher specimens on GBIF as suggested through the matching process can be manually vetted using a Django app that was developed during the Biohackathon. The matches can be imported in a JSON format, as can additional metadata from both ENA and GBIF to better inform the user.



Please separate paragraphs with a double line.

## Subsection level 2

Please keep sections to a maximum of three levels, even better if only two levels.

### Subsection level 3

Please keep sections to a maximum of three levels.

## Tables, figures and so on

Please remember to introduce tables (see Table 1) before they appear on the document. We recommend to center tables, formulas and figure but not the corresponding captions. Feel free to modify the table style as it better suits to your data.

Table 1
| Header 1 | Header 2 |
| -------- | -------- |
| item 1 | item 2 |
| item 3 | item 4 |

Remember to introduce figures (see Figure 1) before they appear on the document. 

![BioHackrXiv logo](./biohackrxiv.png)
 
Figure 1. A figure corresponding to the logo of our BioHackrXiv preprint.

# Other main section on your manuscript level 1

Feel free to use numbered lists or bullet points as you need.
* Item 1
* Item 2

# Discussion and/or Conclusion

We recommend to include some discussion or conclusion about your work. Feel free to modify the section title as it fits better to your manuscript.

# Future work

Reconnecting the links between objects and the data derived from them is inefficient, error prone and expensive. Indeed, if rigorous data management procedures were followed it would not be necessary. Considerable work needs to be done to improve scientific procedures, infrastructural standards and scientific data management culture. Much of the followup work that needs to be done is to make these changes, so that there will be no need to reconnect vouchers and their data in the future.

# Jupyter notebooks, GitHub repositories and data repositories

* Please add a list here
* Make sure you let us know which of these correspond to Jupyter notebooks. Although not supported yet, we plan to add features for them
* And remember, software and data need a license for them to be used by others, no license means no clear rules so nobody could legally use a non-licensed research object, whatever that object is

# Acknowledgements
The authors thank the organizers BioHackathon-Europe for their support and the smooth running of the event. QG, PH, MD, MT were supported by SYNTHESYS+ a Research and Innovation action funded under H2020-EU.1.4.1.2. Grant agreement ID: 823827 and by DiSSCo Prepare H2020-INFRADEV-2019-2020 – Grant Agreement No. 871043.

# References

Leave thise section blank, create a paper.bib with all your references.


