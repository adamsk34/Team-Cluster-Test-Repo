
# Team Cluster Test Repo

Simple repo for collecting twitter data

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

