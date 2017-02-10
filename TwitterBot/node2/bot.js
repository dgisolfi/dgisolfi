//bot.js
//2.8
//Daniel Gisolfi

//Print message notifing user, bot is begining
console.log('The bot is starting')

//Import and require the twit package
var Twit = require('twit');
//Import and require the config file for tokens package
var config = require('./config');

//Declare a variable for the twit package and use config in it
var T = new Twit(config);

//search parameters for twitter
var params = {
	//what key words and date params
	q:'weed since:2011-07-11',
	//how much data
	count: 2
}

//get info from twitter
T.get('search/tweets', params, gotData);

//run through tweets with loop
function gotData(err, data, response) {
  var tweets = data.statuses;
  for (var i = 0; i < tweets.length; i++) {
    console.log(tweets[i].text);  	
  }
}