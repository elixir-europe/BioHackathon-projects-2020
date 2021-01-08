# Bioschemas Knowledge Graph Data Model



## Wikidata Model

Convert data to common identifier scheme for specific entity type, and store in a common graph.

### Advantages

- Tracks where each statement has come from
  - Supports ranking statements
  - Supports richer metadata at a statement level
- Requires additional vocabularies and many more triples
- Enables direct querying of the knowledge in simpler way
- Updating more complex as data is scattered throughout the graph



## Open PHACTS Approach

Convert data to common identifier scheme for specific entity type. Store in a graph per data source.

### Advantages

- Provenance tracking at the graph level
  - Is this sufficient for our needs?
- Queries need to perform the union of graphs
- Updating more straightforward; drop and replace whole graph 