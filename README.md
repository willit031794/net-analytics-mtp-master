# **SMM638 - Network Analytics (Midterm Project)**

## **Overview**
Over recent decades, it has been a growing interest of scientists to analyse the flow of information in complicated social networks. The concept of ‘Community Detection’ has been studied to identify certain groups that exist within such networks. This can be used to solve important business or managerial issues such as organisational silos or security in email networks. Therefore, the members of group 7 have conducted a study on use cases of 5 different algorithms and tested their characteristics on a Star Wars data set to help solve organisational silos. This will be contrasted with the Robustness Test created by the group to comment on the differences of each algorithm.

## **Dataset**
-   [Kaggle: Star Wars Social Network](https://www.kaggle.com/ruchi798/star-wars)   
This dataset contains the social network of Star Wars characters extracted from the movie scripts. If two characters speak together within the same scene, they have been connected.  

**starwars-full-interactions.json**  
- Number of nodes: 110  
- Number of edges: 398  
- Average degree:   7.2364  

## **Directory Structure**


```
        net-analytics-mtp
        ├── README.md
        ├── requirement.txt
        ├── Group7SMM638.pptx
        ├── datasets
        │   ├── starwars-full-interactions.json
        │   ├── starwars-episode-1-interactions.json
        │   ├── starwars-episode-2-interactions.json
        │   ├── starwars-episode-3-interactions.json
        │   ├── starwars-episode-4-interactions.json
        │   ├── starwars-episode-5-interactions.json
        │   ├── starwars-episode-6-interactions.json
        │   ├── starwars-episode-7-interactions.json
        │   └── README.md
        └── scripts
            ├── 00_data_exploration.ipynb
            ├── 01_star_wars_community_detection.ipynb
            ├── 02_null_case_community_detection.ipynb
            ├── community_detection
            |   ├── __init__.py
            |   ├── algorithms.py
            |   ├── data_preprocessing.py
            |   ├── evaluation.py
            |   ├── timeit_functions.py
            |   └── visualize.py
            └── output
                ├── gn_modularity_plot_Erdős-Rényi.png
                ├── gn_modularity_plot_Star-Wars.png
                ├── viz_erdős-rényi_clauset-newman-moore.html
                ├── viz_erdős-rényi_girvan-newman.html
                ├── viz_erdős-rényi_infomap.html
                ├── viz_erdős-rényi_leiden.html
                ├── viz_erdős-rényi_louvain.html
                ├── viz_star-wars_clauset-newman-moore.html
                ├── viz_star-wars_girvan-newman.html
                ├── viz_star-wars_infomap.html
                ├── viz_star-wars_leiden.html
                └── viz_star-wars_louvain.html

```

## File Description
-   `requirement.txt` -> Python packages requirements
-   `Group7SMM638.pptx` -> Project presentation
### datasets
-   `starwars-full-interactions.json` -> Json file contains all nodes and edges from Star-Wars episode 1-7
-   `starwars-episode-1-interactions.json` -> Json file contains nodes and edges from Star-Wars episode 1 
-   `starwars-episode-2-interactions.json` -> Json file contains nodes and edges from Star-Wars episode 2
-   `starwars-episode-3-interactions.json` -> Json file contans nodes and edges from Star-Wars episode 3
-   `starwars-episode-4-interactions.json` -> Json file contains nodes and edges from Star-Wars episode 4
-   `starwars-episode-5-interactions.json` -> Json file contains nodes and edges from Star-Wars episode 5
-   `starwars-episode-6-interactions.json` -> Json file contains nodes and edges from Star-Wars episode 6
-   `starwars-episode-7-interactions.json` -> Json file contains nodes and edges from Star-Wars episode 7

### scripts
-   `00_data_exploration.ipynb` -> Exploratory data analysis on Star-Wars network
-   `01_star_wars_community_detection.ipynb` -> Network analysis on Star-Wars network
-   `02_null_case_community_detection.ipynb` -> Network analysis on Erdős-Rényi graph (random graph)

#### community_detection
-   `algorithms.py` -> Python script contains functions to implement community detection algorithms on a 1-mode undirected graph
-   `data_preprocessing.py` -> Python script contains a function to load and pre-process Star-Wars network graph 
-   `evaluation.py` -> Python script contains functions to evaluate algorithms and results
-   `timeit_functions.py` -> Python script contains functions to capture the execution time of each algorithm 
-   `visualize.py` -> Python script contains functions to visualize 3D network graphs

### output
-   `gn_modularity_plot_Erdős-Rényi.png` -> Modularity plot from Girvan-Newman algorithm on Erdős-Rényi graph
-   `gn_modularity_plot_Star-Wars.png` -> Modularity plot from Girvan-Newman algorithm on Star-Wars graph
-   `viz_erdős-rényi_clauset-newman-moore.html` -> 3D plot of communities in Erdős-Rényi graph segmented by Clauset-Newman-Moore algorithm
-   `viz_erdős-rényi_girvan-newman.html` -> 3D plot of communities in Erdős-Rényi graph segmented by Girvan-Newman algorithm
-   `viz_erdős-rényi_infomap.html` -> 3D plot of communities in Erdős-Rényi graph segmented by Infomap algorithm
-   `viz_erdős-rényi_leiden.html` -> 3D plot of communities in Erdős-Rényi graph segmented by Leiden algorithm
-   `viz_erdős-rényi_louvain.html` -> 3D plot of communities in Erdős-Rényi graph segmented by Louvain algorithm
-   `viz_star-wars_clauset-newman-moore.html` -> 3D plot of communities in Star-Wars graph segmented by Clauset-Newman-Moore algorithm
-   `viz_star-wars_girvan-newman.html` -> 3D plot of communities in Star-Wars graph segmented by Girvan-Newman algorithm
-   `viz_star-wars_infomap.html` -> 3D plot of communities in Star-Wars graph segmented by Infomap algorithm
-   `viz_star-wars_leiden.html` -> 3D plot of communities in Star-Wars graph segmented by Leiden algorithm
-   `viz_star-wars_louvain.html` -> 3D plot of communities in Star-Wars graph segmented by Louvain algorithm


## **Example of result:**
**Infomap model** 

- Number of communities: 9 + 1 (One isolated node)
```
{
0: ['QUI-GON', 'OBI-WAN', 'EMPEROR', 'CAPTAIN PANAKA', 'SIO BIBBLE', 'JAR JAR', 'TARPALS', 'BOSS NASS', 'PADME', 'WATTO', 'ANAKIN', 'SEBULBA', 'JIRA', 'SHMI', 'KITSTER', 'WALD', 'FODE/BEED', 'GREEDO', 'VALORUM', 'MACE WINDU', 'KI-ADI-MUNDI', 'YODA', 'RABE', 'BAIL ORGANA', 'CAPTAIN TYPHO', 'SENATOR ASK AAK', 'ORN FREE TAA', 'TAUN WE', 'LAMA SU', 'COUNT DOOKU', 'PLO KOON', 'ODD BALL', 'GENERAL GRIEVOUS', 'CLONE COMMANDER GREE', 'CLONE COMMANDER CODY', 'TION MEDON', 'CAPTAIN ANTILLES'], 
1: ['C-3PO', 'JABBA', 'LUKE', 'LEIA', 'HAN', 'RIEEKAN', 'DERLIN', 'ZEV', 'DACK', 'LANDO', 'BIB FORTUNA', 'BOUSHH', 'ADMIRAL ACKBAR', 'ADMIRAL STATURA'], 
2: ['LOR SAN TEKKA', 'POE', 'KYLO REN', 'CAPTAIN PHASMA', 'FINN', 'UNKAR PLUTT', 'REY', 'GENERAL HUX', 'LIEUTENANT MITAKA', 'BALA-TIK', 'SNOKE', 'MAZ', 'BB-8', 'SNAP', 'YOLO ZIFF', 'COLONEL DATOO', 'ELLO ASTY', 'JESS', 'NIV LEK'], 
3: ['BOBA FETT', 'JANGO FETT', 'DARTH VADER', 'MOTTI', 'TARKIN', 'PIETT', 'OZZEL', 'NEEDA', 'JERJERROD'],
4: ['NUTE GUNRAY', 'PK-4', 'TC-14', 'DOFINE', 'RUNE', 'TEY HOW', 'DARTH MAUL', 'GENERAL CEEL', 'SUN RIT', 'POGGLE'], 
5: ['CAMIE', 'BIGGS', 'DODONNA', 'GOLD LEADER', 'WEDGE', 'RED LEADER', 'RED TEN', 'JANSON'], 
6: ['OWEN', 'BERU', 'CLIEGG'], 
7: ['RIC OLIE', 'BRAVO TWO', 'BRAVO THREE'],
8: ['FANG ZAR', 'MON MOTHMA', 'GIDDEAN DANU'],
9: ['SOLA', 'JOBAL', 'RUWEE'], 
10: ['GOLD FIVE']}
```

## **Datasets insight**

This table shows which episode(s) each character was in the movie. 
```
|     | name                 |   ep_1 |   ep_2 |   ep_3 |   ep_4 |   ep_5 |   ep_6 |   ep_7 |
|----:|:---------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
|   0 | QUI-GON              |      1 |      0 |      1 |      0 |      0 |      0 |      0 |
|   1 | NUTE GUNRAY          |      1 |      1 |      1 |      0 |      0 |      0 |      0 |
|   2 | PK-4                 |      1 |      1 |      0 |      0 |      0 |      0 |      0 |
|   3 | TC-14                |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|   4 | OBI-WAN              |      1 |      1 |      1 |      1 |      1 |      1 |      0 |
|   5 | DOFINE               |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|   6 | RUNE                 |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|   7 | TEY HOW              |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|   8 | EMPEROR              |      1 |      1 |      1 |      0 |      1 |      1 |      0 |
|   9 | CAPTAIN PANAKA       |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  10 | SIO BIBBLE           |      1 |      1 |      0 |      0 |      0 |      0 |      0 |
|  11 | JAR JAR              |      1 |      1 |      1 |      0 |      0 |      0 |      0 |
|  12 | TARPALS              |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  13 | BOSS NASS            |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  14 | PADME                |      1 |      1 |      1 |      0 |      0 |      0 |      0 |
|  15 | RIC OLIE             |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  16 | WATTO                |      1 |      1 |      0 |      0 |      0 |      0 |      0 |
|  17 | ANAKIN               |      1 |      1 |      1 |      0 |      0 |      1 |      0 |
|  18 | SEBULBA              |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  19 | JIRA                 |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  20 | SHMI                 |      1 |      1 |      0 |      0 |      0 |      0 |      0 |
|  21 | C-3PO                |      1 |      1 |      1 |      1 |      1 |      1 |      1 |
|  22 | DARTH MAUL           |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  23 | KITSTER              |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  24 | WALD                 |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  25 | FODE/BEED            |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  26 | JABBA                |      1 |      0 |      0 |      1 |      0 |      1 |      0 |
|  27 | GREEDO               |      1 |      0 |      0 |      1 |      0 |      0 |      0 |
|  28 | VALORUM              |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  29 | MACE WINDU           |      1 |      1 |      1 |      0 |      0 |      0 |      0 |
|  30 | KI-ADI-MUNDI         |      1 |      1 |      0 |      0 |      0 |      0 |      0 |
|  31 | YODA                 |      1 |      1 |      1 |      0 |      1 |      1 |      0 |
|  32 | RABE                 |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  33 | BAIL ORGANA          |      1 |      1 |      1 |      0 |      0 |      0 |      0 |
|  34 | GENERAL CEEL         |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  35 | BRAVO TWO            |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  36 | BRAVO THREE          |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  37 | CAPTAIN TYPHO        |      0 |      1 |      1 |      0 |      0 |      0 |      0 |
|  38 | SENATOR ASK AAK      |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  39 | ORN FREE TAA         |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  40 | SOLA                 |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  41 | JOBAL                |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  42 | RUWEE                |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  43 | TAUN WE              |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  44 | LAMA SU              |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  45 | BOBA FETT            |      0 |      1 |      0 |      0 |      1 |      0 |      0 |
|  46 | JANGO FETT           |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  47 | OWEN                 |      0 |      1 |      0 |      1 |      0 |      0 |      0 |
|  48 | BERU                 |      0 |      1 |      0 |      1 |      0 |      0 |      0 |
|  49 | CLIEGG               |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  50 | COUNT DOOKU          |      0 |      1 |      1 |      0 |      0 |      0 |      0 |
|  51 | SUN RIT              |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  52 | POGGLE               |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  53 | PLO KOON             |      0 |      1 |      1 |      0 |      0 |      0 |      0 |
|  54 | ODD BALL             |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
|  55 | GENERAL GRIEVOUS     |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
|  56 | FANG ZAR             |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
|  57 | MON MOTHMA           |      0 |      0 |      1 |      0 |      0 |      1 |      0 |
|  58 | GIDDEAN DANU         |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
|  59 | CLONE COMMANDER GREE |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
|  60 | CLONE COMMANDER CODY |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
|  61 | TION MEDON           |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
|  62 | CAPTAIN ANTILLES     |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
|  63 | DARTH VADER          |      0 |      0 |      1 |      1 |      1 |      1 |      0 |
|  64 | LUKE                 |      0 |      0 |      0 |      1 |      1 |      1 |      0 |
|  65 | CAMIE                |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
|  66 | BIGGS                |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
|  67 | LEIA                 |      0 |      0 |      0 |      1 |      1 |      1 |      1 |
|  68 | MOTTI                |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
|  69 | TARKIN               |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
|  70 | HAN                  |      0 |      0 |      0 |      1 |      1 |      1 |      1 |
|  71 | DODONNA              |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
|  72 | GOLD LEADER          |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
|  73 | WEDGE                |      0 |      0 |      0 |      1 |      1 |      1 |      0 |
|  74 | RED LEADER           |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
|  75 | RED TEN              |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
|  76 | GOLD FIVE            |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
|  77 | RIEEKAN              |      0 |      0 |      0 |      0 |      1 |      0 |      0 |
|  78 | DERLIN               |      0 |      0 |      0 |      0 |      1 |      0 |      0 |
|  79 | ZEV                  |      0 |      0 |      0 |      0 |      1 |      0 |      0 |
|  80 | PIETT                |      0 |      0 |      0 |      0 |      1 |      1 |      0 |
|  81 | OZZEL                |      0 |      0 |      0 |      0 |      1 |      0 |      0 |
|  82 | DACK                 |      0 |      0 |      0 |      0 |      1 |      0 |      0 |
|  83 | JANSON               |      0 |      0 |      0 |      0 |      1 |      0 |      0 |
|  84 | NEEDA                |      0 |      0 |      0 |      0 |      1 |      0 |      0 |
|  85 | LANDO                |      0 |      0 |      0 |      0 |      1 |      1 |      0 |
|  86 | JERJERROD            |      0 |      0 |      0 |      0 |      0 |      1 |      0 |
|  87 | BIB FORTUNA          |      0 |      0 |      0 |      0 |      0 |      1 |      0 |
|  88 | BOUSHH               |      0 |      0 |      0 |      0 |      0 |      1 |      0 |
|  89 | ADMIRAL ACKBAR       |      0 |      0 |      0 |      0 |      0 |      1 |      1 |
|  90 | LOR SAN TEKKA        |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
|  91 | POE                  |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
|  92 | KYLO REN             |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
|  93 | CAPTAIN PHASMA       |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
|  94 | FINN                 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
|  95 | UNKAR PLUTT          |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
|  96 | REY                  |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
|  97 | GENERAL HUX          |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
|  98 | LIEUTENANT MITAKA    |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
|  99 | BALA-TIK             |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| 100 | SNOKE                |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| 101 | MAZ                  |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| 102 | BB-8                 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| 103 | SNAP                 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| 104 | ADMIRAL STATURA      |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| 105 | YOLO ZIFF            |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| 106 | COLONEL DATOO        |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| 107 | ELLO ASTY            |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| 108 | JESS                 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| 109 | NIV LEK              |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
|----:|:---------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
```

## **Reference**
-   [Community detection in Social Media](https://0-www-proquest-com.wam.city.ac.uk/docview/928388728?OpenUrlRefId=info:xri/sid:summon&accountid=14510) 
-   [A Distributed Infomap Algorithm for Scalable and High-Quality Community Detection](https://dl.acm.org/doi/10.1145/3225058.3225137) 
-   [A new algorithm CNM-Centrality of detecting communities based on node centrality](https://www.sciencedirect.com/science/article/abs/pii/S0378437115009425) 
-   [Detecting community structure in networks](https://link.springer.com/article/10.1140/epjb/e2004-00124-y) 
-   [Fast algorithm for detecting community structure in networks](https://arxiv.org/abs/cond-mat/0309508) 
-   [PARC: ultrafast and accurate clustering of phenotypic data of millions of single cells](https://academic.oup.com/bioinformatics/article/36/9/2778/5714737) 
-   [Dynamic Clustering in Social Networks using Louvain and Infomap Method](https://arxiv.org/abs/1603.02413) 
-   [From Louvain to Leiden: Guaranteeing well-connected communities](https://www.nature.com/articles/s41598-019-41695-z) 
-   [Fast unfolding of communities in large networks](https://arxiv.org/abs/0803.0476) 
-   [Community Detection in Who-calls-Whom Social Networks](https://link.springer.com/chapter/10.1007/978-3-319-98539-8_2) 
-   [Community structures and role detection in music networks](https://aip.scitation.org/doi/abs/10.1063/1.2988285)
-   [Community structure in networks: Girvan-Newman algorithm improvement](https://ieeexplore.ieee.org/document/6859714)


