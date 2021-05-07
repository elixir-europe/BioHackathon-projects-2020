import os,sys

'''
pwd /home3/bbalech/DBs/Taxonomy/NCBI/Update_101120/
mkdir new_taxdump
cd /home3/bbalech/DBs/Taxonomy/NCBI/Update_101120/new_taxdump/
wget ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/new_taxdump/new_taxdump.tar.gz
gunzip new_taxdump.tar.gz
tar -xf new_taxdump.tar 
'''

'''
1- taxid of rhinolophus
2- query taxidlineages and get the organism name where the Rhinolophus taxid is present
3- ensure the taxid is in SpeciesNodes
4- get the name from TaxID_ScientificNames
'''



NCBI_taxonomy_Path='/home3/bbalech/DBs/Taxonomy/NCBI/Update_101120/new_taxdump/'

Nodes_NCBI= NCBI_taxonomy_Path+'nodes.dmp'


f_in_taxa=sys.argv[1]

def get_taxa(f_in_taxa):
    D_Taxon_RankKingdom={}
    f=open(f_in_taxa,'r')
    f.readline()
    for line in f:
        l=line.strip().split('\t')
        Taxon2Search=l[0]
        TaxonRank=l[1]
        TaxonKingdom=l[2]
        D_Taxon_RankKingdom[Taxon2Search]=[TaxonRank,TaxonKingdom]
    f.close()
    return D_Taxon_RankKingdom

Taxon_RankKingdom=get_taxa(f_in_taxa)
print Taxon_RankKingdom

def taxonomyLevelsNum():
    D_TaxonomyLevelsNum={}
    TaxR='phylum,class,order,family,genus,species'
    TaxRanks=TaxR.split(',')
    for i,n in enumerate(TaxRanks):
        D_TaxonomyLevelsNum[n]=i
    return D_TaxonomyLevelsNum

taxonomyLevelsNum=taxonomyLevelsNum()


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
            #Dict_Synonyms_TaxID.setdefault(name_txt,[]).append(tax_id)
            Dict_Synonyms_TaxID.setdefault(tax_id,[]).append(name_txt)
        elif className=='equivalent name':
            #Dict_Synonyms_TaxID.setdefault(name_txt,[]).append(tax_id)
            Dict_Synonyms_TaxID.setdefault(tax_id,[]).append(name_txt)
        #Dict_TaxName_TaxID.setdefault(name_txt,[]).append(tax_id)
        #Dict_TaxID_TaxName.setdefault(tax_id,[]).append(name_txt)
    f_TaxNames.close()
    #return Dict_TaxName_TaxID, Dict_TaxID_TaxName, ScientificNames, Dict_TaxID_ScientificNames
    return Dict_ScientificNames_TaxID, Dict_Synonyms_TaxID, Dict_TaxID_ScientificNames

tx_n_Id=getTaxID_SynNames(NCBI_taxonomy_Path)
SciName_TaxId=tx_n_Id[0]
Synonyms_TaxId=tx_n_Id[1]
TaxID_ScientificNames=tx_n_Id[2]

print SciName_TaxId['Rhinolophus']


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

print len(Lineages_Taxid)

def get_SpeciesNames(Taxon_RankKingdom, SciName_TaxId, TaxID_ScientificNames, SpeciesNodes, OtherRanks, Taxid_Lineages, Synonyms_TaxId):
    Sps_Taxids={}
    for taxon in Taxon_RankKingdom:
        taxRank=Taxon_RankKingdom[taxon][0]
        print taxRank
        taxKingdom=Taxon_RankKingdom[taxon][1]
        print taxKingdom
        taxon_txid=SciName_TaxId[taxon][0] #here we think that the taxon has only one taxid. For multiple match we implement it later
        print taxon_txid
        kingdom_txid=SciName_TaxId[taxKingdom][0]
        print kingdom_txid
        if OtherRanks[taxon_txid]==taxRank:
            for L in Taxid_Lineages:
                L_temp=Taxid_Lineages[L]
                L1=L_temp.split()
                #print L, L1
                if taxon_txid in L1 and kingdom_txid in L1:
                    #PotentialTaxID=L
                    if L in SpeciesNodes:
                        Sps_Taxids.setdefault(L, []).append(TaxID_ScientificNames[L])
    f_out=open(taxon+'_species_ScientificNames.tsv','w')
    f_out.write('SpeciesName\tNCBI_Synonyms\tNCBI_TaxID\n')
    for tid in Sps_Taxids:
        if tid in Synonyms_TaxId:
            Syno=';'.join(Synonyms_TaxId[tid])
            f_out.write(','.join(Sps_Taxids[tid])+'\t'+Syno+'\t'+tid+'\n')
        else:
            f_out.write(','.join(Sps_Taxids[tid])+'\t'+'NA'+'\t'+tid+'\n')
    f_out.close()
    return Sps_Taxids

Sps=get_SpeciesNames(Taxon_RankKingdom, SciName_TaxId, TaxID_ScientificNames, SpeciesNodes, OtherRanks, Taxid_Lineages, Synonyms_TaxId)



