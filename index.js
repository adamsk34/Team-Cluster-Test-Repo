var fs = require("fs");
var Twit = require("twit");
var config = require("./config.json");
var party_leader = require("./party_leader/parties_leaders.json")
var all_cities = require("./city_rules/all_cities.json")

var T = new Twit(config);
var count = 100

var today = new Date()
var date = today.getFullYear() + "-" + (today.getMonth() + 1) + "-" + today.getDate();


all_cities["cities"].forEach(city => {

    var city_name = city["name"]
    var geo_code = city["geocode"]

    party_leader["parties"].forEach(party => {

        var params = {
                q : party,
                count: count,
                geocode: geo_code
            };
        
        getAndProcessTwitterData(params, city_name, "party", party);

    });

    party_leader["leaders"].forEach(leader => {

        var params = {
            q : leader,
            count: count,
            geocode: geo_code
        };

        getAndProcessTwitterData(params, city_name, "leader", leader);
    });
});


function getAndProcessTwitterData(params, city_name, whichQ, query) {

    T.get("search/tweets", params, gotData);

    function gotData (err, data, response) {
        var name = "city_tweets/" + city_name  + "_" + whichQ  + "_" + query.replace(/ /g, '-') + "_" + date + ".json";
        console.log("output file =", name);
    
        fs.writeFile(name, JSON.stringify(data, null, 2), 'utf8', function (err) {
            if (err) {
                return console.log(err);
            }
        });
    }
}


