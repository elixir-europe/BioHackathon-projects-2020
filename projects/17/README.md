# Project 17: Improve the support of Common Workflow Language in Galaxy

## Abstract

The field of bioinformatics has seen increasing use of the Common Workflow Language (CWL) standards to systematically describe computational pipelines. The 2018 ELIXIR Implementation Study “Enabling the reuse, extension, scaling, and reproducibility of scientific workflows” demonstrated how CWL tool and workflow descriptions can be shared and reused across different workflow executors and workflow management systems (e.g. Toil, Galaxy, CWLEXEC, Cromwell, etc.), addressing the assembly and functional annotation of transcriptomes from isolated marine eukaryotes.

One of the main tasks of this Implementation Study was to test the support for using these tool and workflow descriptions in Galaxy, using the fork of the Galaxy codebase created by John Chilton to add native CWL support to Galaxy. A number of modifications made in this fork have already been merged back in the main Galaxy repository, which has allowed us to identify gaps between the tool/workflow models of Galaxy and CWL that hinder this support, leading to potential improvements on both sides.

The first two BioHackathons allowed several different contributors to coordinate in person and discuss with the wider communities. This resulted in major portions of the CWL branch of Galaxy making their way into the core Galaxy project and we propose to continue that effort. Additionally, for the 2020 BioHackathon we will be working on a set of topics that both drive the project of implementing CWL inside of Galaxy forward but also are of broad interest to diverse other projects at the hackathon.

During the 2019 BioHackathon the [Galaksio project](https://github.com/elixir-europe/BioHackathon-projects-2019/tree/master/projects/19), along with other members of the Galaxy community, scoped out plans for a simplified, modern interface for running workflows in Galaxy - that work became a major development thrust of the Galaxy project and we propose to adapt CWL workflows executed in Galaxy to this new interface and evaluate it.

Another major thrust of last year’s hackathon was exporting workflow representations and workflow execution provenance. We will use this year’s event as an opportunity to synchronize efforts such as exporting abstract CWL representations of Galaxy workflows and Research Object-derived representations of Galaxy workflow runs (already the basis of the CWLProv specification).

Finally, version 1.2 of the CWL specifications should be released by the time of the event and are important to many ELIXIR projects, we therefore propose adapting the existing Galaxy work to these newer specifications and start work on prototyping CWL conditionals in Galaxy workflows. Our expectation is that implementing CWL 1.2 conditionals in Galaxy will both provide interesting insights to the CWL community as another implementation and would bootstrap an implementation of general conditionals in the Galaxy core that we expect would be merged quickly and benefit native Galaxy workflow execution independent of the CWL implementation.

## Topics

- Compute Platform
- EOSC-life
- Galaxy
- Interoperability Platform
- Marine Metagenomics
- Tools Platform

**Project Number:** 17



**EasyChair Number:** 26

## Team

### Lead(s)

- Nicola Soranzo <nicola.soranzo@earlham.ac.uk>
- Hervé Ménager <herve.menager@pasteur.fr>
- John Chilton <john.chilton@gmail.com>
- Michael Crusoe <mrc@commonwl.org>

### Nominated participant(s)

- Marius van den Beek <m.vandenbeek@gmail.com>
- Nicola Soranzo <nicola.soranzo@earlham.ac.uk>

## Expected outcomes

- Implement CWL 1.2 conditionals in Galaxy
- Advance the merge of the separate branch into the upstream Galaxy repository to be part of the next release of Galaxy
- Implement a new "Simplified Workflow execution UI" in Galaxy
- Export Galaxy workflows to non-abstract CWL

## Expected audience

Software developers with either Python or Web Frontend development skills (especially JavaScript/Vue.js), with or without an initial experience of development in Galaxy and/or CWL.

**Number of expected hacking days**: 4

