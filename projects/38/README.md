# Project 38: panoptes: monitor computational workflows in real time

## Abstract

Bioinformaticians and data scientists, rely on computational frameworks (e.g. [snakemake](https://snakemake.readthedocs.io/en/stable/), [nextflow](https://www.nextflow.io/), [CWL](https://www.commonwl.org/), [WDL](https://software.broadinstitute.org/wdl/)) to process, analyze and integrate data of various types. Such frameworks allow scientists to combine software and custom tools of different origin in a unified way, which lets them reproduce the results of others, or reuse the same pipeline on different datasets. One of the fundamental issues is that the majority of the users execute multiple pipelines at the same time, or execute a multistep pipeline for a big number of datasets, or both, making it hard to track the execution of the individual steps or monitor which of the processed datasets are complete. [panoptes](https://github.com/panoptes-organization/panoptes) is a tool that monitors the execution of such workflows.

[panoptes](https://github.com/panoptes-organization/panoptes) is a service that can be used by:
- Data scientists, bioinformaticians, etc. that want to have a general overview of the progress of their pipelines and the status of their jobs
- Administrations that want to monitor their servers
- Web developers that want to integrate the service in bigger web applications

**Note:** [panoptes](https://github.com/panoptes-organization/panoptes) is in early development stage and the first proof of concept server supports [snakemake](https://snakemake.readthedocs.io/en/stable/) workflows.

Below is an example of panoptes in action:

[![Watch the video](https://img.youtube.com/vi/de-YSJmq_5s/hqdefault.jpg)](https://www.youtube.com/watch?v=de-YSJmq_5s)

## Topics

- Tools and compute
- Workflows

### Lead(s)

Foivos Gypas, foivos.gypas@fmi.ch, Friedrich Miescher Institute for Biomedical Research (FMI), Basel, Switzerland
Argyrios-Alexandros Gardelakos, agardelakos@gmail.com, Technical Universiry of Crete

### Participants

Georgios Kostoulas, Technical Universiry of Crete
Georgios Ntalaperas, Commodity Risk Management Expertise Centre
Dimitrios Rekoumis, Technical Universiry of Crete

## Expected outcomes

1. Expand the functionality of panoptes
2. Increase test coverage and improve CI/CD

Please have a look on the [issues section](https://github.com/panoptes-organization/panoptes/issues), follow the [contributing instructions](https://github.com/panoptes-organization/panoptes/blob/master/CONTRIBUTING.md) and please adhere to the [code of conduct](https://github.com/panoptes-organization/panoptes/blob/master/CODE_OF_CONDUCT.md).

## Expected audience

Useful skills related to the project:
- python
- flask
- javascript
- snakemake (or any other workflow management system)
- databases
- CI/CD
- APIs
- docker
- JWT

But anyone is very welcome!

**Number of expected hacking days**: 2-4