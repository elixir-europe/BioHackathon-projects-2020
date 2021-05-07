import os,sys

NCBI_taxonomy_Path='/home3/bbalech/DBs/Taxonomy/NCBI/Update_101120/new_taxdump/'

Nodes_NCBI= NCBI_taxonomy_Path+'nodes.dmp'


f_in_taxa=sys.argv[1]
f_out_Syno=f_in_taxa.split('.')[0]+'_WithTaxIDs.tsv'

Kingdom='Metazoa'
taxRank='species'

def get_taxa(f_in_taxa, Kingdom, taxRank):
    D_Taxonomy_RankKingdom={}
    f=open(f_in_taxa,'r')
    Headers='\t'.join(f.readline().strip().split('\t')[1:])
    for line in f:
        l=line.strip().split('\t')
        if l[2]!='NA':
            Taxon2Search_Taxonomy='\t'.join(l[1:])
            TaxonRank=taxRank
            TaxonKingdom=Kingdom
            D_Taxonomy_RankKingdom[Taxon2Search_Taxonomy]=[TaxonRank,TaxonKingdom]
    f.close()
    return D_Taxonomy_RankKingdom, Headers

T=get_taxa(f_in_taxa, Kingdom, taxRank)
Taxon_RankKingdom=T[0]
HEADERS=T[1]
#print Taxon_RankKingdom

T=get_taxa('Rhinolophus_species_ScientificNames_SynoSpecies.tsv', Kingdom, taxRank)

def getTaxID_SynNames(NCBITaxonomyPath):
    #Dict_TaxName_TaxID={}
    #Dict_TaxID_TaxName={}
    #ScientificNames=[]
    Dict_TaxID_ScientificNames={}
    Dict_ScientificNames_TaxID={}
    Dict_Synonyms_TaxID={}
    f_TaxNames=open(NCBITaxonomyPath+'names.dmp','r')
    for line in f_TaxNames:
        l=line.split('\t')
        tax_id=l[0]
        name_txt=l[2]
        #uniqueName=l[4]
        className=l[6]
        if className =='scientific name':
            #ScientificNames.append(name_txt)
            Dict_TaxID_ScientificNames[tax_id]=name_txt
            Dict_ScientificNames_TaxID.setdefault(name_txt,[]).append(tax_id)
        elif className=='synonym':
            Dict_Synonyms_TaxID.setdefault(name_txt,[]).append(tax_id)
            #Dict_Synonyms_TaxID.setdefault(tax_id,[]).append(name_txt)
        elif className=='equivalent name':
            Dict_Synonyms_TaxID.setdefault(name_txt,[]).append(tax_id)
            #Dict_Synonyms_TaxID.setdefault(tax_id,[]).append(name_txt)
        #Dict_TaxName_TaxID.setdefault(name_txt,[]).append(tax_id)
        #Dict_TaxID_TaxName.setdefault(tax_id,[]).append(name_txt)
    f_TaxNames.close()
    #return Dict_TaxName_TaxID, Dict_TaxID_TaxName, ScientificNames, Dict_TaxID_ScientificNames
    return Dict_ScientificNames_TaxID, Dict_Synonyms_TaxID, Dict_TaxID_ScientificNames

tx_n_Id=getTaxID_SynNames(NCBI_taxonomy_Path)
SciName_TaxId=tx_n_Id[0]
Synonyms_TaxId=tx_n_Id[1]
TaxID_ScientificNames=tx_n_Id[2]

def get_Taxid_lineage():
    TaxidLineageFile=NCBI_taxonomy_Path+'taxidlineage.dmp'
    D_Taxid_lineage={}
    D_lineage_Taxid={}
    f_taxidlin=open(TaxidLineageFile,'r')
    for line in f_taxidlin:
        l=line.split('\t|\n')[0].split('\t|\t')
        TaxId=l[0].strip()
        #Org_taxid=l[1]
        lineage_Txid=l[1].strip()
        D_Taxid_lineage[TaxId]=lineage_Txid+' '+TaxId
        D_lineage_Taxid[lineage_Txid]=TaxId
    f_taxidlin.close()
    return D_Taxid_lineage, D_lineage_Taxid

T=get_Taxid_lineage()
Taxid_Lineages=T[0]
Lineages_Taxid=T[1]

def get_SpeciesNodes(f_Nodes_NCBI):
    D_TaxId_True={}
    D_OtherRanks_TaxIds={}
    D_TaxidsAll_True={}
    R=['phylum', 'class', 'order', 'family', 'genus']
    f=open(f_Nodes_NCBI, 'r')
    for line in f:
        l=line.split('\t')
        TxId=l[0]
        Sp=l[4]
        if Sp=='species':
            D_TaxId_True[TxId]=True
            D_TaxidsAll_True[TxId]=True
        elif Sp in R:
            D_OtherRanks_TaxIds[TxId]=Sp
            D_TaxidsAll_True[TxId]=True
        else:
            continue
    f.close()
    return D_TaxId_True, D_OtherRanks_TaxIds, D_TaxidsAll_True

S=get_SpeciesNodes(Nodes_NCBI)
SpeciesNodes=S[0]
OtherRanks=S[1]
MainRanks_Taxids=S[2]



def get_SpeciesNames(Taxon_RankKingdom, SciName_TaxId, TaxID_ScientificNames, SpeciesNodes, OtherRanks, Taxid_Lineages, Synonyms_TaxId):
    Sps_Taxids={}
    for taxon_temp in Taxon_RankKingdom:
        taxon=' '.join(taxon_temp.split('\t')[-2:])
        taxRank=Taxon_RankKingdom[taxon_temp][0]
        #print taxRank
        taxKingdom=Taxon_RankKingdom[taxon_temp][1]
        #print taxKingdom
        #taxon_txid=SciName_TaxId[taxon][0] #here we think that the taxon has only one taxid. For multiple match we implement it later
        #print taxon_txid
        kingdom_txid=SciName_TaxId[taxKingdom][0]
        #print kingdom_txid
        if SciName_TaxId.has_key(taxon):
            TaxonTaxID=SciName_TaxId[taxon]
            if len(TaxonTaxID)==1:
                Sps_Taxids[taxon_temp]=TaxonTaxID[0]
        elif Synonyms_TaxId.has_key(taxon):
            TaxonTaxID_Syn=Synonyms_TaxId[taxon]
            if len(TaxonTaxID_Syn)==1:
                Sps_Taxids[taxon_temp]=TaxonTaxID_Syn[0]
        else:
            Sps_Taxids[taxon_temp]='NA'
    return Sps_Taxids

speciesTaxIDs=get_SpeciesNames(Taxon_RankKingdom, SciName_TaxId, TaxID_ScientificNames, SpeciesNodes, OtherRanks, Taxid_Lineages, Synonyms_TaxId)

print speciesTaxIDs

def write_Taxonomy_withSpeciesTaxIDs(speciesTaxIDs, f_out_Syno, HEADERS):
    f_out=open(f_out_Syno, 'w')
    f_out.write(HEADERS+'\tNCBI_TaxID\n')
    for sp in speciesTaxIDs:
        f_out.write(sp+'\t'+speciesTaxIDs[sp]+'\n')
    f_out.close()

W=write_Taxonomy_withSpeciesTaxIDs(speciesTaxIDs, f_out_Syno, HEADERS)








