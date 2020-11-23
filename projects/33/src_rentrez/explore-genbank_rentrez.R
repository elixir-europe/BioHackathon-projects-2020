

library(rentrez)
library(tidyverse)

entrez_dbs()
db<-"biosample" # 40 results, we can get id's directly
# db<-"nucleotide" # 9000 results, we need to use web history objects
entrez_db_summary(db)


query_init<-entrez_search(db,term="meise",use_history=T)
# fetch the result directly 
query_result <- entrez_fetch(db=db,web_history = query_init$web_history,rettype = "xml",retmode = "xml")

# directyl write to file
cat(entrez_fetch(db=db,web_history = query_init$web_history,rettype = "json"),file="query_result.json")
# stream to file
write_lines(entrez_fetch(db=db,web_history = query_init$web_history,rettype = "json"),"out_lines.txt")


res_summary<-entrez_summary(db=db,web_history = query_init$web_history,retmode="xml")

extracted_catalogNumbers<- str_extract_all(query_result,"BR[0-9 ]+") %>% unlist %>% unique
extracted_catalogNumbers[nchar(extracted_catalogNumbers) < 15] %>%
  str_extract_all("[0-9]+") %>%
  unlist() %>% 
  
# glue BR + 15-number of digits-2: zeros's + digits
# str_extract_all(as.character(res_summary),"BR[0-9 ]+") %>% unlist %>% unique
