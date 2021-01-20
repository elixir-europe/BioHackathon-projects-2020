#!/usr/bin/env node
"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const Setup = require("@comunica/runner-cli");
const fs = require('fs');
const util = require('util');
(async function () {
    // Instantiate a Comunica runner, this will instantiate all components in the given config-default.json.
    // Typically, this happens behind the scenes when calling newEngineDynamic, which will return the SPARQL engine actor.
    // However, since we not only need access to the SPARQL engine, but also our custom observer,
    // we need access to the runner instance, so that we can retrieve the SPARQL engine and our observer from it.
    const runner = await Setup.instantiateComponent(__dirname + '/../config/config-default.json', 'urn:comunica:my', // The IRI of the runner, as defined in config-default.json
    { mainModulePath: __dirname + '/../' }); // The path to the root module, so that the setup code can find our new observer component
    // Retrieve the SPARQL engine and observer instances from our runner.
    const { engine, observer } = runner.collectActors({
        engine: 'urn:comunica:sparqlinit',
        observer: 'urn:observer:my',
    });
    const args = process.argv;
    //console.log('args 0' + args[0])
    //console.log('args 1' + args[1])
    //console.log('args 2' + args[2])
    //console.log('args 3' + args[3])
    //console.log('args 4' + args[4])
    const endpoint = args[2];
    const queryfile = args[3];
    var query = "";
    console.log('getting ' + queryfile);
    console.log('endpoint ' + endpoint);
    const readFileContent = util.promisify(fs.readFile);
    const fetchFile = async (path) => {
        // The readFileContent() method reads the file 
        // and returns buffer form of the data  
        const buff = await readFileContent(path);
        const querystr = buff.toString();
        //console.log(`\nContents of the QUERY file :\n${querystr}`)
        return querystr;
    };
    fetchFile(queryfile)
        .then(async (querystr) => {
        //console.log(`\nContents of the QUERY in then :\n${querystr}`);
        query = querystr;
        // Execute a SPARQL query using our engine.
        const result = await engine.query(query, { sources: [endpoint] });
        // Handle the query results in a streaming manner
        let js = [];
        let results = 0;
        result.bindingsStream.on('data', (data) => results++);
        result.bindingsStream.on('end', () => {
            // Wait a bit, as there may still be buffered actions (TODO: fix this in Comunica so that actions are aborted once query exec ends)
            setTimeout(() => {
                // Print stats to stdout
                console.log('Query results: ' + results);
                console.log('HTTP requests: ' + observer.urls.length);
                observer.quadss.forEach(function (q) {
                    js.push(JSON.parse(q));
                });
                js.forEach(function (j) {
                    //console.log(j.graph.termType);
                    if (j.graph.termType == "NamedNode") {
                        return;
                    }
                    process.stdout.write(j.subject.value + "|||" + j.predicate.value + "|||" + j.object.value + "\n");
                });
            }, 100);
        });
    });
})();
//# sourceMappingURL=run.js.map