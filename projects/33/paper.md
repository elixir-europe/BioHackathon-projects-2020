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
    orcid: 0000-0002-6267-7258
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
 - name: Natural History Museum, University of Oslo, Sars Gate 1, 0562, Oslo, Norway
   index: 2
 - name: Naturalis Biodiversity Center, Darwinweg 2, 2333 CR Leiden, Netherlands
   index: 3
 - name: Cardiff University, Cardiff CF10 3AT, United Kingdom
   index: 4
 - name: University of Vienna, Universitätsring 1, 1010 Vienna, Austria
   index: 5   
date: 11 November 2020
bibliography: paper.bib
---

# 1. Introduction or Background

Add to this section a couple of paragraphs introducing the work done during the BioHackathon, CodeFest, VoCamp or Sprint event. Please add references whenever needed, for instance [@Katayama:2010].

When DNA is sequenced from an organism, it is best practice to create voucher specimens [@PLEIJEL2008369; @10.1111/jai.12568]. This ensures that the results are repeatable and that the identification of the organism can be verified. It also means that other information, that perhaps do not fit within the data model for sequences, can still be made available, linked to the specimen. Molecular sequence vouchers are often kept in herbaria and museums where they are curated and stored for the long-term. Similarly, DNA is also extracted from specimens having been collected and stored in collections some time ago. In both cases, it is important both to be able to know all the sequences extracted from a specimen and find the specimen from which the sequences have been extracted. Yet currently, connecting specimens to sequences is difficult without considerable manual detective work. To a researcher with expertise, specimens are identifiable by the details of the collection event, such as date, location, collector, collector number and taxonomic name. But they may also be referenced by accession numbers. However, these fields are mostly unformatted text strings in a database record and there is little-to-no consistency between these data in specimen and sequence databases.

Still, the situation does not have to be this way. Databases of the [International Nucleotide Sequence Database Collaboration](http://www.insdc.org/) (INSDC), such as the [European Nucleotide Archive (ENA)](https://www.ebi.ac.uk/ena/browser/home), have unique identifiers for sequences, as do many specimens [@10.1093/database/bax003]. It would be possible to create bidirectional links to connect these data permanently and in a machine readable way. Ideally, this would be done when these database entries are created, but this will require changes to the data standards, databases and procedural change by researchers, collections and their institutions. Yet, even if we can resolve the challenges of future data, there still remains a large legacy of unconnected sequences that need connecting to their vouchers.

At the Biohackathon we attempted to build a semi-automated workflow that would take specimen data from the Meise Herbarium and search for references to those same specimens in a DNA sequence database. We took advantage of matching elements of the specimen and sequence data, such as date, location, collector, collector number and taxonomic name. As these data are not necessarily in the same format, we experimented with ways to match these data indirectly.

 Our aims for the hackathon are…

To make recommendations on how specimen and sequence databases should be connected in the future.
To analysis of the types of data available in databases suitable for linking specimens to sequences.
To create scripts to match existing data and evaluate how success we are.

Ultimately, these outcomes will help any collection connect its data better and will support the Elixir (https://elixir-europe.org/) goals of improving human and machine readable access to all data in the biological sciences.
## Methodological Approach
[European Nucleotide Archive (ENA)](https://www.ebi.ac.uk/ena/browser/home) and other sequence databases follow standards such as [Minimum Information about any (x) Sequence (MIxS)](https://gensc.org/mixs/) created by the Genomic Standards Consortium. Specimens databases generally follow the standards, Darwin Core ([@10.1371/journal.pone.0029715]) or ABCD ([@10.1080/11263504.2012.740085]). These standards define terms for the data that describe the sequence or specimen and their origins. However, many of these terms require only free text content and the terms do not necessarily map interoperably between standards. Our approach is to discover ways to connect related elements of these data standards to identify the associated sequences and specimens.

For example, our [herbarium)[https://www.plantentuinmeise.be/en/] has been working towards connecting all the people associated with specimens, such as collectors and identifiers, to stable identifiers, such as [ORCID](https://orcid.org/) IDs. If we are able to match person names on sequences to stable identities, such as [ORCID](https://orcid.org/) IDs, we can narrow the search of specimens and sequence considerably. We can also make use of the power of [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page) as a broker of person identifiers, so that if we have one identifier in one database, we can use Wikidata to find other identifiers and use the full suite of identifiers to search the other database.

![Schema of the workflow](data/workflowschema.jpg "Schema of the workflow")

Figure 1. A diagram of the connections between sequence databases (e.g. ENA) and specimens (GBIF). Sequences and specimens are often cited in literature and biological databases. These can be used as a source of accession numbers, locations, dates, person names and taxa with which sequence and specimen data can be linked. Wikidata can be used as a broker to link identifier schemes, such as taxon IDs. Even though candidate matches between sequences and specimens can be found uncertainty often remains. Therefore, we have foreseen a human verification step to confirm matches before the results are stored as a digital object that combines the results.
# 2. Methods
## 2.1. Finding candidate sequences

### 2.1.1

Access to sequence data Queries were made to the [ENA portal API](https://www.ebi.ac.uk/ena/portal/api/) attempting to select sequence records potentially related to voucher specimens from the herbarium collection of [Meise Botanic Garden](https://www.botanicalcollections.be/#/en/home) (MeiseBG). ENA also contains data on samples that sequences have been derived from, however, similar searches to those conducted on sequences resulted in far fewer results. Most sequences appeared unassociated with samples. We focused on the `specimen_voucher` data field, as other fields like `description` threw many false positives with our querying approach and rarely contained indicators of interest. All query work was done in R, a script called bh-apicalls.R available in this repository.

Different query approaches were tried. Initially, multiple queries were specified combining wild cards (*) and common terms associated with MeiseBG. The query values are listed below:

`*br)*`

`*br:*`

`*br<*`

`*br-*`

`*meise*`

`*gard.*belg*`

These values mostly use MeiseBG’s Index Herbariorum code `BR`, adding punctuation characters to omit false-positives as the queries are not case sensitive. The ENA portal API also does not support regular expressions. To work around this, a query was made for the more generic `*b*` (i.e. all sequences with a b in their specimen_voucher field). A more generic any value query for this field (i.e. `*`) was attempted, but came with performance issues (both at the API response and the local memory side) and was thus abandoned. The exported results from this general “*b*” query were then mined using more specific regular expressions, including (other than those previously listed):

`br[0-9]{13}`

`br [0-9]{13}`

These fit the pattern of MeiseBG specimen barcodes, which are used as catalogue numbers. Regular expressions were also used to eliminate some false-positives, in particular acronyms that contained BR but were not limited to it and hence contained other upper case characters (i.e. using negative grep for `[A-Z]BR`). Records including ‘Meisenburg’, a partial homonym to ‘Meise’, were also removed in this step.

## 2.2. Mining the results for specimen properties

Both approaches yielded an eventual result of ca. 8,398 sequences and 5,920 after eliminating false-positives with the method described previously (see script bh-cleanup.R). For all of these results, an attempt was made to identify within the `specimen_voucher` string collection numbers and collector names.

The recommended format for `specimen voucher` is `institutionCode:collectionCode:id`, but in practice this format is only rarely used. More often, beyond a reference to the institution as described above (i.e. BR or Meise), the specimen is only described through a combination of the name(s) of the person(s) who collected it and a numeric identifier. This (alpha)numeric identifier can be the so-called `collection number`, which is often given to a botanical specimen during the collection event or shortly after it, to differentiate it from other specimens collected by the same individuals on the same date. The numeric identifier may also be the unique accession number which physically disambiguates the specimen from all others in the collection. It is not uncommon for the physical identifier to be only partially present in the `specimen voucher` field, e.g. for the nonnumeric part to be omitted or for numbers to be dropped, in particular leading zeroes. It is also not uncommon for multiple numeric identifiers to be present in the `specimen voucher` field.

To match the numeric identifiers found on ENA sequences to numbers known for Meise’s herbarium specimens, the numbers were extracted by splitting the `specimen voucher` string into space-separated substrings. Out of each substring that contained at least one number, the numeric elements were extracted to avoid ambiguity through punctuation. For example, a `specimen voucher` value of `De Block 6 (BR)(Meise 77-0360)` would result in two substrings of `6` and `770360`.

To match person names, the last names of persons listed in MeiseBG’s list of known collectors were matched into the whole `specimen voucher` string. Any positive match was accepted and the PIDs associated with that record in the collector list were added to the ENA sequence record.

Finally, the ENA provided `tax_id` - an NCBI taxon id - was matched to a GBIF backbone taxon ID using Wikidata as a broker. This was done using a series of SPARQL queries. This way, the taxon names for ENA sequences could be unambiguously compared to taxon names for specimens in GBIF.

## 2.3. Matching to specimen data

Subsequently, a matching process was set up, where a positive link between a specimen published to GBIF and an ENA sequence was withheld if there was a match between all of the following: 

taxon ID on ENA and taxonKey on GBIF
one of the numeric elements on ENA and the numeric element of recordNumber on GBIF
one of the PIDs connected to the ENA record and recordedByID on GBIF. 

The matching was performed locally using the GBIF-generated occurrence file of the Meise Botanic Garden Herbarium dataset (https://doi.org/10.15468/wrthhx). This way, API overhead was avoided and manipulations such as extracting only numeric elements was possible.

Through this process, 2.504 ENA sequences were connected to at least one GBIF record. This approach only looked at herbarium specimens on GBIF. Further work should be done to look into living accessions and unpublished specimens. A particular class is preserved specimens collected from accessions in the Garden. These are not published as they do not fit very well into the Darwin Core standard, given that they have two gathering events: the original gathering indicating its provenance and the secondary gathering from the area where it was cultivated.

The ENA sequences and their candidate voucher specimens on GBIF as suggested through the matching process can be manually vetted using a Django app that was developed during the Biohackathon. The matches can be imported in a JSON format, as can additional metadata from both ENA and GBIF to better inform the user. In the future, the Django app should also include functionality to allow for the export of validated matches. This export can subsequently be used to annotate the GBIF records with their correct ENA sequence, or vice versa. Validated matches can also be made available through an update operation of a digital object representing the Meise specimens, adding links to ENA sequences when positively matched. 



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


