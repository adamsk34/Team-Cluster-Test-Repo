var Twit = require("twit");

var config = require("./config.json");
var T = new Twit(config);

var params = {
    q: "Justin Trudeau",
    count: 100
}

// gets latest 100 tweets returned by searching "Justin Trudeau"
T.get("search/tweets", params, gotData);

function gotData (err, data, response) {
    // prints data as JSON
    console.log(JSON.stringify(data, null, 2));
}