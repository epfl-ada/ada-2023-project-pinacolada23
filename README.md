# The Evolution of Actors Post-Blockbuster in the Film Industry

## Abstract

This project aims to analyze the career trajectories of actors following their roles in high-grossing films, using the CMU Movie Dataset as a primary resource. We're curious about how a significant box office success impacts an actor's subsequent choices and overall career path. Specifically, we intend to explore two dimensions: the evolution in the types of roles these actors undertake post-blockbuster, and the continuity of their box office success. This study seeks to find out patterns and trends in the film industry, providing insights into how a commercial success influence an actor's career decisions. By examining these aspects, we hope to understand and share the story of how sucess works in movie business and how it affects actors over time.


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
