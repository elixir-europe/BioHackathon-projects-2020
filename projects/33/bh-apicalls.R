library(tidyverse)
library(jsonlite)
library(httr)
library(urltools)
library(rentrez)
library(magrittr)

#function to query ena
querna <- function(url) {
  full_url <- URLencode(url)
  ena_r = GET(full_url)
  rcontent = content(ena_r,
                     as="text")
  rjson = fromJSON(rcontent,
                   flatten=T)
  return(rjson)
}

#ena

base_url = "https://www.ebi.ac.uk/ena/portal/api/search?"

#niki's example request
full_url = paste0(base_url, "result=sequence",
                  "&query=collection_date>=2015-01-01 AND collection_date<=2019-12-31",
                  #"&query=specimen_voucher=\"*meise*\"",
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
                         "study_accession,",
                         "collected_by,",
                         "collection_date,",
                         "tax_id,",
                         "identified_by"),
                  "&limit=0&format=json")

#find all records with a b (big content)
full_url = paste0(base_url, "result=sequence",
                  "&query=specimen_voucher=\"*b*\"",
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
                         "study_accession,",
                         "collected_by,",
                         "collection_date,",
                         "tax_id,",
                         "identified_by"),
                  "&limit=0&format=json")

#separate extraction as memory issues may occur:
full_url <- URLencode(full_url)

ena_r = GET(full_url)

rcontent = content(ena_r,
                   as="raw")

#may need to save workspace or raw file and reboot R session
#then convert raw content
rcontent= rawToChar(rcontent)

rjson = fromJSON(rcontent,
                 flatten=T)

#see frequency of empty fields
#use this on bigset for an overview (otherwise not used)
stats = b[2,]
for (i in 1:dim(b)[2]) {
  var = colnames(b)[i]
  x = b %>%
    filter(.data[[var]]=="")
  stats[1,i] = dim(x)[1]
  stats[2,i] = round(100*dim(x)[1]/dim(b)[1],2)
}

#other queries for Meise-related sequences
full_url = paste0(base_url, "result=sequence",
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
                         "study_accession,",
                         "collected_by,",
                         "collection_date,",
                         "tax_id,",
                         "identified_by"),
                  "&limit=0&format=json")

brmeise = querna(full_url)
write_tsv(brmeise,"data/brmeiseset.txt",na="")

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
                         "study_accession,",
                         "collected_by,",
                         "collection_date,",
                         "tax_id,",
                         "identified_by"),
                  "&limit=0&format=json")

brcard = querna(full_url)
write_tsv(brcard,"data/brcard.txt",na="")

full_url = paste0(base_url, "result=sequence",
                  "&query=specimen_voucher=\"*BR:*\"",
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
                         "study_accession,",
                         "collected_by,",
                         "collection_date,",
                         "tax_id,",
                         "identified_by"),
                  "&limit=0&format=json")
brcolon = querna(full_url)
write_tsv(brcolon,"data/brcolonset.txt",na="")

full_url = paste0(base_url, "result=sequence",
                  "&query=specimen_voucher=\"*BR-*\"",
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
                         "study_accession,",
                         "collected_by,",
                         "collection_date,",
                         "tax_id,",
                         "identified_by"),
                  "&limit=0&format=json")

brdash = querna(full_url)
write_tsv(brdash,"data/brdashset.txt",na="")

#don't run
#many genes give false positives when querying the description field
# full_url = paste0(base_url, "result=sequence",
#                   "&query=description=\"*BR)*\"",
#                   paste0("&fields=",
#                          "accession,",
#                          "country,",
#                          "location,",
#                          "description,",
#                          "scientific_name,",
#                          "bio_material,",
#                          "culture_collection,",
#                          "specimen_voucher,",
#                          "sample_accession,",
#                          "study_accession,",
#                          "collected_by,",
#                          "collection_date,",
#                          "tax_id,",
#                          "identified_by"),
#                   "&limit=0&format=json")

full_url = paste0(base_url, "result=sequence",
                  "&query=specimen_voucher=\"*BR0000*\"",
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
                         "study_accession,",
                         "collected_by,",
                         "collection_date,",
                         "tax_id,",
                         "identified_by,",
                         "tax_division"),
                  "&limit=0&format=json")
br0 = querna(full_url)

#not run
#regex doesn't work
# full_url = paste0(base_url, "result=sequence",
#                   "&query=specimen_voucher=\"BR[0-9]{13}\"",
#                   paste0("&fields=",
#                          "accession,",
#                          "country,",
#                          "location,",
#                          "description,",
#                          "scientific_name,",
#                          "bio_material,",
#                          "culture_collection,",
#                          "specimen_voucher,",
#                          "sample_accession,",
#                          "study_accession,",
#                          "collected_by,",
#                          "collection_date,",
#                          "tax_id,",
#                          "identified_by"),
#                   "&limit=0&format=json")
#brre = querna(full_url)

#
#samples: very few
# full_url = paste0(base_url, "result=sample",
#                   "&query=center_name=\"*br*\"",
#                   paste0("&fields=",
#                          "accession,",
#                          "country,",
#                          "location,",
#                          "description,",
#                          "bio_material,",
#                          "culture_collection,",
#                          "specimen_voucher,",
#                          "sample_accession,",
#                          "collected_by,",
#                          "collection_date,",
#                          "identified_by,",
#                          "center_name"),
#                   "&limit=0&format=json")
# brs = querna(full_url)

#old approach: multiple queries join

br = rbind(brmeise,brcard)
br = rbind(br,brcolon)
br = rbind(br,brdash)
br = rbind(br,br0)

br = filter(br,!duplicated(accession))

write_tsv(br,"data/brpossibles.txt",na="")

#new approach: mine big set of b query
#allows use of regex for barcodes
br2 = b %>%
  mutate(specimen_voucher2 = tolower(specimen_voucher)) %>%
  filter(grepl(paste("br\\)",
                     "br[0-9]{13}",
                     "br:",
                     "br<",
                     "br-",
                     "br [0-9]{13}",
                     "meise",
                     "gard.*belg",
                     sep="|"),
               specimen_voucher2)) %>%
  select(-specimen_voucher2)

#will omit a few of the meise query with no b
br2n = filter(br2,!accession%in%br$accession)
br3 = rbind(br,br2n)

write_tsv(br3,"brpossibles.txt",na="")