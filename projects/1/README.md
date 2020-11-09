# Project 1: Follow-up analysis on BioHackathon-Europe outcomes

## Schedule for the BioHackathon Europe week
* Brainstorming meeting on Remo: Tuesday 9:00 UTC = 10:00 CET = 18:00 Japan

## Abstract

One of the recurring questions when it comes to BioHackathons is how to measure their impact. In order to do so, we first need to understand the outcomes from a BioHackathon. Some possible outcomes are software, publications and collaborations. Such outcomes could be analyzed from activity post-hackathon on GitHub repositories as well as publications generated out of BioHackathon topics. For the particular case of the BioHackathon-Europe, which has been running only for two years now, we propose to focus on GitHub activity post-BioHackathon. We want to learn about what happens with the BioHackathon GitHub repos after the hacking days. Some of the questions we want to answer are: do BioHackathon GitHub repositories follow minimum open science recommendations w.r.t. research software? Do attendees continue working on BioHackathon GitHub proposals? If there is some continuance, for how long does it persist? In order to better shape our proposal to the BioHackathon-Europe outcomes analysis needs, we want to take advantage of the hacking days to brainstorm with organizers and attendees to define what and how outcomes should be targeted and analyzed. After this stage, we will start with the data model and data gathering by using the GitHub API. Data will be stored in the form of a knowledge graph so we can later apply some graph-based data analytics combined with machine learning approaches as well as integrate additional data coming from scholarly publications. We aim to create a comprehensive view of BioHackathon outcomes so we can better assess their impact on both research and community.

## Topics

* Data Platform
* Interoperability Platform
* Machine learning
* Tools Platform

**Project Number:** 1

**EasyChair Number:** 1

## Team

### Lead(s)

* Leyla Jael Garcia Castro <ljgarcia@zbmed.de> * corresponding author
* Dietrich Rebholz-Schuhmann <rebholz-schuhmann@zbmed.de>

### Participants

* Interested in brainstorming
  * Terue Takatsuki
  * Corinne Martin
  * Are you interested? Ping me on Slack at #BioHackOutcomes
  
* Interested in development
  * Benjamin Wolff
  * Georgi Lazarov
  * Are you interested? Ping me on Slack at #BioHackOutcomes

## Expected outcomes 

Note: we are starting from zero --sort of

* Brainstorming
  * Initial assessment on what BioHackathon-Europe outcomes should be targeted
    * From GitHub (this project)
    * Beyond GitHub (future work)
  * Initial assessment on what analyses should be performed
    * From GitHub (this project)
    * Beyond GitHub (future work)
  * Preliminary data model
    * From GitHub (this project)
    * Beyond GitHub (future work)
  
* Development  
  * Preliminary data model
  * Initial metadata extraction from GitHub
    * Let's try first with the BioHackathon project repository 
    * Let's go later for repositories belongin to people added as members of the BioHackathon projects repository
    * We want to get a prototype on data gathering from GitHub
  * How can we browse/view/analyze the gathered metadata?
    * Representation on a knowledge graph with query capabilities
    * Data on Elastic Search with some basic search functionality
    * Some graphics or plots to get a general idea on what we have there

## Expected audience

* People who has participated in a BioHackathon and interested in following up software outcomes from it
* People with some knowledge on software citation and versioning on GitHub
* People with some knowledge on GitHub API
* People with some knowledge on RDF triple stores or other graph databases

**Number of expected hacking days**: 4 days


### GitHub repo and development

* https://github.com/zbmed/BioHackOutcomes
* Let's work in Python (Jupyter notebooks or Python files, TBD)
* Some projects that might be useful
  * https://github.com/KnowledgeCaptureAndDiscovery/somef
  * https://github.com/weso-edma/hercules-challenge-git

