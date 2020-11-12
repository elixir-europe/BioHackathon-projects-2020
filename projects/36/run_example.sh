#!/usr/bin/env bash

sample="321458_1771_F07"  # "260005_918_H09"

python3 "./V-pipe/scripts/assemble_visualization_webpage.py" \
    --consensus "./data/$sample/ref_majority.fasta" \
    --coverage "./data/$sample/coverage.tsv.gz" \
    --vcf "./data/$sample/snvs.vcf" \
    --gff "./V-pipe/references/gffs/" \
    --template "./V-pipe/scripts/visualization.html" \
    --wildcards "$sample" \
    --output "./report.html"
