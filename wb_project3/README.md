# World Bank Financial Inclusion Classification Project 3

The main purpose for this project was to use the World Bank Financial Inclusion dataset to check whether or not a person can come up with emergency funds within a month equal to 20% of annual NGDP by country as a binary classification problem and then use this data in conjunction with outside datasets to analyze the differences between countries for the most and least important features for this classification problem.

### Feature Engineering Problem

My initial dataset was the World Bank Financial Inclusion. However, all the answers were either binary or categorical, making feature engineering particularly difficult. Since I could not use feature engineering in order to get a better score, this is why I chose feature addition in order to improve accuracy with the inclusion of the WEO, WBH, and life expectancy.

## Getting Started

All code is ran from WBFI.ipynb one cell at a time.

### Data Acquisition:

The data used from this project as acquired from multiple sources.
Firstly, the World Bank Financial Inclusion dataset was downloaded from http://microdata.worldbank.org and must be applied for. After that I got secondary datasets from the World Bank Health Dataset, the World Bank Education Dataset, the World Economic Outlook Dataset from the IMF, and the Life Expectancy dataset from the CIA. All are within the project directory. 

### Data Cleaning:

One of the main sources of data cleaning in this project is matching the countries within each dataset. Other than that, the other issue is nulls. Since we are using decision tree based classifiers such as Random Forest Classifier and gradient boosted descent methods such as XGBoost, we can keep our nulls or set them to an arbitrarily large negative number. Once all our data is cleaned and combined, we remove some arbitrary and unecessary features and make sure our data makes sense. 

### Metric selection

Amongst the metrics I chose to use to measure success of our model, I chose F1 metrics since there was no preferences between precision and recall, making it an ideal metric. Accuracy could have been used as well since the classes were relatively well balanced but I felt F1 to be a better statistic for this particular project.

### Data Analysis:

I used a logistic regression, a random forest classifier, and xgboost to compare results with a train test set and cross validating the train set with 5 folds. XGboost gave the best results and once the hyperparameters were set, I ran the model on all countries and returned the feature importances to compare the differences between countries as well as running them on all regions. Our F1 score for CV 5-fold mean for the total dataset was .781 which of course varied depending on country and region.

## Running the Code

Since this is all within ipython and jupyter notebooks, you can run imdb.ipynb and run each cell. You should end up with pandas dataframes and visualization charts of the data and coefficients and residuals by the end of the notebook.

### Prerequisites

(What things you need to install the software and how to install them)
Mainly, just the basics are necessary as prerequisites such as pandas, etc.
It also uses scikitlearn and xgboost extensively
```
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```
```
from sklearn.linear_model import LinearRegression, Lasso, LassoCV, Ridge, RidgeCV, LogisticRegression, LogisticRegressionCV
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, precision_recall_curve, f1_score, fbeta_score, classification_report,accuracy_score, confusion_matrix, roc_auc_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import RFE

from xgboost import XGBClassifier
```
### Installing

This should be relatively unecessary since these are common libraries, but if these need to be installed,

```
pip install numpy
pip install matplotlib
pip install pandas
pip install seaborn
pip install scikit-learn
pip install xgboost
```
conversely, these can be installed via anacondas as well,

```
conda install numpy,
etc.
```

This is all run on Python3 within Jupyter Notebooks

### Visualization

I used Matplotlib and Seaborn as basic visualization but used Tableau for the presentation visualizations to show the differences between countries.

## Authors

* **Christian Branton** 

[Metis](https://github.com/thisismetis)

## Acknowledgments

* A big thanks to Metis for making all this possible
