library(tidyverse)
library(jsonlite)
library(httr)
library(urltools)
library(rentrez)

#ena

base_url = "https://www.ebi.ac.uk/ena/portal/api/search?"

full_url = paste0(base_url, "result=sequence",
                  #"&query=collection_date>=2015-01-01 AND collection_date<=2019-12-31",
                  "&query=specimen_voucher=\"*meise*\"",
                  paste0("&fields=",
                         "accession,",
                         "country,",
                         "location,",
                         "description,",
                         "scientific_name,",
                         "bio_material,",
                         "culture_collection,",
                         "specimen_voucher,",
                         "sample_accession,",
                         "study_accession"),
                  "&limit=0&format=json")

full_url <- URLencode(full_url)

ena_r = GET(full_url)

rcontent = content(ena_r,
                   as="text")

rjson = fromJSON(rcontent,
                 flatten=T)

full_url = paste0(base_url, "result=sequence",
                  "&query=specimen_voucher=\"*BR)*\"",
                  paste0("&fields=",
                         "accession,",
                         "country,",
                         "location,",
                         "description,",
                         "scientific_name,",
                         "bio_material,",
                         "culture_collection,",
                         "specimen_voucher,",
                         "sample_accession,",
                         "study_accession"),
                  "&limit=0&format=json")

#genbank

gb_r = entrez_search(db="nuccore",
                  term="*meise*")

#only 20 res, need to page

#entrez_db_searchable(db="nuccore")

gb_results = entrez_summary(db="nuccore",
                   id=gb_r$ids)