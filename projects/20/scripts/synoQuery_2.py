from SPARQLWrapper import SPARQLWrapper, JSON
import requests
from lxml import  etree as et
import sys
import click
import synoQueryLib as SynQL


ncbi_spNames=sys.argv[1]

# @click.command()
# @click.argument('genus')
# @click.argument('species')



def getSpeciesNames(ncbi_spNames):
    D_TxID_sciNameSyno={}
    f=open(ncbi_spNames, 'r')
    f.readline()
    for line in f:
        l=line.strip().split('\t')
        sciName=l[0]
        syno=l[1].split(';')
        TaxID=l[2]
        if 'NA' not in syno:
            D_TxID_sciNameSyno[TaxID]=[sciName]+ syno
        else:
            D_TxID_sciNameSyno[TaxID]=[sciName]
    f.close()
    return D_TxID_sciNameSyno

TaxID_sciNameSyno=getSpeciesNames(ncbi_spNames)


def strSpecQuery(genus, species):
    string = \
        """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX treat: <http://plazi.org/vocab/treatment#>
    PREFIX dwc: <http://rs.tdwg.org/dwc/terms/>
    SELECT DISTINCT ?tc ?genus ?species
    WHERE {{
      ?t dwc:genus "{}".
      ?t dwc:species "{}". 
    MINUS {{ ?t dwc:subSpecies ?subspecies.}}
      ?t ((^treat:deprecates/(treat:augmentsTaxonConcept|treat:definesTaxonConcept))|((^treat:augmentsTaxonConcept|^treat:definesTaxonConcept)/treat:deprecates))* ?tc .
      ?tc a <http://filteredpush.org/ontologies/oa/dwcFP#TaxonConcept> .
      ?tc dwc:genus ?genus .
      ?tc dwc:species ?species. 
    }}""".format(genus, species)
    return string


def querySynoSpecies(genus, species):
    sparql = SPARQLWrapper("https://treatment.ld.plazi.org/sparql")
    sparql.setQuery(strSpecQuery(genus, species))
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    bindings = results['results']['bindings']
    L=[]
    for i in bindings:
        L.append(i['genus']['value'] + ' ' +i['species']['value'])
    return list(set(L))



# def querySynoSpecies(genus, species):
#     sparql = SPARQLWrapper("https://treatment.ld.plazi.org/sparql")
#     sparql.setQuery("""
#     PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#     PREFIX treat: <http://plazi.org/vocab/treatment#>
#     PREFIX dwc: <http://rs.tdwg.org/dwc/terms/>
#     SELECT DISTINCT ?tc ?genus ?species
#     WHERE {
#       ?t dwc:genus "Rhinolophus" .
#       ?t dwc:species "sinicus". 
#     MINUS { ?t dwc:subSpecies ?subspecies.}
#       ?t ((^treat:deprecates/(treat:augmentsTaxonConcept|treat:definesTaxonConcept))|((^treat:augmentsTaxonConcept|^treat:definesTaxonConcept)/treat:deprecates))* ?tc .
#       ?tc a <http://filteredpush.org/ontologies/oa/dwcFP#TaxonConcept> .
#       ?tc dwc:genus ?genus .
#       ?tc dwc:species ?species. 
#     }""")
#     sparql.setReturnFormat(JSON)
#     results = sparql.query().convert()
#     bindings = results['results']['bindings']
#     L=[]
#     for i in bindings:
#         L.append(i['genus']['value'] + ' ' +i['species']['value'])
#     return list(set(L))
    #print results
    #print bindings



def getSynoSpecies(genus, species):
    results = SynQL.synoQuerySpecs(genus, species)
    bindings = results['results']['bindings']
    dSynoQuery = {}
    for result in bindings:
        uriSpec = result["tc"]["value"]
        with requests.get(uriSpec, stream=True) as r:
            if r.status_code == requests.codes.ok:
                # print('\n\n', r.text, '\n\n')
                root = SynQL.etRoot(r.text, kind='stream')
                SynQL.et2screen(root)
                dSynoQuery[SynQL.uri2key(uriSpec)] = SynQL.et2dict(root)
        synonymsRes = SynQL.synoQuerySynonyms(uriSpec)
        synonyms = synonymsRes['results']['bindings']
        for synonym in synonyms:
            uriSyn = synonym["tc"]["value"]
            #print(uriSyn)
            with requests.get(uriSyn, stream=True) as r:
                if r.status_code == requests.codes.ok:
                    # print('\n\n', r.text, '\n\n')
                    root = SynQL.etRoot(r.text, kind='stream')
                    SynQL.et2screen(root)
                    dSynoQuery[SynQL.uri2key(uriSyn)] = SynQL.et2dict(root)
    return dSynoQuery


def get_synoSpecies_Res(TaxID_sciNameSyno, f_out_name):
    D_TaxIDS_sciName_SynoSpecies={}
    for TaxID in TaxID_sciNameSyno:
        Names=TaxID_sciNameSyno[TaxID]
        for name in Names:
            if 'sp.' not in name and '/' not in name:
                sci_temp=name.split(' ')
                if len(sci_temp)>2 and 'cf.' in sci_temp:
                    gen=sci_temp[0]
                    sp=sci_temp[2]
                    Syno_Synospecies=getSynoSpecies(gen, sp)
                    if len(Syno_Synospecies)>0:
                        Res=[name, Syno_Synospecies]
                        D_TaxIDS_sciName_SynoSpecies.setdefault(TaxID,[]).append(Res)
                    elif len(Syno_Synospecies)==0:
                        Res=[name, ['NA']]
                        D_TaxIDS_sciName_SynoSpecies.setdefault(TaxID,[]).append(Res)
                elif len(sci_temp)>2 and 'cf.' not in sci_temp:
                    pass
                elif len(sci_temp)==2:
                    gen=sci_temp[0]
                    sp=sci_temp[1]
                    Syno_Synospecies=getSynoSpecies(gen, sp)
                    if len(Syno_Synospecies)>0:
                        Res=[name, Syno_Synospecies]
                        D_TaxIDS_sciName_SynoSpecies.setdefault(TaxID,[]).append(Res)
                    elif len(Syno_Synospecies)==0:
                        Res=[name, ['NA']]
                        D_TaxIDS_sciName_SynoSpecies.setdefault(TaxID,[]).append(Res)
    f_out=open(f_out_name, 'w')
    f_out.write('NCBI_Taxid\tNCBI_Name\tSynoSpeciesName\tKingdom\tPhylum\tClass\tOrder\tFamily\tGenus\tSpecies\n')
    for tid in D_TaxIDS_sciName_SynoSpecies:
        for res in D_TaxIDS_sciName_SynoSpecies[tid]:
            initialQuery=res[0]
            queryRes=res[1]
            if type(queryRes)==list:
                f_out.write(tid+'\t'+initialQuery+'\t'+queryRes[0]+'\n')
            elif type(queryRes)==dict:
                for syn in queryRes:
                    Kingdom=queryRes[syn]['kingdom']
                    Phylum=queryRes[syn]['phylum']
                    Class=queryRes[syn]['class']
                    Order=queryRes[syn]['order']
                    Family=queryRes[syn]['family']
                    Genus=queryRes[syn]['genus']
                    Species=queryRes[syn]['species']
                    L=[Kingdom, Phylum, Class, Order, Family, Genus, Species]
                    f_out.write(tid+'\t'+initialQuery+'\t'+syn+'\t'+'\t'.join(L)+'\n')
    f_out.close()


f_outName=ncbi_spNames.split('.')[0]+'_SynoSpecies.tsv'
SYNO=get_synoSpecies_Res(TaxID_sciNameSyno, f_outName)

#             if len(syno)>0:
#                 for s in syno:
#                     if 'sp.' not in s and len(s.split()==2):
#                         s1=s.split()
#                         synoSpecies=querySynoSpecies(s1[0], s1[1])
#                         
#                         
# 
# d={u'head': {u'vars': [u'tc', u'genus', u'species']}, u'results': {u'bindings': [{u'genus': {u'type': u'literal', u'value': u'Rhinolophus'}, u'tc': {u'type': u'uri', u'value': u'http://taxon-concept.plazi.org/id/Animalia/Rhinolophus_ferrumequinum_Ellerman_1951'}, u'species': {u'type': u'literal', u'value': u'ferrumequinum'}}, {u'genus': {u'type': u'literal', u'value': u'Rhinolophus'}, u'tc': {u'type': u'uri', u'value': u'http://taxon-concept.plazi.org/id/Animalia/Rhinolophus_ferrumequinum_Schreber_1774'}, u'species': {u'type': u'literal', u'value': u'ferrumequinum'}}]}}
# 
# >>> for i in d['results']['bindings']:
# ...     print i['genus'], i['species']
# ... 
# {u'type': u'literal', u'value': u'Rhinolophus'} {u'type': u'literal', u'value': u'ferrumequinum'}
# {u'type': u'literal', u'value': u'Rhinolophus'} {u'type': u'literal', u'value': u'ferrumequinum'}
# >>> 
# >>> for i in d['results']['bindings']:
# ...     print i['genus']['value'], i['species']['value']
# 
# 
# for result in bindings:
#     uri = result["tc"]["value"]
#     print(uri)
# #    with requests.get(uri, stream=True) as r:
# #        if r.status_code == requests.codes.ok:
# #            content = r.text
# #            print(content)
# #            root = et.fromstring(content)
# #            print(root)
# 
# Rhinolophus_ferrumequinum_Ellerman_1951
# Rhinolophus_ferrumequinum_Schreber_1774