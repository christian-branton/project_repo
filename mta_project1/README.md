# MTA Turnstile EDA and Bar Location Recommendation

The main idea for this project was explatory data analysis of subway MTA turnstile data. After cleaning, sorting, and analyzing this data, we then used this data combined with data we scraped and cleaned from the NYC.gov website for liquor licenses and created ratios for foot traffic by station and number of bars within a 0.5 kilometer radius around the station. The idea is to find stations with the most foot traffic but with the least amount of competition from other bars in the area.

## Getting Started

mta_data.ipynb has the bulk of the code necessary for the MTA turnstile data portion of the project. If each cell is run in order, it will pull the data, clean it (which is a majority of the project since the data is rather messy), and sorts and analyzes it.

Once this is done, mta_barproximityranking.ipynb pulls the data for the liquor licenses, cleans it, and combines it with our earlier data from mta_data.ipynb to create our ratios of foot-traffic to bars within a certain radius of a subway station.

### Prerequisites

(What things you need to install the software and how to install them)
Mainly, just the basics are necessary as prerequisites such as pandas, etc.

```
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```
Additionally, we used folium to map out bars as pins with the radius around them to show the density of bars around certain stations.

EX. Bars around Times Square and 42nd Station (Bad foot traffic to bar density)
![Times Square and 42nd Station](TimeSquare-42nd.png)

EX. Bars around 125th Station (Good foot traffic to bar density)
![125th Station](125th.png)

### Installing

This should be relatively unecessary since these are common libraries, but if these need to be installed,

```
pip install numpy
pip install matplotlib
pip install pandas
pip install seaborn
```
conversely, these can be installed via anacondas as well,

```
conda install numpy,
etc.
```

This is all run on Python3 within Jupyter Notebooks

## Running the Code

Since this is all within ipython and jupyter notebooks, you can run full_mta_complete.ipynb and run each cell. You should end up with pandas dataframes and visualization charts of top stations with highest ratio of foot traffic to bars in the area.


EX. Busiest stations in NYC
![Busiest stations](busstatfig.png)

EX. Stations with the most bars nearby
![stations with the most bars nearby](barsnearbyfig.png)

EX. Busiest locations with least bars
![busiest locations with least bars](endfig.png)

## Built With

* [Folium](https://pypi.org/project/folium/) - Geographic visualization library
* [Matplotlib](https://matplotlib.org/) - Visualization library
* [Seaborn](https://seaborn.pydata.org/) - Visualization library

## Authors

* **Christian Branton** 
* **Lukas Wadya** 
* **Phillip Beltre** 
* **James Mitchell**

[Metis](https://github.com/thisismetis)

## Acknowledgments

* Thanks to my team members for this project
* And a big thanks to Metis for making all this possible