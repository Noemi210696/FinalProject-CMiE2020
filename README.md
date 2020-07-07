# CMiE2020- Final Project "The musical ´Balkan´: Orientalism and Autobalkanism"

This repository contains a simple code for the analysis of machine-readable scores: arrangements of Serbian songs, and compositions associated to and/or inspired by the "Balkan(s)". These are the materials used for the final project for the course "Computational methods in ethnomusicology" (Kunstuniversität Graz, 2020). The code consists of two functions: one which counts the number of augmented seconds in each part of a score, and the other that calculates the percentage of augmented seconds in the entire score. 

## Requirements for reproducibility: 

- `Python 3` 
- `Music21` (version: music21==5.7.2), which can be downloaded from https://web.mit.edu/music21/; and 
- `Matplotlib` (version: matplotlib==3.1.1), which is available under https://matplotlib.org/.

## Content

Alongside this file, the repository includes the script `ScoresAnalysis.py`, which contains the two functions with explanations that allow for the application of the code to any score consisting of either one or multiple parts. The file `Plot.py` contains the code used to plot categorical variables. The notebook `Score_Analysis.ipynb` contains the analysis with results for each score used for this project.

 
## Dataset

The scores used for this analysis were found on MuseScore (https://musescore.com/dashboard) and downloaded as musicXML files. These include six idividual pieces and two collections:

- "Collection_1" is available under https://musescore.com/anthonthelad/2
- "Collection_2" is available under https://musescore.com/anthonthelad/medley_-_serbian_songs_mscz-2
- "Memoires of Mostar" is available under https://musescore.com/user/280306/scores/266386
- "Balkan Mixture" is availabe under https://musescore.com/user/2564496/scores/1155611
- "Balkan Trio" is available under https://musescore.com/user/3536041/scores/1022146
- "Misrlu" is available under https://musescore.com/user/3998046/scores/1111256
- "Nesanica" is available under https://musescore.com/user/27147554/scores/5547832
- "Balkan dance" is available under https://musescore.com/user/27668777/scores/5260870


## Use

The above listed requirements need to be installed for the code to work. If the code will be applied on the same scores used for this project, these need to be downloaded as musicxml files from the links provided in the above section ("Dataset"). 

## License
GNU GENERAL PUBLIC LICENSE

