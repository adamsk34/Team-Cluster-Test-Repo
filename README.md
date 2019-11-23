
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
Run the following command to take tweet data from twitter and put it in JSON files in the directory `city_tweets/`
```
node index.js
```
