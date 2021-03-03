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

base_url = "https://www.ebi.ac.uk/ena/portal/api/search?"

#
##Acquire a generic dataset to mine
#

#as regex not supported for API queries:

#find all records with a b
full_url = paste0(base_url, 
                  "result=sequence",
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

#separate response extractions instead of function 
#as memory issues may occur:
full_url <- URLencode(full_url)

ena_r = GET(full_url)

rcontent = content(ena_r,
                   as="raw")

#at this point, may need to save workspace or raw file 
#and reboot R session

#then convert raw content to json char
rcontent= rawToChar(rcontent)

#json to tibble
rjson = fromJSON(rcontent,
                 flatten=T)

#
##see the frequency of missing values
#

#use this on a big response set 
#for an overview (otherwise not used)
stats = rjson[2,]
for (i in 1:dim(rjson)[2]) {
  var = colnames(rjson)[i]
  x = rjson %>%
    filter(.data[[var]]=="")
  stats[1,i] = dim(x)[1]
  stats[2,i] = round(100*dim(x)[1]/dim(rjson)[1],2)
}

#
##other queries for Meise-related sequences
#

#meise
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

#
##mine big set of b query
#

#allows use of regex for barcodes
br2 = rjson %>%
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

#add the sequences from the meise query without a b in the 
#voucher field
br3 = filter(br2,!accession%in%brmeise$accession)
br3 = rbind(br3,brmeise)

#save results
write_tsv(br3,"brpossibles.txt",na="")