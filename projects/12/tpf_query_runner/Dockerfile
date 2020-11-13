FROM comunica/actor-init-sparql:latest

# Install location
ENV dir /var/www/@comunica/

# Copy the engine files (generated from package.json!files)
COPY . /var/www/@comunica/
#COPY ./actor-observer-rdf-dereference/* /var/www/@comunica/actor-observer-rdf-dereference/

# Run base binary (generated from package.json!bin)
ENV dir /var/www/@comunica/actor-observer-rdf-dereference/
COPY ./entrypoint.sh ${dir}/entrypoint.sh
WORKDIR ${dir}
#ENTRYPOINT ["node",  "./bin/run.js", "http://fairdata.systems:5000/fairdata-tfs", "/queries/query2"]
ENTRYPOINT ["bash",  "entrypoint.sh"]

