#import entrez library
from Bio import Entrez
#other:
import tempfile
import os
import glob
import shutil
import time
import datetime
from urllib.error import HTTPError
import pandas as pd
import readline
from ete3 import NCBITaxa
import math
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles, venn2_unweighted
from collections import Counter
import requests
import numpy as np
import io
from  more_itertools import unique_everseen
from Bio import SeqIO

#variables necessary for the script functions:
pd.options.mode.chained_assignment = None

#complete lines with tab:
readline.parse_and_bind('tab: complete')
readline.set_completer_delims(' \t\n')

def clear():
    os.system('tput reset')

#fetch taxid sequence release from ENA-EBI:
def fetch_taxid(taxid):
    url=f"https://www.ebi.ac.uk/ena/portal/api/links/taxon?accession={taxid}&format=json"
    r = requests.get(url)
    r.raise_for_status()
    listJSON=r.json()
    dictsequence=[d for d in listJSON if d["result_id"] == "sequence"] ###perchè non sequence???
    #print(dictsequence)
    number=dictsequence[0]['entry_cnt']
    return int(number)

#fetch accessions from ENA
def get_accessionENA(taxid,limit):
    url=f"https://www.ebi.ac.uk/ena/portal/api/search?result=sequence&query=tax_eq({taxid})&fields=accession&limit={limit}&format=json"
    r = requests.get(url)
    r.raise_for_status()
    listJSON=r.json()
    return listJSON

def get_GenBankENA(accession):
    url=f"https://www.ebi.ac.uk/ena/browser/api/text/{accession}"
    r = requests.get(url)
    r.raise_for_status()
    genbank = r.text
    return genbank

def main_menu():
    print("\n Welcome to ENA query tool:\n")
    print("\n Choose one of the following: \n")
    print(" 1 - Download accessions function")
    print(" 2 - Get country ang gene information from GenBank")

    while True:
        try:
            module = int(input(">> Enter the number of the chosen function: "))
            if module not in (1, 2):
                print("Error, enter a valid choice!")
                continue
            break
        except ValueError:
            print("Wrong input, expected a numeric input, try again.")

    clear()

    if module == 1:
        get_accession()

    if module == 2:
        get_CountryGene()

def get_accession():
    print("\n ---DOWNLOAD ACCESSION FROM ENA---\n")
    file_manual=input(str("Do you want to find ACCESSIONS through a file or manual input? (f > file, m > manual)"))
    while len(file_manual) <= 0 or file_manual[0] not in ("f", "F", "m", "M"):
        print("Wrong input, write <f> for csv or <m> for manual! (Without <>)\n")
        file_manual = input(
            "Do you want to find ACCESSIONS through a file or manual input? (f > file, m > manual)")

    if file_manual[0] in ("m", "M"):

        query_taxid = input(str("\nEnter your chosen TAXID (e.g 9606 for Homo Sapiens):"))
        taxid = int(query_taxid)

        total_sequence = fetch_taxid(query_taxid)
        print(f"\nNumber of sequences found for txid{query_taxid}: " + str(total_sequence))

        limit_query = input(str("\nEnter the number of accessions to retrieve (enter 0 for all) :"))
        limit = int(limit_query)
        manual_json=get_accessionENA(taxid,limit)
        df_m_accession = pd.DataFrame.from_records(manual_json)
        df_m_accession.insert(loc=0, column='taxid', value=query_taxid)
        df_m_accession.to_csv(f'TAXID{query_taxid}_accession.tsv',sep='\t', index=False)
        print("\nWORK DONE!!!!")

    if file_manual[0] in ("f", "F"):

        tax_tsv = input(str("\nEnter your tsv with taxids:"))
        #df_tax = pd.read_csv(tax_tsv, sep='\t',names=['taxid'])
        df_tax = pd.read_csv(tax_tsv, sep='\t',header=0)
        df_F_accession = pd.DataFrame()
        limit = 0
        #for taxid in df_tax['taxid']:
        for taxid in df_tax['NCBI_TaxID']:
            try:
                file_json=get_accessionENA(taxid,limit)
                df_f_accession = pd.DataFrame.from_records(file_json)
                df_f_accession.insert(loc=0, column='NCBI_TaxID', value=taxid)
                df_F_accession=pd.concat([df_F_accession, df_f_accession], ignore_index=True)
            except ValueError as err:
                print(f"\nJSON error for taxid: {taxid}")
                continue

        final_df = pd.merge(df_tax, df_F_accession,  how='left', on= ['NCBI_TaxID'])
        output_name = tax_tsv.split('.')[0]
        final_df.to_csv(f'TAXID_{output_name}_accession.tsv',sep='\t', index=False)
        print("\nWORK DONE!!!!")

def get_CountryGene():
    print("\n ---DOWNLOAD COUNTRY AND GENE INFORMATION FROM ENA---\n")

    '''# single query, BETA
    acc = input(str("\n Enter your accession:"))
    gb = get_GenBankENA(acc)
    print(gb)
    print(type(gb))
    listGENE = []
    listCOUNTRY = []
    listAcc = []
    str_acc = io.StringIO(gb)
    for line in str_acc:
        if line.startswith(("AC","FT")):
                newline=line.replace("\n", ",").strip()
                listAcc.append(newline)
    #print(listAcc)

    listCountryGene = [elem for elem in listAcc if "/country=" in elem or "/gene=" in elem ]
    listCountryGene = list(unique_everseen(listCountryGene))

    if "/country=" not in str(listCountryGene[:]):
        listCountryGene.insert(1,str("Missing country"))

    if "/gene=" not in str(listCountryGene[:]):
        listCountryGene.append("None")

    listGENE.append(listCountryGene[0])
    listCOUNTRY.append(listCountryGene[-1])
    print(listCountryGene)
    print(listGENE)
    print(listCOUNTRY)


    acc_tsv = input(str("\nEnter your tsv with Accessions:"))
    df_acc = pd.read_csv(acc_tsv, sep='\t',header=0)
    listGENE = []
    listCOUNTRY = []

    for accession in df_acc["accession"]:
        if accession == '' or pd.isnull(accession):
            print("\nNO ACCESSION FOUND")
            listGENE.append("Missing gene")
            listCOUNTRY.append("Missing country")
            continue

        else:
            gb = get_GenBankENA(accession)
            listAcc = []
            str_acc = io.StringIO(gb)

            for line in str_acc:
                if line.startswith(("AC","FT")):
                        newline=line.replace("\n", ",").strip()
                        listAcc.append(newline)

            listCountryGene = [elem for elem in listAcc if "/country=" in elem or "/gene=" in elem ]
            listCountryGene = list(unique_everseen(listCountryGene))

            print(listCountryGene)
            if "/country=" not in str(listCountryGene[:]):
                listCountryGene.insert(0,str("Missing country"))

            if "/gene=" not in str(listCountryGene[:]):
                listCountryGene.append("Missing gene")

            print(listCountryGene)
            listGENE.append(listCountryGene[-1])
            listCOUNTRY.append(listCountryGene[0])

    print(listGENE)
    print(listCOUNTRY)

    output_name = acc_tsv.split('.')[0].split('TAXID')[-1]
    df_acc['Country'] = np.nan
    df_acc['Country'] = listCOUNTRY
    df_acc['Gene'] = np.nan
    df_acc['Gene'] = listGENE
    df_acc["Country_cleaned"] = df_acc["Country"].str.findall( '"([^"]*)"').astype(str)
    df_acc["Gene_cleaned"] = df_acc["Gene"].str.findall( '"([^"]*)"').astype(str)
    df_acc.to_csv(f'ALL_METADATA_{output_name}_accession.tsv',sep='\t', index=False)
'''
    acc_tsv = input(str("\nEnter your tsv with Accessions:"))
    df_acc = pd.read_csv(acc_tsv, sep='\t',header=0)
    output_name = acc_tsv.split('.')[0].split('TAXID')[-1]

    try:
        os.makedirs(f"ACCESSION_{output_name}")
    except FileExistsError:
        print("Dir exist!")

    dir = f"ACCESSION_{output_name}"
    os.chdir(f"{dir}")

    gene = "NaN"
    country = "NaN"
    author = "NaN"
    journal = "NaN"
    list_dict = []

    for accession in df_acc["accession"]:
        if os.path.isfile(f'{accession}.txt'):
            print (f"File {accession}.txt exist")
            record = SeqIO.read(f"{accession}.txt" , "embl")

            for feature in record.features:
                 if feature.type=="CDS":
                     try:
                         gene = feature.qualifiers['gene'][0]
                     except KeyError:
                         gene = "NaN"
                         continue

            for feature in record.features:
                 if feature.type=="source":
                     try:
                         country = feature.qualifiers['country'][0]
                         specimen_voucher = feature.qualifiers['specimen_voucher'][0]
                     except KeyError:
                         country = "NaN"
                         specimen_voucher = "NaN"
                         continue


            seqAnn = record.annotations
            #seqAnn['references'][0].title
            print(record.records)
            author = record.annotations['references'][0].authors
            journal = record.annotations['references'][0].journal
            list_dict.append({'accession' : accession, 'author' : author, 'journal' : journal, 'gene' : gene, 'country' : country, 'specimen_voucher' : specimen_voucher})
            continue

        else:
            try:
                if accession == '' or pd.isnull(accession):
                    print("\nNO ACCESSION FOUND")
                    gene = "NaN"
                    country = "NaN"
                    author = "NaN"
                    journal = "NaN"
                    specimen_voucher = "NaN"
                    list_dict.append({'accession' : accession, 'author' : author, 'journal' : journal, 'gene' : gene, 'country' : country, 'specimen_voucher' : specimen_voucher })
                    continue

                else:
                    print(accession)

                    gb = get_GenBankENA(accession)
                    text_file = open(f"{accession}.txt", "w")
                    text_file.write(gb)
                    text_file.close()

                    record = SeqIO.read(f"{accession}.txt" , "embl")

                    for feature in record.features:
                         if feature.type=="CDS":
                             try:
                                 gene = feature.qualifiers['gene'][0]
                             except KeyError:
                                 gene = "NaN"
                                 continue

                    for feature in record.features:
                         if feature.type=="source":
                             try:
                                 country = feature.qualifiers['country'][0]
                                 specimen_voucher = feature.qualifiers['specimen_voucher'][0]
                             except KeyError:
                                 country = "NaN"
                                 specimen_voucher = "NaN"
                                 continue


                    seqAnn = record.annotations
                    #seqAnn['references'][0].title
                    author = record.annotations['references'][0].authors
                    journal = record.annotations['references'][0].journal
                    list_dict.append({'accession' : accession, 'author' : author, 'journal' : journal, 'gene' : gene, 'country' : country, 'specimen_voucher' : specimen_voucher})

            except KeyboardInterrupt:
                print("\nKeyboard interruption")
                alt=str(input("Continue?[y/n]:"))
                if alt[0]=='y':
                    continue
                else:
                    quit()

            except HTTPError as err:
                if 400 <= err.code <= 599:
                    print('\nConnection error: %s' % err)
                    time.sleep(60)

            except requests.exceptions.SSLError as err:
                print("Error...Max retries exceeded with url")
                time.sleep(60)

            except requests.exceptions.ConnectionError as err:
                print("Error...connection aborted, please wait")
                time.sleep(60)

    #print(list_dict)
    df_metadata = pd.DataFrame(list_dict)
    #print(df_metadata)
    mergeddf = df_acc.merge(df_metadata, on=['accession'],how='left')
    #print(mergeddf)
    mergeddf = mergeddf.drop_duplicates()
    mergeddf.to_csv(f'ALL_METADATA_{output_name}.tsv',sep='\t', index=False)


clear()
main_menu()

'''
print(record.annotations)
for ref in record.annotations["references"]:
    print(ref)
for ref in record.features:
    print(ref)
print(record.annotations['references'][0].collection_date)
'''
