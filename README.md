# The Evolution of Actors Post-Blockbuster in the Film Industry

## Datastory

TODO: put the link here with a small sentence

## Abstract

This research project is designed to conduct a comprehensive analysis of the career trajectories of actors subsequent to their involvement in high-grossing films, utilizing the CMU Movie Dataset as the principal data source. The objective is to investigate the impact of significant box office success on an actor's subsequent professional choices and the trajectory of their career. The study will specifically focus on two key aspects: the progression in the variety of roles chosen by these actors after their blockbuster experiences, and the sustainability of their success at the box office. The aim is to identify patterns and trends within the film industry, shedding light on how commercial success influences the career decisions of actors. By delving into these dimensions, the project aspires to elucidate and articulate the narrative of success in the movie business and its enduring effects on actors' careers.


## Research questions
- Does a high-grossing film consistently lead to continued box office success for its actors in their subsequent films?
- Is there a noticeable change in the genre or type of characters portrayed by actors after a significant hit?
- What are the long-term career impacts on actors who have starred in blockbuster hits?


## Proposed additional datasets
No other dataset used for now
Optional: IMDb ratings, BAFTA


## Methods

We will be compairing the general trends in career evolution of actors that played in a very successful movie (high box office revenue) with the career evolution of acotrs that did not play in any successful movies. In this analysis, actors that did not play in a very successful movie constitute our control group. On the other hand, actors that had a big hit consitute the treated group.

- Data pre-processing and cleaning:
    - Selecting relevant features: we decided to keep movies from the U.S. from the year 1980 and after
    - Handling missing data: remove 
    - Merging datasets
- Statistical analysis:
    - Pair matching for control and treatement group
    - T-Test and/or Chi-Square to evaluate the statistical significance of possible differences between these two groups
    - Correlate box office revenue associated to movies from an actor with changes in roles
- Data visualization: For clear representation of trends and patterns.
- Machine Learning Techniques: Employing clustering algorithms to group actors based on similarities in their career paths post-hit.
- Time-Series Analysis: Identifying patterns and anomalies over time in box office performance and role selection.
- Natural Language processing Techniques: Analyse plot summaries to extract additional informations on character types


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

Abir: Pair matching and mitigation of confounder effect 

Diego: Feature selection and data filtering

Raphaelle: Movie summary information retrieval

Yassine: Character type information retrieval

Xenia: IMDs rating dataset addition assessement (meaningfulness and feasability)


## Questions for TAs
None for now.
