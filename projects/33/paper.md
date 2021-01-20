---
title: 'Connecting molecular sequences to their voucher specimens'
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

When DNA is sequenced from an organism, it is best practice to create voucher specimens [@PLEIJEL2008369; @10.1111/jai.12568]. This ensures that the results are repeatable and that the identification of the organism can be verified. It also means that other information, that perhaps do not fit within the data model for sequences, can still be made available, linked to the specimen. Molecular sequence vouchers are often kept in herbaria and museums where they are curated and stored for the long-term. Similarly, DNA is also extracted from specimens that have been collected and stored in collections, perhaps before sequencing technologies were even available. In both cases, it is important both to be able to know all the sequences extracted from a specimen and find the specimen from which the sequences have been extracted. Yet currently, connecting specimens to sequences is difficult without considerable manual detective work. To a researcher with expertise, specimens are identifiable by the details of the collection event, such as date, location, collector, collector number and taxonomic name. But they may also be referenced by accession numbers. However, these fields are mostly unformatted text strings in a database record and there is little-to-no consistency between these data in specimen and sequence databases.

Still, the situation does not have to be this way. Databases of the [International Nucleotide Sequence Database Collaboration](http://www.insdc.org/) (INSDC), such as the [European Nucleotide Archive (ENA)](https://www.ebi.ac.uk/ena/browser/home), have unique identifiers for sequences, as do many specimens [@10.1093/database/bax003]. It would be possible to create bidirectional links to connect these data permanently and in a machine readable way. Ideally, this would be done when these database entries are created, but this will require changes to the data standards, databases and procedural change by researchers, collections and their institutions. Yet, even if we can resolve the challenges of future data, there still remains a large legacy of unconnected sequences that need connecting to their vouchers.

At the Biohackathon we attempted to build a semi-automated workflow that would take specimen data from the Meise Herbarium and search for references to those same specimens in a DNA sequence database. We took advantage of matching elements of the specimen and sequence data, such as date, location, collector, collector number and taxonomic name. As these data are not necessarily in the same format, we experimented with ways to match these data indirectly.

 Our aims for the hackathon are…

To make recommendations on how specimen and sequence databases should be connected in the future.
To analyze the types of data available in databases suitable for linking specimens to sequences.
To create scripts to match existing data and evaluate how successful we are.

Ultimately, these outcomes will help any collection connect its data better and will support the Elixir (https://elixir-europe.org/) goals of improving human and machine readable access to all data in the biological sciences.
## 1.1. Methodological Approach
[European Nucleotide Archive (ENA)](https://www.ebi.ac.uk/ena/browser/home) and other sequence databases follow standards such as [Minimum Information about any (x) Sequence (MIxS)](https://gensc.org/mixs/) created by the Genomic Standards Consortium. Specimens databases generally follow the standards, Darwin Core ([@10.1371/journal.pone.0029715]) or ABCD ([@10.1080/11263504.2012.740085]). These standards define terms for the data that describe the sequence or specimen and their origins. However, many of these terms require only free text content and the terms do not necessarily map interoperably between standards. Our approach is to discover ways to connect related elements of these data standards to identify the associated sequences and specimens.

For example, our [herbarium](https://www.plantentuinmeise.be/en/) has been working towards connecting all the people associated with specimens, such as collectors and identifiers, to stable identifiers, such as [ORCID](https://orcid.org/) IDs [@10.1093/database/baaa072]. If we are able to match a person name in the metadata of a sequence to a stable identifier, such as an [ORCID](https://orcid.org/) ID, we can narrow the search of specimens and sequence considerably. We can also make use of the power of [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page) as a broker of person identifiers, so that if we have one identifier in one database, we can use Wikidata to find other identifiers and use the full suite of identifiers to search the other database.

![Schema of the workflow](data/workflowschema.jpg "Schema of the workflow")

Figure 1. A diagram of the connections between sequence databases (e.g. ENA) and specimens (GBIF). Sequences and specimens are often cited in literature and biological databases. These can be used as a source of accession numbers, locations, dates, person names and taxa with which sequence and specimen data can be linked. Wikidata can be used as a broker to link identifier schemes, such as taxon IDs. Even though candidate matches between sequences and specimens can be found uncertainty often remains. Therefore, we have foreseen a human verification step to confirm matches before the results are stored as a digital object that combines the results.
# 2. Methods
## 2.1. Finding candidate sequences

### 2.1.1

Access to sequence data Queries were made to the [ENA portal API](https://www.ebi.ac.uk/ena/portal/api/) attempting to select sequence records potentially related to voucher specimens from the herbarium collection of [Meise Botanic Garden](https://www.botanicalcollections.be/#/en/home) (MeiseBG). ENA also contains data on samples that sequences have been derived from, however, similar searches to those conducted on sequences resulted in far fewer results. Most sequences appeared unassociated with samples. We focused on the `specimen_voucher` data field, as other fields like `description` threw many false positives with our querying approach and rarely contained indicators of interest. All query work was done in R, a script called `bh-apicalls.R` available in this repository.

Different query approaches were tried. Initially, multiple queries were specified combining wild cards (*) and common terms associated with MeiseBG. For example, the internationally recognised herbarium code for the herbarium of Meise Botanic Garden is `BR` (see [Index Herbariorum](http://sweetgum.nybg.org/science/ih/)).
The query values are listed below:

`*br)*`

`*br:*`

`*br<*`

`*br-*`

`*meise*`

`*gard.*belg*`

These values mostly use the code `BR`, adding punctuation characters to omit false-positives as the API’s queries are not case sensitive. Nor does the ENA API support regular expressions. To work around this, a query was made for the more generic `*b*` (i.e. all sequences with a b in their specimen_voucher field). A more generic any value query for this field (i.e. `*`) was attempted, but came with performance issues (both at the API response and the local memory side) and was thus abandoned. The exported results from this general `*b*` query were then mined using more specific regular expressions, including (other than those previously listed):

`br[0-9]{13}`

`br [0-9]{13}`

These fit the pattern of MeiseBG specimen barcodes, which are used as catalogue numbers. Regular expressions were also used to eliminate some false-positives, in particular acronyms that contained BR but were not limited to it and hence contained other upper case characters (i.e. using negative grep for `[A-Z]BR`). A few sequences were found by the `*meise*` query, but not in the `*b*` query. These were added to the results from the mining approach of the `*b*` query.

## 2.2. Mining the results for specimen properties

Using this method, an eventual result was obtained of ca. 8,398 sequences. 5,920 were left after eliminating false-positives, including records with ‘Meisenburg’, a partial homonym to ‘Meise’, and acronyms that contained BR but also contained other uppercase characters. Subsequently, for all of these results we attempted to identify collection numbers and collector names within the `specimen_voucher` string from ENA.

The recommended format for [`specimen voucher`](https://www.ebi.ac.uk/ena/WebFeat/qualifiers/specimen_voucher.html) is `institutionCode:collectionCode:id`, but in recommendation has not been followed in our institution. More often, beyond a reference to the institution as described above (i.e. BR or Meise), the specimen is only described through a combination of the name(s) of the person(s) who collected it and a numeric identifier. This (alpha)numeric identifier can be the so-called `collection number`, which is often given to a botanical specimen during the collection event or shortly after, to differentiate it from other specimens collected by the same individuals on the same date. The numeric identifier may also be the unique accession number that disambiguates the specimen from all others in the collection. It is not uncommon for this identifier to be only partially present in the `specimen voucher` field. For example, the non-numeric part may be omitted or leading zeroes. It is also not uncommon for multiple numeric identifiers to be present in the `specimen voucher` field.

To match the numeric identifiers found in the ENA sequence metadata to numbers known for Meise’s herbarium specimens, the numbers were extracted by splitting the `specimen voucher` string into substrings divided by spaces. Out of each substring that contained at least one number, the numeric elements were extracted to avoid ambiguity through punctuation. For example, a `specimen voucher` value of `De Block 6 (BR)(Meise 77-0360)` would result in two substrings of `6` and `770360`.

To match person names, the surnames of persons listed in MeiseBG’s list of known collectors were matched into the whole `specimen voucher` string. Any positive match was accepted and the PIDs associated with that record in the collector list were linked to the ENA sequence metadata.

Finally, the ENA provided `tax_id` - an [NCBI](https://www.ncbi.nlm.nih.gov/taxonomy/) taxon id - was matched to the [Global Biodiversity Information Facility](https://www.gbif.org/) (GBIF) backbone taxon ID using Wikidata as a broker [@10.15468/39omei]. This was done using a series of SPARQL queries. This way, the taxon names for ENA sequences could be unambiguously linked to taxon names for specimens in GBIF.

## 2.3. Matching to specimen data

Subsequently, a matching process was set up, where a positive link between a specimen published to GBIF and an ENA sequence was confirmed if there was a match between all of the following: 

taxon ID on ENA and taxonKey in the GBIF Backbone
one of the numeric elements in the ENA `specimen_voucher` field and the numeric element of `recordNumber` on a specimen record in GBIF
one of the PIDs connected to the ENA record and `recordedByID` in GBIF. 

GBIF has an [API](https://www.gbif.org/developer/summary), but the matching was performed locally using the GBIF-generated occurrence file of the Meise Botanic Garden Herbarium dataset [@10.15468/wrthhx]. This way, the overhead of using an API was avoided and manipulations such as extracting only numeric elements was possible.

Through this process, 1,336 ENA sequences were connected to at least one GBIF record. This approach only considered herbarium specimens on GBIF. Further work is needed to link living accessions and unpublished specimens. A particular class of specimens are those that were collected from living accessions in the Garden. These are currently not published to GBIF, in part because their metadata do not fit well into the Darwin Core standard used on GBIF. Many of these specimens have two gathering events: the original gathering indicating its provenance and the secondary gathering from the place it was cultivated in the Garden.

Candidate matches between sequences on GBIF and sequences on ENA were envisaged to be processed through an online application whereby a user could compare the metadata of the two entities. They would then confirm in the application that they agreed that both the sequence and the specimen had a common origin. During the Biohackathon a Django app was developed to demonstrate the possibility. Matches could be imported in a JSON format and combined with additional metadata from both ENA and GBIF to better inform the user. In the future, such an app could export validated matches. This export could subsequently be used to annotate the GBIF records with their correct ENA sequence, or vice versa. Validated matches could also be made available through an update operation of a digital object representing the Meise specimens, adding links to ENA sequences when positively matched.

# 3. Recommendations

## For INSDC partner databases
Databases should incorporate PIDs into their data model for…
people (i.e. [ORCID](https://orcid.org/))
institutions (i.e. [ROR](https://ror.org/scope))
publications (i.e. [DOI](https://www.doi.org/))
and specimens [@10.1093/database/bax003].
## For collections
Scientists depositing sequence data should be given training on the data model and standards used.
Collections should make more effort to reconnect their backlog of voucher specimens to their sequences.
Specimens should obtain a PID at the earliest point possible upon collection and certainly before tissue collection for sequencing.
Novel data encapsulation approaches are needed to ensure that the links between these data can be transversed by people and by machines.

# 4. Future work

Reconnecting the links between objects and the data derived from them is inefficient, error prone and expensive. Indeed, if rigorous data management procedures were followed it would not be necessary. Considerable work needs to be done to improve scientific procedures, infrastructural standards and scientific data management culture. Much of the followup work that needs to be done is to make these changes, so that there will be no need to reconnect vouchers and their data in the future.

# Acknowledgements
The authors thank the organizers BioHackathon-Europe for their support and the smooth running of the event. QG, PH, MD, MT were supported by SYNTHESYS+ a Research and Innovation action funded under H2020-EU.1.4.1.2. Grant agreement ID: 823827 and by DiSSCo Prepare H2020-INFRADEV-2019-2020 – Grant Agreement No. 871043.

# References

Leave thise section blank, create a paper.bib with all your references.


