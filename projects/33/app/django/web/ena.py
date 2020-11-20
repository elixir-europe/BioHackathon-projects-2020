from django.db import models
from django.db.models import JSONField
import requests
from pygbif import occurrences
from wikidataintegrator import wdi_core
import pandas as pd
import numpy as np
from ete3 import NCBITaxa


class ENAtoGBIF:
    """
    input: ena_query, ena_accession (list)
    output: ena2gbif (dict)
    """
    all_sequence_return_fields = "accession,study_accession,sample_accession,tax_id,scientific_name,base_count,bio_material,cell_line,cell_type,collected_by,collection_date,country,cultivar,culture_collection,dataclass,description,dev_stage,ecotype,environmental_sample,first_public,germline,host,identified_by,isolate,isolation_source,keywords,lab_host,last_updated,location,mating_type,mol_type,organelle,serotype,serovar,sex,submitted_sex,specimen_voucher,strain,sub_species,sub_strain,tax_division,tissue_lib,tissue_type,topology,variety,altitude,haplotype,plasmid,sequence_md5,sequence_version,sequence_version"
    base_url = "https://www.ebi.ac.uk/ena/portal/api/"
    ena_accession = None
    ena_query = None
    ena_return = None
    ena_query_param = {
            "result": "sequence",
            "fields": all_sequence_return_fields,
            "format": "json",
            "limit": 0
        }
    gbif_query = {
        "institutionCode" : "", 
        "taxonKey" : ""
    }

    def __init__(self, gbif_query:dict=None,ena_accession:list=None, ena_query:str=None):
        self.ena_accession = ena_accession  # accession candidates (i.e. from user/ PaperParser)
        self.ena_query = ena_query  # more flexible search "specimen_voucher=\"*BR)*\"", this will be placed directly in the api query string
        if not (self.ena_accession == None or self.ena_query == None):
            raise Exception("Only accept either one of these: ena_accession, ena_query. Not both.")
        if self.ena_accession is None and self.ena_query is None:
            raise Exception("At least one of these should be provided.")
        if gbif_query:
            #self.gbif_query.update(gbif_query)
            self.gbif_query = gbif_query

    def get_ena_results(self):

        # construct query strong from list of ena_accession
        # FIXME: ena api refuse to process wrong accession, have to filter it before query
        if not self.ena_query:
            search_r = requests.get(f"{self.base_url}search?includeAccessions={','.join([str(s) for s in self.ena_accession])}", params=self.ena_query_param)
        else:
            search_r = requests.get(f"{self.base_url}search?query={self.ena_query}", params=self.ena_query_param)
        print(search_r.status_code)
        results = search_r.json()
        # Change this to {'AF123': {'sex': '', 'host': '', 'tax_id': '84861'....}, 'AF456': {'sex': 'm', 'host': '', ...
        # also save it
        self.ena_return = {r['accession']: r for r in results}
        return {r['accession']: r for r in results}

    def get_gbif_results(self):
        first = occurrences.search(**self.gbif_query)
        results = first['results']
        for offset in range(300, min(first['count'], 90000), 300):
            args = {**self.gbif_query, **{'offset': offset}}
            results += occurrences.search(**args)['results']

        return {r['gbifID']: r for r in results}

    def get_wikidata_results(self, tax_ids:list=None):
        if tax_ids is None:
            assert (self.ena_return is not None) , "Empty ena API return"
            tax_ids = []
            for a,d in self.ena_return:
                tax_ids.append(d["tax_id"])

        # TODO: if there is no match, go up to family level
        query_template = """
                SELECT ?taxon ?taxonLabel ?ncbi_taxonID ?gbifid WHERE {
                  VALUES ?ncbi_taxonID {%s}
                  ?taxon wdt:P685 ?ncbi_taxonID.
                  OPTIONAL {?taxon wdt:P846 ?gbifid .}
                  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
                }
                """ 
        results = {}
        for tax_ids_subset in np.array_split(list(tax_ids), 30):
            query = query_template % ('"' + '" "'.join(tax_ids_subset.tolist()) + '"')
            try:
                # result_df.shape[0] should match ncbi_taxonID
                result_df = wdi_core.WDFunctionsEngine.execute_sparql_query(query=query, as_dataframe=True)
                # TODO: check which cell in column gbifid is empty, compare the df['ncbi_taxonID'] with the query listy
                # TODO: filter the unmatch ncbi_taxonID and go up to family level
                # query wikidata using the same query_template (should to it recursively, but can also stop if we cannot find the match order name)
                if results == {}:
                    results = result_df
                else:
                    results.append(result_df)
            except Exception as e:
                print(e)

        # Find the family name of them and put it to WHERE?

        return results.replace(np.nan, '').to_dict()

    # FIXME: maybe better to use the gbif API
    def ncbi_taxnomy_get_lineage(self,ncbi_taxonID:list):
        lineage_ls = []
        # http://etetoolkit.org/docs/latest/tutorial/tutorial_ncbitaxonomy.html
        self.ncbi.update_taxonomy_database()  #  this may take long time, better to include the sqlite db (~300mb) in the image
        for i in ncbi_taxonID:
            lineage_ls.append(self.ncbi.get_lineage(int(i)))
        return lineage_ls
