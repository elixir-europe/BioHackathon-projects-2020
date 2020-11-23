# library(microbenchmark)
library(tidyverse)
library(data.table)
library(stringdist)
library(tictoc)
library(magrittr)

gbif_export<-fread(file.path("../33_molseq","data","0107125-200613084148143.csv"),encoding = "UTF-8")
ENA_big<-fread("6M_ENA_specimen_vouchers.csv",select=c("specimen_voucher","accession"),na.strings = "")
ENA_big_all<-fread("6M_ENA_specimen_vouchers.csv",na.strings = "") %>% mutate_all(list(~na_if(.,"")))
ENA_poss<-fread(file.path("../33_molseq","data","brpossibles.txt"))


# create visualistation of available data ---------------------------------

ENA_big_all[sample(.N, 100000)] %>%
  select(-c(
    "accession",
    "description",
    "scientific_name",
    # "specimen_voucher",
    "tax_id"
  )) %>% mutate_all(list(~na_if(.,"")))
  %>% visdat::vis_dat(warn_large_data = F)


# closer look at the date field, because vis_guess does not do Date types, but
# handles numbers better

ENA_big_all[sample(.N, 100000)] %>%
  select(c("collection_date"
    )) %>% mutate_all(list(~na_if(.,""))) %>% 
visdat::vis_guess(palette = "cb_safe")

determine_type <- function(input_object) {
  readr::guess_parser(input_object)
}

ENA_date<-ENA_big_all[sample(.N,100000)][,.(collection_date)][,type:=map_chr(collection_date,determine_type)]
ENA_date %>% group_by(type) %>% arrange() %>% visdat::vis_dat()


# extract and match specimen vouchers -------------------------------------


# 
# extract_number <- function(input_string) {
#   
#     paste0(unlist(str_extract_all(str_extract(input_string,"([0-9]+(?>-)?[0-9]+)"),"[0-9]+")),collapse = "")
#   
# }

library(stringi)
extract_number <- function(input_string) {
  
  # paste0(unlist(str_extract_all(str_extract(input_string,"([0-9]+(?>-)?[0-9]+)"),"[0-9]+")),collapse = "")
  # paste0(
    stri_trim_left(
    stri_extract_first(
      stri_extract(input_string, regex = "([0-9]+(?>-)?[0-9]+)"),
      regex = "[0-9]+"
    ),pattern="[^0]")
    # , collapse = "")
  
}

# microbenchmark(extract_number,times = 100)

ENA_poss[,digit:=map_chr(specimen_voucher,extract_number)]

system.time(ENA_big[1:10000,digit:=map_chr(specimen_voucher,extract_number)])

ENA_big[,digit:=map_chr(specimen_voucher,extract_number)]
# gbif_export[,digit:=map_chr(catalogNumber,extract_number)]
gbif_export[,digit:=map_chr(recordNumber,extract_number)]

# gbif_export[ENA_big]


glimpse(gbif_export)

# setkey(gbif_export,"changed catalog number integers")

# gbif_export[1:400,catalogNumber] %>% str_extract("[0-9]+") %>% as.double() %>% format(scientific=F) %>% trimws()

# splitsen op spaties, elke chunk met cijfers erin, haal te veel letters en
# haakjes eruit, en die strings enkel de cijfers, en vergelijken met wat er op
# GBIF staat in catalgoNumber, occurenceID, recordNumber (enkel de cijfers)



# stringdistance matching -------------------------------------------------

# Hamming distance: Number of positions with same symbol in both strings. Only
# defined for strings of equal length.

# Longest Common Substring distance: Minimum number of symbols that have to be
# removed in both strings until resulting substrings are identical.



tic()

# pull random sets to work on ---------------------------------------------

# set sample size
sample_size=100000

gbif_sample <- gbif_export[sample(.N, sample_size)][!is.na(digit), ]
# ENA_sample <- ENA_big[sample(.N, sample_size)][!is.na(digit), ]
ENA_sample <- ENA_poss[!is.na(digit), ]
# set maximum amount of times a digit can occur in the ENA dataset for it still to be matched
digit_occurence_treshold <- 50
common_digits <- ENA_sample %>%
  group_by(digit) %>%
  tally() %>%
  filter(n > digit_occurence_treshold) %>%
  pull(digit)
# drop the most common digits
ENA_sample <- ENA_sample %>% filter(!(digit %in% common_digits))
message(paste("filtered ENA_sample down to", nrow(ENA_sample), "digits"))

# string positions 
# 
# gbif_sample[
# ain(
#   gbif_sample[, digit],
#   ENA_sample[, digit],
#   method = "osa",
#   maxDist = 0.25,
#   weight = c(
#     d = .25, #deletions
#     i = .25, #insertions
#     s = 1, #substitution, not allowed
#     t = 1 #transposition, not allowed
#   )
# )]#[,ENA:=ENA_sample$digit]


# c("123","999")[ain(c("123","999"),c("23"),method="osa",maxDist=1,weight=c(d=.5,i=.5,s=1,t=1))]

# gbif_sample[
#   ain(
#     gbif_sample[, digit],
#     ENA_sample[, digit],
#     method = "osa",
#     maxDist = 0.25,
#     weight = c(
#       d = .25, #deletions
#       i = .25, #insertions
#       s = 1, #substitution, not allowed
#       t = 1 #transposition, not allowed
#     )
#   )][,ENA:=ENA_sample[amatch(  gbif_sample[, digit],
#          ENA_sample[, digit],method = "osa",
#          maxDist = 0.25,
#          weight = c(
#            d = .25, #deletions
#            i = .25, #insertions
#            s = 1, #substitution, not allowed
#            t = 1 #transposition, not allowed
#          )
# ),digit]] %>% View()


# getting fuzzy string results --------------------------------------------



# NOTE we are only getting the first match, not multiple! 

match_results<-ENA_sample[amatch(gbif_sample[, digit],
                  ENA_sample[, digit],method = "osa",
                  maxDist = 0.5,
                  weight = c(
                    d = .25, #deletions
                    i = 1, #insertions
                    s = 1, #substitution, not allowed
                    t = 1 #transposition, not allowed
                  ),nomatch = NA,)]$accession


# NOTE: extract identifier instead, and get digit by joining the columns: we
# want from ENA: identifier, voucher specimen field, and digit


# generate matched dataframe ----------------------------------------------



gbif_sample %>% mutate(ENA_accession=as.list(match_results)) %>%
  mutate(ENA_accession=as.character(ENA_accession)) %>% 
  right_join(ENA_sample,by=c("ENA_accession"="accession"),suffix=c(".gbif",".ena")) %>% 
  filter(!is.na(ENA_accession)) %>% 
  filter(!is.na(catalogNumber)) %>% # BUG we are getting matches without catalogNumber
  select(digit.gbif,digit.ena,ENA_accession,catalogNumber,specimen_voucher,recordNumber) %T>% 
  View("GBIF_ENA_matching_results") %>% 
  fwrite(paste0(sample_size,"-GBIF_ENA_matching_results.csv"))

toc()


# sample code and tryouts -------------------------------------------------


stringdist::stringdist("123","23",method = "lcs")



amatch(c("123","897"),c("23","2299","12"),method="osa",maxDist = 0.25,
       weight = c(
         d = .25, #deletions
         i = .25, #insertions
         s = 1, #substitution, not allowed
         t = 1 #transposition, not allowed
       ),nomatch = NA)


ain(c("123","897"),c("23","2299"),method="lcs",maxDist=1)
ain(c("123","897"),c("23","2299"),method="osa",maxDist=1,weight=c(d=.5,i=.5,s=1,t=1))

