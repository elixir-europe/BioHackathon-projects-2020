from django.db import models
from django.db.models import JSONField
import requests
from pygbif import occurrences
from wikidataintegrator import wdi_core
import pandas as pd
import numpy as np
from .ena import ENAtoGBIF
import json


class MatchingRun(models.Model):
    ena_query = models.CharField(max_length=500)
    ena_results = JSONField(null=True, blank=True)
    gbif_query = JSONField()
    gbif_results = JSONField(null=True, blank=True)
    wikidata_results = JSONField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    # These two will contain a list like [{enaID1: [gbifID1, gbifID2}, {enaID2: [gbifID3]}]
    # obj.suggested_results = {'MH175419': ['2571204007', '2571204014', '2571204017']}
    # The validated_matches will be a data export for Francisco/nsidr.org
    validated_matches = models.JSONField(null=True, blank=True)
    suggested_matches = models.JSONField(null=True, blank=True)

    def save(self):
        # If we do it this way, need to add some way of handling validation if genbank_query or gbif_query are badly formatted
        if not self.ena_results:  # This is so that modifying db objects does not cause the query to get run  again
            #self.ena_results = self.get_ena_results()
            enaApi = ENAtoGBIF(ena_query=self.ena_query, gbif_query=self.gbif_query)
            self.ena_results = enaApi.get_ena_results()
        if not self.gbif_results:
            enaApi = ENAtoGBIF(ena_query=self.ena_query, gbif_query=self.gbif_query)
            self.gbif_results = enaApi.get_gbif_results()
        if not self.wikidata_results:
            enaApi = ENAtoGBIF(ena_query=self.ena_query, gbif_query=self.gbif_query)
            self.wikidata_results = enaApi.get_wikidata_results(set([t['tax_id'] for k, t in self.ena_results.items()]))
        # I guess we can do some kind of automated matching here, before the super
        if not self.suggested_matches:
            self.suggested_matches = self.get_suggested_matches_demo()

        super(MatchingRun, self).save()

    def export_validated_matches(self):
        return self.validated_matches

    def get_suggested_matches_demo(self):
        sms = self.get_suggested_matches()
        i = 0
        demo_matches = {}
        for key, val in sms.items():
            if i < 11:
                demo_matches[key] = val
            i += 1
        return demo_matches

    def get_suggested_matches(self):
        gbif = pd.read_json(json.dumps(self.gbif_results), orient='index', dtype='str')
        gbif['eventDate'] = gbif['eventDate'].str[0:10]
        all_matches = {}
        for ena_key, ena in self.ena_results.items():
            suggested_matches = []
            if ena['tax_id'] in self.wikidata_results['ncbi_taxonID'].values():
                key_number = [key for key, val in self.wikidata_results['ncbi_taxonID'].items() if val == ena['tax_id']]
                if key_number:
                    gbif_taxon_id = self.wikidata_results['gbifid'][key_number[0]]  # Take first result
                    matching_rows = gbif.loc[gbif['taxonKey'] == gbif_taxon_id, 'gbifID']
                    print(matching_rows)
                    if ena['collection_date'] != '':
                        tougher_match = gbif.loc[(gbif['taxonKey'] == gbif_taxon_id) & (
                                    gbif['eventDate'] == ena['collection_date']), 'gbifID']
                        if tougher_match.any():
                            matching_rows = tougher_match

                    suggested_matches += list(matching_rows.values)
            else:
                sn_len = len(ena['scientific_name'])
                matching_rows = gbif.loc[gbif['scientificName'].str[0:sn_len] == ena['scientific_name'], 'gbifID']
                suggested_matches += list(matching_rows.values)
                sname = ena['scientific_name'].split(' ')[0]
                matching_rows = gbif.loc[gbif['scientificName'].str.split(' ').str[0] == sname, 'gbifID']
                suggested_matches += list(matching_rows.values)

            if suggested_matches:
                all_matches[ena_key] = list(set(suggested_matches))
        return all_matches
