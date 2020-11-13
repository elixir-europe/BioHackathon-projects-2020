yarn add @comunica/runner

docker build -t markw/comunica_watcher:0.0.1 .

entrypoint: ENTRYPOINT ["bash", "/entrypoint.sh"]

entrypoint.sh:
     #!/bin/bash

     if [[ $1 && $2 ]]; then
         node ./bin/run.js $1 $2
     fi

triples are separated by ||| and are output to STDOUT

so (for now) create a folder "queries", put your query in "queryxxx" (whatever name you wish), mount that inside the docker image as "/queries/" 

 docker run --rm   -v   $PWD/queries:/queries markw/comunica_watcher:0.0.1     http://fairdata.systems:5000/fairdata-tfs    /queries/queryxxx    >    testoutput
 
 if you dont' unclude a name, you can run this multiple times simultaneously
 
 