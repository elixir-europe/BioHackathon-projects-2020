import os

import gffpandas.gffpandas as gffpd


def append_line(fname, tid, entry):
    fname_out = f'{fname}.mod'

    match = f'transcript_id "{tid}"'

    with open(fname, 'r') as fd_inp, open(fname_out, 'w') as fd_out:
        for line in fd_inp:
            app = ''
            if match in line:
                # print(match, line)
                app = f'UNIPROT "{entry}";'

            if 'UNIPROT' in line:
                print('Warning, duplicate UNIPROT associations')
                app = ''

            fd_out.write(f'{line.rstrip()} {app}'.rstrip() + '\n')

    os.replace(fname_out, fname)


def main(map_file, gtf_file):
    df_gtf = gffpd.read_gff3(map_file).df.reset_index()

    df_gtf['transcript_id'] = df_gtf['phase'].apply(lambda x: dict([e.split('=') for e in x.split(';')]).get('Note'))

    for row in df_gtf.itertuples():
        uniprot = row.index
        tid = row.transcript_id

        if tid is None:
            continue

        print(uniprot, tid)
        append_line(gtf_file, tid, uniprot)

if __name__ == '__main__':
    main(
        'data/Names_uniprot-sars-cov-2-filtered-organism__sars-cov-2_reviewed_yes.gff',
        'V-pipe/references/gffs/Sars-Cov2_Mature_products.gtf'
    )
