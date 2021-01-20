#!/bin/bash

if [[ $1 && $2 ]]; then
    node ./bin/run.js $1 $2
fi
