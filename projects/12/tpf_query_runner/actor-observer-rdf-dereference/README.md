# Comunica Example: Observe all received RDF triples

This is an example [Comunica](https://github.com/comunica/comunica) package where all RDF triples that are received
by the engine are counted.
This is done by creating an [`ActionObserver`](https://github.com/comunica/comunica/blob/master/packages/core/lib/ActionObserver.ts)
for the [`rdf-dereference` bus](https://github.com/comunica/comunica/tree/master/packages/bus-rdf-dereference).

Concretely, this example package does the following:
* **Required:** Implementation of an observer that will listen on the `rdf-dereference` bus: `lib/MyActionObserverRdfDereference.ts`
* **Required:** Comunica config with our custom observer: `config/config-default.json`
* **Optional:** Run script for using the observer with a query: `bin/run.ts`

The remainder of this README contains several pointers on how this package is constructed.

## Package Overview

### Observer implementation

Comunica allows so-called _observers_ to be attached to any of its buses.
These observers will then be able to see which actions are being executed on the bus,
together with their output, and the actor that has executed it.

When creating an observer, you first have to determine which bus you want to subscribe to.
Buses in comunica are [packages that start with `bus-`](https://github.com/comunica/comunica/tree/master/packages).

In our case, we want to listen to RDF dereference actions,
so we pick the [`rdf-dereference` bus](https://github.com/comunica/comunica/tree/master/packages/bus-rdf-dereference).

All observers must implement the [`ActionObserver` interface](https://github.com/comunica/comunica/blob/master/packages/core/lib/ActionObserver.ts).
Our implementation can be found in `lib/MyActionObserverRdfDereference.ts`.
Make sure to export this class from `index.ts`, so that this class can be instantiated later on.

### Configs

Similar to the [tutorial on creating a custom Comunica actor](https://github.com/comunica/Tutorial-Comunica-Reduced-Actor/wiki/Comunica-tutorial:-Creating-a-REDUCED-actor),
we define a `MyActionObserverRdfDereference` component in the `components/` folder.
This will make it possible to refer to this component from within our config file.

In this example, we make use of the default Comunica SPARQL config,
and we just add an instance of our observer to it.

For this, we have a `config/config-default.json` file,
where we _import_ the [default Comunica SPARQL config `"files-cais:config/config-default.json"`](https://github.com/comunica/comunica/blob/master/packages/actor-init-sparql/config/config-default.json),
and we import a local configuration file `"files-ex:config/sets/rdf-deference-observer.json"`.

This local configuration file resides in `config/sets/rdf-dereference-observer.json`,
which just contains an instance of `MyActionObserverRdfDereference`. 

### Run script

`bin/run.ts` contains logic to instantiate our engine and observer,
execute a simple query, and log the observed output to stdout.
