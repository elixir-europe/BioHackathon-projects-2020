# Project 22: Federating Accessible InterMine Resources

## Abstract

InterMine, an ELIXIR Recommended Interoperability Resource, is a platform to integrate life science data. The many InterMine installations around the world contain information on diverse organisms, including human data, model animals, plants and drug targets. An InterMine instance stores all its data in a relational database. This data can be accessed through a set of RESTful web service APIs, with direct support for many common programming languages such as Python, JavaScript, Java and R. In order to increase data interoperability and enable federated queries among different resources, we we will explore and prototype a new mechanism which will allow the users to access InterMine data using SPARQL, a language able to retrieve data stored in RDF graphs. SPARQL will be a new method to interoperate between InterMine and life science datasets and beyond, for example using the European Patent Office or habitat data from the EU Commission SPARQL endpoints. In particular, during this hackathon we will use CovidMine, an InterMine instance which integrates COVID 19 data, Sars-CoV-2 reference genome and nucleotide sequences, to interoperate with resources such as the SIB covid-19 integrated knowledgebase.

Direct translation of InterMine data to an RDF has been carried out in the past but it is inconvenient to maintain such duplication. In this hackathon we will use existing software, such as Ontop, to translate SPARQL queries into SQL queries. This relies on declarative mappings which specify how to map the InterMine relational schema to an RDF model. This will allow SPARQL access to InterMine-hosted data with a minimal increase in infrastructure cost. Writing such mappings for InterMine is challenging, due to the flexible nature of its data models, which vary according to the different installations: whilst InterMine comes with a data model for core biological entities, deployments often extend these entities to publish more types of data.
In general, this project is an opportunity to encourage those who maintain resources based on relational databases to provide similar mechanisms for running SPARQL queries against their data in an efficient way.
Beyond InterMine, we welcome other life science resources using relational storage to help with implementing RDF views on their data, when possible directly exposing their data with BioSchemas, ready to query.

Example SPARQL queries representing interesting biological use cases will be wrapped in examplar FAIR accessors (https://peerj.com/articles/cs-110/)) to show how this hackathon can directly improve the European FAIR life science data landscape.

Special care will be taken to ensure Interoperability with other key life science data sets such as UniProt, Rhea, Disgenet, Orphanet and many more. Which will be demonstrated with queries using the federated capabilities of SPARQL, letting these act as if they are part of an InterMine instance.


## Topics

Bioschemas
 Covid-19
 Data Platform
 Federated Human Data
 Interoperability Platform
 Plant Sciences

**Project Number:** 22



**EasyChair Number:** 33

## Team

### Lead(s)

Daniela Butano - daniela@intermine.org
 Jerven Bolleman - Jerven.Bolleman@sib.swiss

### Nominated participant(s)

Jerven Bolleman - Jerven.Bolleman@sib.swiss
 Daniela Butano - daniela@intermine.org

## Expected outcomes

1. Generate a dynamic R2RML mappings starting from the InterMine core model
 2. Execute some queries using Ontop (or D2R server) and CovidMine resource
 3. Execute some federated queries using UniProt
 4. Run a set of complex sparql queries to verify that translation of SPARQL queries -> SQL queries works well

## Expected audience

1. SPARQL/RDF/Semantic Web developers
 2. People with resources with a relational backend who want to provide a similar mechanism

**Number of expected hacking days**: 4

## Useful links
1. InterMine-R2RML-mapping github repo (https://github.com/danielabutano/intermine-R2RML-mapping)
 2. InterMine model description doc (https://intermine.readthedocs.io/en/latest/data-model/model/)
 3. R2RML Mapping Language (https://www.w3.org/TR/r2rml/)
 4. Ontop (https://ontop-vkg.org/)
 
## Instruction to build the biotestmine database using Docker
biotestmine database is a test database containing some data sets for Malaria (P. falciparum)
To build the database using docker:
1. Download the archive https://www.dropbox.com/s/tuqq3429jn3gd6b/biotestmine-data.tar.gz?dl=0
2. Unzip biotestmine-data.tar.gz
3. Start a new container with a docker volume mounted:
docker run -d --name postgres -v {FULL_path_of_unzipped_data_dir_}:/var/lib/postgresql/data -u 1000:1000 intermine/postgres
4. check the data:
docker exec -it postgres bash
psql -U postgres biotestmine

## Instruction to build the biotestmine database using InterMine script
Follow the instructions in the README (https://github.com/intermine/biotestmine/blob/master/README.md)
