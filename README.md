
# Team Cluster Test Repo

Simple repo for collecting twitter data

## Dependencies
* npm
* node

## Install node modules
```
npm install
```

## Setup
Rename the file [config-example.json](./config-example.json) to "config.json". Fill in all the keys with what I posted in the #general slack channel 

## Run
Outputs to terminal
```
node index.js
```

### How to generate all samples
You have to run [index.js](index.js) several times (24 times total), changing variables `city`, `whichQ`, and `date`
* `city`: should run [index.js](index.js) twice for each city
* `whichQ`: should be `"party"` once for each city and `"leader"` once for each city
* `date`: should be today's date