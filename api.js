var request = require("request");
var db = require("nedb");
infos =  new db({filename: 'db/info.db', autoload: true, timestampData: true});

var url = "https://randomuser.me/api/";

request(url, function(err, response, body) {
    if (err){
        console.log('error: ', error);
    } else {
        var person = JSON.parse(body);
        var record = person.results[0];
        r = { "name" : record.name.first + " " + record.name.last, "gender" : record.gender, "email" : record.email, "dob" : record.dob.date};
        infos.insert(r, function(err, doc) {
	    console.log("Inserted new person info: " + r.name);
        });
    }
});

infos.find({}).sort({gender: 1}).exec(function(err, docs) {
    docs.forEach(function(d) {
        console.log('Found user: ', d.name);
    });
});