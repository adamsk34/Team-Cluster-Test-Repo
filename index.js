var fs = require("fs");
var Twit = require("twit");
var config = require("./config.json");

/* *** change `city`, `whichQ`, and `date` to generate all samples for today's date *** */

// var city = "aberdeen";
// var city = "belfast";
// var city = "birmingham";
// var city = "cardiff";
// var city = "derry";
// var city = "edinburgh";
// var city = "glasgow";
// var city = "lisburn";
// var city = "liverpool";
// var city = "london";
// var city = "newport";
var city = "swansea";

// var whichQ = "leader";
var whichQ = "party";

var date = "2019-11-15";// Should be today's date

var fileName = "city_rules/" + city + ".json";
var content = JSON.parse(fs.readFileSync(fileName));

var T = new Twit(config);
var count = 100

var qParties = "Labour Party OR Conservative Party OR Liberal Democrats OR Brexit Party";
var qLeaders = "Jeremy Corbyn OR Boris Johnson OR Jo Swinson OR Nigel Farage";

var params = {
    count: count,
    geocode: content.geocode
};

if (whichQ === "party") {
    params.q = qParties;
}
if (whichQ === "leader") {
    params.q = qLeaders;
}

console.log("params =", params);
T.get("search/tweets", params, gotData);

function gotData (err, data, response) {
    var name = "city_tweets/" + date + "_" + whichQ + "_" + city + ".json";
    console.log("output file =", name);

    fs.writeFile(name, JSON.stringify(data, null, 2), 'utf8', function (err) {
        if (err) {
            return console.log(err);
        }
    });
}