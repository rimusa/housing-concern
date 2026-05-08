# Data Card

This datacard is based on the template used to document the resources that form part of SuperLim.
Said template can be found [here](https://github.com/spraakbanken/SuperLim).


## 1. Identifying Information

### General Information

- **Title:** Housing Market Concern
- **Subtitle:** A dataset with annotations, prompts, and processing code for Reddit comments for concern over housing security and affordability
- **Created by:** Emilie Francis, Céline Leuzinger, Ricardo Muñoz Sánchez, Lee Gauthier
- **Publisher(s):** N/A
- **License(s):** CC0 1.0 Universal
- **Funded by:** N/A
- **Link(s)/permanent identifier(s):**
    - https://github.com/rimusa/housing-concern


### Abstract

There is a housing affordability crisis in many cities, but perspectives on what constitutes housing affordability/availability differ.
Large language models (LLMs) have often been proposed as substitutes for human annotators in a variety of tasks.
In parallell, there has been increased focus on the role that human subjectivity and perspective plays in data annotation.
To avoid eliminating the human role in annotation entirely, the use of LLMs for pre-annotation has been suggested as an alternative approach.
This dataset was created to explore differences stemming between human-only annotation and the usage of LLMs for pre-annotation.

The data was gathered from Reddit comments from six English speaking countries identified among the top locales for housing cost burden in OECD reports: U.S.A., Canada, U.K., Ireland, Australia, and New Zealand.
For each country, we select the largest two cities by population and collect threads from the local subforums (subreddits) from [the Reddit PushShift Dataset](https://ojs.aaai.org/index.php/ICWSM/article/view/7347).
All comments are in English, dating from 2013 to 2023.


### Citation
> Emilie Francis, Céline Leuzinger, Ricardo Muñoz Sánchez, Lee Gauthier. 2026. ChatGPT, why can't anyone afford a house? On the Effects of LLM pre-annotation on Annotator Subjectivity. In Proceedings of the 5th Workshop on Perspectivist Approaches to NLP, Palma de Mallorca, Spain. Association for Computational Linguistics.


## 2. Usage	

- **Key applications:** [More Information Needed]
- **Intended task(s)/usage(s):** [More Information Needed]
- **Recommended evaluation measures:** [More Information Needed]
- **Dataset function(s):** [More Information Needed]
- **Recommended split(s):** [More Information Needed]


## 3. Data	

- **Primary data:** Text
- **Language:** English


### Dataset in numbers

3,000 sets of annotations, released both in a standardised and a nonstandardised version, for a total of 6,000 sets of annotations.


### Nature of the content

[More Information Needed]


### Format

CSV files where each row is a set of annotations.
There are four of such files in the ```Annotations``` directory.
Those with the prefix ```human``` contain the annotations for the human-only setup (i.e. without any LLM involvement).
Those with the prefix ```llm``` contain the annotations for the LLM-asisted setup (i.e. an LLM was used for pre-annotation, the output of which was given to the annotators).
For each of those setups there is a standardised or cleaned-up version for ease of analysis (```standard```) and one that maintains all labels and annotations by the annotators (```nostandard```).

Each CSV file has the following columns:
- **annotator:** the annotator for the labels within that row, denoted as one of A, B, or C. Note that the same letters were used for the same annnotators across files.
- **cause_exacerbate:** aspects that are claimed to exacerbate issues of affordability in the housing market. The same comment may mention multiple factors. See the annotation guidelines for more information.
- **cause_improve:** aspects that are claimed to improve affordability in the housing market. The same comment may mention multiple factors. See the annotation guidelines for more information.
- **concern:** a numerical value denoting the level of concern about the status of affordability in the housing market. The potential values are as follows:
  - **0:** off-topic
  - **1:** no concern
  - **2:** mixed
  - **3:** concern
- **factor:** aspects that comments use to measure or evaluate affordability of housing. The same comment may mention multiple factors. See the annotation guidelines for more information.
- **id:** the id of the comment in [the Reddit PushFit Dataset](https://ojs.aaai.org/index.php/ICWSM/article/view/7347). Note that we _do not_ include the comments themselves, so these are necessary to make the annotations match with the proper comment.
- **month:** month in which the original comment was published, as an integer.
- **subreddit:** subreddit from which the original comment comes from. They all correspond to a city.
- **year:** year in which the original comment was published.


### Data source(s)

Comments from [the Reddit Pushfit Dataset](https://ojs.aaai.org/index.php/ICWSM/article/view/7347).


### Data collection method(s)

Not applicable, the data was sourced from a previously existing dataset.


### Data selection and filtering

[More Information Needed]


### Data preprocessing

[More Information Needed]


### Data labeling

The annotation procedure followed the perspectivist paradigm (Basile et al., 2020; Cabitza et al., 2023). That is, we kept all labels and did not aggregate annotations in any manner.
The dataset includes four categories of labels: concern score, factor, aspect-improve, and aspect-exacerbate.
- Two categories (concern score and factor) are prescriptive labels based on the More Effective Social Protection for Stronger Economic Growth Survey and Building for a better tomorrow: Policies to make housing more affordable Brief reports from the OECD, respectively.
- The remaining two categories (aspect-improve and aspect-exacerbate) were developed in a collaborative document using open coding (Khandkar, 2009)

There were two different setups for the data labeling process:
- **human-only:** these annotations were created by humans, without any LLM involvement.
- **LLM-assisted:** an LLM was used for pre-annotation, which was then given to the same set of annotators as in the human-only setup.


### Annotator characteristics

Annotation was carried out by a team of three volunteers, each of which have spent one or more years living in one of the cities in the study.
Two annotators are women in their late 20s to early 30s from a middle-class background in mid-sized cities, while the third is a man in his thirties from a small-town working class background.


## 4. Ethics and Caveats	

### Ethical considerations

First, all annotators involved in the project were given authorship on the paper as compensation for their contributions.

There are two main considerations that come into play regarding the data used for these experiments:

- Although we have taken steps to anonymize comments by removing clear PII, it is incredibly challenging to control for all information that has the potential to identify individuals. Data de-identification is still an open problem, with multiple considerations that must be taken in mind.
- Even though all comments are freely viewable on public facing forums, the comment authors did not give informed consent for their data to be used for research purposes. Because of this, we opted not to re-publish raw text from the resulting dataset in a public forum. 


### Things to watch out for

[More Information Needed]


### 5. About Documentation	

- **Data last updated:** [More Information Needed]
- **Which changes have been made, compared to the previous version:**
    - None, this is the first iteration of the dataset
- **Access to previous versions:** N/A
- **This document created:** 2026-05-08
- **This document last updated:** 2026-05-08
- **Where to look for further details:** The original paper and the annotation guidelines
- **Documentation template version:** [1.0](https://github.com/spraakbanken/SuperLim/blob/main/documentation_sheet_template_v1.0.tsv)


### 6. Other	

- **Related projects:** N/A
- **References:**
    1. [More Information Needed]
