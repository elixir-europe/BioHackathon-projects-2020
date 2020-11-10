#!/usr/bin/env bash

python3 "./V-pipe/scripts/assemble_visualization_webpage.py" \
    --consensus "./data/ref_majority.fasta" \
    --coverage "./data/coverage.tsv.gz" \
    --vcf "./data/snvs.vcf" \
    --gff "./V-pipe/references/gffs/" \
    --template "./V-pipe/scripts/visualization.html" \
    --wildcards "260005_918_H09-20200914_JB26N" \
    --output "./report.html"
