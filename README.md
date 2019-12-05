
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


