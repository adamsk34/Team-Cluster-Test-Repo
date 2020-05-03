
# Team Cluster Test Repo

This is an academic project for the class Data Mining (COMP 4710) at the University of Manitoba for fall 2019. This repo contains twitter data and code for collecting and processing it. The goal of this project is to predict the outcome of the 2019 United Kingdom general election.

## This Repository Contains Data

* Raw Twitter Data
    * `city_tweets/` contains responses from the Twitter API when running [index.js](index.js).
* Tweets and Meta Data
    * `tweets_csv/no_date_overlap/` contains output from running [convertJsontoCsvNoDateOverlap.py](convertJsontoCsvNoDateOverlap.py)
* Words and Sentimental Value
    * [AFINN-111.csv](AFINN-111.csv) contains words and associated sentimental value
* Sentiment of Tweets
    * `NETWORK-PYTHON PACKAGE/Calculated data/` contains batches of tweets (organized by date). Batches contain files with  sentimental scores of leaders and parties derived from the tweets, and meta data.

## Dependencies
* npm 6.7.0
* node 8.10.0
* python 3.6

## Install node modules
```
npm install
```

## Setup
Rename the file [config-example.json](./config-example.json) to `"config.json"`. Fill in all the keys with what's in a pinned message in the #general slack channel.

## Running the code

### Getting the tweets

Run the following command to take tweet data from twitter and put it in JSON files in the directory `city_tweets/`
```
node index.js
```

### Cleaning up json

Run the following command

```
python convertJsontoCsv.py
```

This will create a folder named as current UK date. In side that folder it will create csv file for each cities. 

Each csv file have five columns ['city', 'party', 'leader', 'tweet', 'tweet_time'] extracted from the JSON file. 

If you want to organize the tweets by date, run the following:
```
python convertJsontoCsvNoDateOverlap.py
```

## Sentimental Analysis

[SentimentREADME.md](SentimentREADME.md) is a readme file that explains [Sentimental.java](Sentimental.java)

## Network Analysis 

Contained in the directory `NETWORK-PYTHON PACKAGE/`
## Setup

Insert sentimental data into Calculated data folder
Will need to install the package networkx

## Running the code 
```
Run SNA.py
```
## Description 

Using the networkx package creates a network of nodes and edges, with edges being the weights of how much sentimental value gets added for each political party. 

It will read the contents of the directory `Calculated data/`  

Results are printed to console 

