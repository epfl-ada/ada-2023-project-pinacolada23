# The Evolution of Actors Post-Blockbuster in the Film Industry

## Datastory

TODO: put the link here with a small sentence

## Abstract

This research project is designed to conduct a comprehensive analysis of the career trajectories of actors subsequent to their involvement in high-grossing films, utilizing the CMU Movie Dataset as the principal data source. The objective is to investigate the impact of significant box office success on an actor's subsequent professional choices and the trajectory of their career. The study will specifically focus on two key aspects: the progression in the variety of roles chosen by these actors after their blockbuster experiences, and the sustainability of their success at the box office. The aim is to identify patterns and trends within the film industry, shedding light on how commercial success influences the career decisions of actors. By delving into these dimensions, the project aspires to elucidate and articulate the narrative of success in the movie business and its enduring effects on actors' careers.


## Research questions
- Does a high-grossing film consistently lead to continued box office success for its actors in their subsequent films?
- Is there a noticeable change in the genre or type of characters portrayed by actors after a significant hit?
- What are the long-term career impacts on actors who have starred in blockbuster hits?


## Datasets
### Main Dataset:
We fully leverage the CMU Movie Corpus as the central pillar of our project.

### Additional Datasets:
We enhance our primary database by selectively integrating relevant data from the IMDB database. Specifically, we focus on the files title.basics.tsv and title.ratings.tsv to provide additional details on films and their ratings.

### Analysis of Actor Roles:
For a comprehensive understanding of actor roles, we apply natural language processing (NLP) techniques to film summaries. This enables us to capture nuances such as the importance of the character and their moral orientation.


## Methods
### 1. Data Preprocessing

#### 1.1 Selected Features:
Choosing relevant features such as actor's name, date of birth, gender, ethnicity, movie revenue, and release date.

#### 1.2 Creation of Subset Data:
Merging the "characters" and "movies" dataframes to integrate information about actors and films.

#### 1.3 Spatial and Temporal Filtering, and Actor Selection:
Restricting the dataset to films produced in the United States, released from 1950 onwards.Analyzing the availability of essential information for each actor (name, date of birth, age, gender, ethnicity).Removing actors who participated in only one film to optimize the size and coherence of the dataset.

### 2. Definition of Successful Films
#### 2.1 Definition of Success Criteria:
Determination of success criteria for a film based on revenue and IMDb ratings. The success metric is the product of revenue and the average rating.

#### 2.2Study of the Evolution of Film Success:
Analysis of the evolution of the success metric over the years.

### 3. Definition of Blockbuster Actors
#### 3.1 Division of Actors into Groups:
Division of actors into two groups: those who have appeared in a blockbuster (treatment group) and others (control group).

#### 3.2 Analysis of Actor Characteristics:
Analysis of distributions of characteristics such as gender and age at the peak.

### 4. Matching
#### 4.1 Matching of Actors:
Matching based on gender and age at the peak of actors' careers.
Identification of the first blockbuster for each actor, addition of the number of films played, and preparation of data for matching.
Execution of the matching process and storage of results in "matched_df".


### 5. Analysis of Characters from Film Summaries
#### 5.1 Analysis of Character Appearances in Film Summaries:
Analyzing plot summaries: Extracting mentioned characters, i.e., names of characters repeated in synopses (entities labeled as PERSON), and determining the percentage of repetition for each name.

#### 5.2 Definition of Actor Roles from Film Summaries:
Actor roles are defined based on actions and attributes assigned to characters, following a method based on dependencies and links between words.
The classification is based on:
* Actions performed by the character: Verbs with "nsubj" or "agent" linked to the character's name.
* Actions the character is subject to: Verbs with "nsubjpass," "iobj," "prep_*," or "dobj" linked to the character's name.
* Attributes: Adjectives and nouns based on specific patterns.
After associating characters with their actions and attributes, a sentiment analysis is performed to determine whether they are predominantly associated with positive or negative actions/attributes.

### 6.Analysis of Actors' Careers After a Blockbuster
#### 6.1 Blockbuster Actors vs. Non-Blockbusters
**Career Longevity:**
Statistical analysis of career longevity between the two groups.
Using a Welch test to compare the means.

**Number of Films:**
Statistical analysis of the number of unique films associated with each actor.
Using a Welch test to compare the means.

#### 6.2 Career Analysis Before and After a Blockbuster
**Career Events for the Control Group:**
Assigning a mock "first blockbuster" to actors in the control group based on the corresponding film from the treatment group to which they are matched.

**Analysis of Revenues, IMDb Ratings, and Success Values:**
Analyzing the evolution of median film revenues, average IMDb ratings, and success values for groups before and after the first major success.
Using quantiles to account for extreme values.

**Career Genres Analysis:**
Converting genres into bags of words.
Calculating similarities between bags of words for successive genres for each actor.
Comparing average similarities between groups.

## Proposed timeline
```
.
o── 21.11.22 - Further data filtering 
│  
o── 23.11.22 - Pair matching of control and treated group, Optional: IMDb rating
│  
o── 25.11.22 - Perform trend analysis
│  
o── 28.11.22 - Work on Homework 2
│  
o── 01.12.23 - Homework 2
│    
o── 05.12.22 - Perform final analysis
│  
o── 12.12.22 - Start implementing data story
│  
o── 15.12.22 - Finalize code implementations and visualizations
│  
o── 18.12.23 - Perfection data story
│  
o 22.12.23 - Project milestone 3
.

```
## Organization within the team


<table class="tg" style="table-layout: fixed; width: 342px">
<colgroup>
<col style="width: 70px">
<col style="width: 600px">
</colgroup>
<thead>
  <tr>
    <th class="tg-0lax">Teammate</th>
    <th class="tg-0lax">Contributions</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Abir:</td>
    <td class="tg-0lax"> Conducted an in-depth analysis of characters from film summaries. <br> Contributed to the data storage process. <br> Provided valuable insights during the analysis of results. </td>
  </tr>
  <tr>
    <td class="tg-0lax">Diego: </td>
    <td class="tg-0lax"> Defined the criteria for successful films. <br> Categorized actors into blockbuster and non-blockbuster groups. <br> Analyzed the characteristics of blockbuster actors versus non-blockbusters. </td>
  </tr>
  <tr>
    <td class="tg-0lax">Raphaelle:</td>
    <td class="tg-0lax"> Integrated IMDb data into the project. <br> Played a crucial role in the data storage process. <br> Contributed to the comprehensive analysis in data stories. </td>
  </tr>
  <tr>
    <td class="tg-0lax">Yassine:</td>
    <td class="tg-0lax"> Led the matching process, ensuring actors were matched based on gender and age.<br> Contributed to the detailed analysis of actors' careers before and after a blockbuster.</td>
  </tr>
    <tr>
    <td class="tg-0lax">Xenia:</td>
    <td class="tg-0lax"> Led spatial and temporal filtering and actor selection. <br> Conducted the initial analysis of characters from film summaries. <br> Took a lead role in crafting the project's readme for clear communication. </td>
  </tr>
</tbody>
</table>


## Questions for TAs
None for now.
