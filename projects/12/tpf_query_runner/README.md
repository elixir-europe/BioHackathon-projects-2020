this goes into: comunica/packages 
docker build is in: comunica/packages/actor-init-sparql 
entrypoint: ENTRYPOINT ["node",  "../actor-observe-rdf-dereference/bin/run.js", "http://fairdata.systems:5000/fairdata-tfs", "/queries/query2"]

so (for now) create a folder "queries", put your query in "query2", mount that inside the docker image as "/queries/" 

