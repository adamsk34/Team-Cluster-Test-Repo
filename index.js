var Twit = require("twit");

var config = require("./config.json");
var T = new Twit(config);

var params = {
    q: "Labour Party OR Conservative Party OR Liberal Democrats OR Brexit Party",
    // party
    // party leader
    count: 100,
    geocode: [51.0, 0.0, "50mi"]
}

T.get("search/tweets", params, gotData);

function gotData (err, data, response) {
    // prints data as JSON
    console.log(JSON.stringify(data, null, 2));
}