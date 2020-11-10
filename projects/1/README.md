# Project 1: Follow-up analysis on BioHackathon-Europe outcomes

## Schedule for the BioHackathon Europe week
* Brainstorming meeting on Remo: Tuesday 9:00 UTC = 10:00 CET = 18:00 Japan (4th floor, if table full, please send us a message on Slack)

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
  * https://melaniesoek0120.medium.com/how-to-use-github-api-to-extract-data-with-python-bdc61106a501

### BioHackthon ideas and planning

#### Brainstorming
* Tuesday 10.Nov.20
  * What impact can be assessed? Change (e.g., scientific advancement, difficult to measure) and performance (more feasible and possible from GitHub data)
  * Some analysis will come directly from the GitHub metadata, e.g., number of commits, forks, and so
  * Some predictions are also possible, e.g., a new contributor engaging during the BioHackathon could be because of the BioHackathon or could have happened in any case
  * There is a lot of metadata, let's start with some of it and later we will include more (when we figure out what can we get out of it)
  
#### Planning
* Parameters (to be set by hand)
  * BioHackathon year
  * Link to BioHackathon project
  * Dates when the events took place: bh_start_date, bh_final_date
  * Initial date for agregations: start_date (if ommited the created date of the analyzed repo will be used)
  * Final date for aggregations: final_date (if ommited "today" will be used)
* Let's focus on BioHackathon Europe GitHub repositories
  * 2019 Projects: https://github.com/elixir-europe/BioHackathon-projects-2019 
  * 2019 BioHackathon dates: 2019.11.18 - 2020.11.22
  * 2020 Projects: https://github.com/elixir-europe/BioHackathon-projects-2020
  * 2020 BioHackathon dates: 2020.11.09 - 2020.11.13
* For a given BioHackathon year (either 2019 or 2020 by now)
  * Let's get the projects out of the folder name "projects"
  * If there is any code in there, let's get metadata
  * If not, let's go through the readme.md file and find any GitHub repo mentioned there that is relevant for us
  * A GitHub repo is a link starting with github.com
  * A GitHub repo is relevant for us if it is a repo rather than an organization or user
  * For 2020 projects, double check that the repo **also** has the topic BioHackEU20 (non-case sensitive)
  * Extract metadata
    * Owner username
    * Repo title
    * Repo description
    * License
    * Creation date    
    * Contributor usernames and dates they joined
    * Total number of commits, downloads, forks, watch
      * between an initial date *start_date* and right before the starting date of the BioHackathon *bh_start_date*
      * during the BioHackathon days *bh_start_date* and *bh_final_date*
      * a given period *start_date* and *final_date*
  * Create dataframe with extracted metadata
      * Aggregate total number of contributors using the same date ranges as for commits and so
  
