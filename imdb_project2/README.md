# IMDB Votes Regression Project 2

The main purpose for this project was to use a basic linear regression or polynomial features of IMDB movie data to predict votes. We use votes as a target because we can use it as a pseudo mark of user interaction with the website dependant on movie parameters. I was particularly interested in genres and MCAA ratings and how they interacted with votes.

## Getting Started

All code is ran from imdb.ipynb one cell at a time.

### Data Acquisition:

The data used from this project as scraped from IMDB from https://www.imdb.com/list/ls057823854/?sort=list_order,asc&st_dt=&mode=detail which pulls US wide-distribution movie releases from 1972 to 2016. The title, genre, movie length, MCAA rating, year it was made, IMDB score, Metacritic score, number of votes, gross earning, director, and actors.

We then combine them into a dataframe.

### Data Cleaning:

First, we bin our actors into top rated actors by how many movies they star in, where 20 movies and up is a popular actor and less than 20 is a less popular actor. We do this for directors as well except for 10 movies instead of 20. Then we dummify our MCAA ratings and clean our genres where certain genres are not real movies, such as reality-TV and news.

### Fixing Nulls:

We then check our null values by features. We quickly see that metacritic scores are often missing to the tune of about 50%. Since this is far too many nulls, we remove this feature from our dat as well as dropping the null rows from votes since it is our target feature.

Then we remove movies with year above 2019 since that would include movies that are not made yet. After checking nulls in imdb score, duration, and directors being less than 20 each, we can safely remove these from our dataset without it impacting our results.

Our last nulls being gross earnings, instead of removing them or replacing them with mean values, we make an assumption based on our domain knowledge such that movies which have no gross earnings must have been relatively small unknown films. We set the value of these to the minimum gross earnings value of 10000.

### Data Analysis:

Prior to data analysis, we split the title, actors, director, genres, and MCAA rating so we can start analyzing our data in regressions.

First we check our basic linear regression by setting votes as our target feature and the rest as X. This gives us an R^2 of .533 as well as our coefficients. 

We check our regression with a heatmap and a pairplot to have a quick look and sanity check our results and linearity of features. since they check out, we use polynomial features with degree 2 and 3 to see if it improves out score. Since polynomial features with a degree of 2 improves our score, we use it and set a loop of lasso regularization with variable alphas to see which gives ur a good R^2 while still giving us interpretable amount of features (around 100). This gives us a training  R^2 of about .69 and a test R^2 of about .63.

### Future Regression Without Constraints:

Since our constraints were using only linear regression models and polynomial features, we can definitely improve upon our score since we can tell that our data is not perfectly linear. We double check this with a quick RandomForestRegressor to check our R^2 giving us a test score of .833 validating our assumption.


## Running the Code

Since this is all within ipython and jupyter notebooks, you can run imdb.ipynb and run each cell. You should end up with pandas dataframes and visualization charts of the data and coefficients and residuals by the end of the notebook.


## Authors

* **Christian Branton** 

[Metis](https://github.com/thisismetis)

## Acknowledgments

* A big thanks to Metis for making all this possible
