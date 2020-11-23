library(tidyverse)
library(data.table)
brpossibles<-fread(file.path("../33_molseq","data","brpossibles.txt"))
# brpossibles<-fread(file.path("../data/brpossibles.txt"))
gbif_export<-fread(file.path("../33_molseq","data","0107125-200613084148143.csv"),encoding = "UTF-8")
botcol_export<-fread(file.path("../33_molseq","data","herbarium_export_20201110022328.txt"),encoding="UTF-8")
# any(across(all_of(names(brpossibles)),stringi::stri_detect_regex("BR[0-9]+")))


# filter on date, then on species, or the other way around? 

# take the (long) numbers from specimen_voucher and query against catalogNumber (partial query allowed?)
possible_barcodes <- filter(brpossibles, str_detect(specimen_voucher, "[0-9]{7,}")) %>%
  pull(specimen_voucher) %>%
  str_extract_all("[0-9]{7,}") %>% 
  # transmute(specimen_voucher,digits=str_extract(specimen_voucher,"[0-9]{7,}")) %>%
  unlist()
  
  

# rewrite candidate barcode extraction ------------------------------------

 transmute(brpossibles,candidate=str_extract(specimen_voucher,"([0-9]+(?>-)?[0-9]+)"))

extract_number <- function(input_string) {
  input_string %>% str_extract("([0-9]+(?>-)?[0-9]+)") %>% 
    str_extract_all("[0-9]+") %>%
    unlist %>% 
    str_c(collapse = '')
}

# brpossibles %>% pull(specimen_voucher) %>%
#   map_chr(extract_number)
  # str_extract("([0-9]+(?>-)?[0-9]+)") %>% 
  # str_extract_all("[0-9]+")

brpossibles %>% 
  mutate(candidate_digits=map_chr(specimen_voucher,extract_number)) %>% 
  filter(nchar(candidate_digits)>6)


# match candidate codes to gbif -------------------------------------------

for(candidate_barcode in unique(possible_barcodes)){
  return<-gbif_export[str_detect(catalogNumber,candidate_barcode),catalogNumber]
  if(length(return)!=0){
    scientificName <-
      gbif_export[str_detect(catalogNumber, candidate_barcode), scientificName]
    
    brpossibles[str_detect(candidate_barcode,specimen_voucher),]
    
    print(paste(candidate_barcode,'=',return))
    
  }
  
# dash and two digits: last two digits are check digit   
# COMBAK: add validation by checking scientificName as well? 
# COMBAK: add validation by checking stringdistance between catalogNumber and candidate_barcode
}



# match candidates to livcol (botcol export) ------------------------------

filter(botcol_export,botcol_export$occurrenceID %in% possible_barcodes) %>% 
  mutate(candidate_barcode=botcol_export$occurrenceID[botcol_export$occurrenceID %in% possible_barcodes],
         identifier=file.path("https://www.botanicalcollections.be/accession",occurrenceID))

# IDEA trim leading zero's from catalogNumbers from GBIF, and look trough brpossibles for a match

# IDEA the other way around, take silica gel specimens from GBIF (those are most
# likely to be sequenced), and looking those up on the ENA API


