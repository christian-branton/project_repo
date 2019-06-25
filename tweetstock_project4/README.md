# Tweet Stock Sentiment Project 4

The main purpose for this project was to use tweets and sentiment analysis on a variety of companies within a variety of industries and see if it was possible to have a leading indicator of stock price based on accumulating sentiment per minute and per amount of tweets. 

## Getting Started

The code for the companies with products is within TweetfinanceP.ipynb while the code for the companies without products is within TweetfinanceNP.ipynb.

### Data Acquisition:

The data used for this project was acquired by using the Twitter API using twitter_streaming_np.py for companies without products and twitter_streaming_p.py for companies with products. I used companies with products such as Google, Amazon, Disney, Apple, and Ford and serached for them and their  products while also searching for a variety of sp100 companies without products celgene and abbvie for pharmaceutical companies; accenture, blackrock, and goldman for finance and consulting companies; and schlumberger, exxon, and chevron for the energy industry. I pulled these tweets from markets hours between 9:30am and 4pm.

### Data Cleaning:

After we put this data in the dataframe, we delete many of the unnecessary features such as id and contributors. Since the data we acquire is in JSON form, we have to get the right tweet format, which is either extended tweet if truncated, tweet comment if retweeting and extended if truncated, or just the retweet if no other tweet comment and extend it if it is truncated. 

### NLP Data Analysis:

As an analysis to this project, I used NMF and PCA with both count vectorizor and tf-idf and NMF with tf-idf gave the best results. It is important to have a subtantial and extensive stopword list before engaging in analysis. Within the stopwords folder has a list of stopwords which can be used for this purpose. Since we chose the main topics beforehand, we can choose the number of topics beforehand to match the number of companies we chose and review the results as a quick sanity check.

### Sentiment and Data Analysis

After analysis the amount of tweets per company for that day and making sure there are enough tweets, we run them through textblob and vadersentiment and check which has the most accurate sentiment analysis. For me, this was via vader sentiment which I then used and then calculated rolling sentiment over time and mapped it against tweets over time. I could then compare this with the stock price over the same time and analyze when the tweet sentiment went over or under a certain number of my choice. Once this coincided with a sufficient tweet count, we could see if it was an leading indicator of the stock price and whether it had any predictive power.

## Running the Code

Since this is all within ipython and jupyter notebooks, you can run both TweetfinanceP.ipynb and TweetfinanceNP.ipynb and run each cell. You should end up with pandas dataframes and visualization graphs of the data by the end of the notebook.

### Prerequisites

You need to have a twitter account and apply for the twitter API in order to access the tweets with this project and code. Besides that, the only other coding prerequisits are mainly just the basics, such as pandas, etc.
It also uses scikitlearn, textblob, wordcloud, and vadersentiment extensively.
```
import json
import pandas as pd
import numpy as np
import re
import datetime
import matplotlib.pyplot as plt
```
```
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.d ecomposition import NMF

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud

```
### Installing

This should be relatively unecessary since these are common libraries, but if these need to be installed,

```
pip install numpy
pip install datetime
pip install matplotlib
pip install pandas
pip install seaborn
pip install scikit-learn
pip install textblob
pip install vaderSentiment
pip install wordcloud
```
conversely, these can be installed via anacondas as well,

```
conda install numpy,
etc.
```

This is all run on Python3 within Jupyter Notebooks

### Visualization

I used Matplotlib and Seaborn as basic visualization but used Tableau for the presentation visualizations to show the stock pricing over minute, the sentiment over minute, and the tweet count over minute so you can see the exact moments of change and indicators.

## Authors

* **Christian Branton** 

[Metis](https://github.com/thisismetis)

## Acknowledgments

* A big thanks to Metis for making all this possible
