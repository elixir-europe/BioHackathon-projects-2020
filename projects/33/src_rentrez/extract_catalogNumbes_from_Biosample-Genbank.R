

library(rentrez)
library(tidyverse)


# entrez_dbs() #get list of Genbank databases to Query

db <- "biosample" # 52 results, we can get id's directly, 36 have voucher codes in the metadata

# db<-"nucleotide" # 9000 results, we need to use web history objects
# entrez_db_summary(db) # get information about selected database

# searching on 'meise'
query_init <- entrez_search(db, term = "meise", use_history = T)
# fetch the result directly
query_result <- entrez_fetch(db = db, web_history = query_init$web_history, rettype = "xml", retmode = "xml")
query_result_list <- query_result %>%
  XML::xmlParse() %>%
  XML::xmlToList()


# extract catalogNumbers based on regex -----------------------------------


extracted_catalogNumbers <- str_extract_all(query_result, "BR[0-9 ]+") %>%
  unlist() %>%
  unique()

# form incorrect catalog numbers to complete ones by guessing
expanded_catalognumbers <- extracted_catalogNumbers[nchar(extracted_catalogNumbers) < 15] %>%
  str_extract_all("[0-9]+") %>%
  unlist() %>%
  str_pad(15 - 2, "left", "0") %>%
  paste0("BR", .)

catalogNumbers <- c(extracted_catalogNumbers[nchar(extracted_catalogNumbers) == 15], expanded_catalognumbers)

# get NCBI biosample identifiers ------------------------------------------
# subset list on barcode present

biosample_ids <- query_result %>%
  str_extract_all('(?<=<Id db="BioSample" is_primary="1">)[A-Z0-9]+') %>%
  unlist() %>%
  .[str_detect(query_result_list, "BR[0-9 ]+")]


biosample_identifiers <- file.path("https://www.ncbi.nlm.nih.gov/biosample", biosample_ids)

# output table ------------------------------------------------------------

tibble(catalogNumber = catalogNumbers, identifier = biosample_identifiers) %>%
  data.table::fwrite(file.path("../data/biosample_catalogNumbers.csv"))
message(paste(length(catalogNumbers), "catalogNumbers got matched to a BioSample id"))
