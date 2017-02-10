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


//Setting up a user stream
var stream = T.stream('user');
//Anytime someone follows me
stream.on('follow', followed);

fucntion followed(eventMsg) {
	console.log('Follow event triggered, thanking user')
	var name = eventMsg.source.name;
	var screenname = eventMsg.source.screenname;
	tweetIt('@' + screenname + 'Thanks for following me!' 
			+'Prepare yourself to be disappointed.');
}

//Posting on twitter

//Setting an interval for when to tweet
setInterval(tweetIt, 1000*3600) // 1 hour
//call function to tweet txt parameter
tweetIt();

//Create a function for tweeting
function tweetIt(txt) {
	//status = text to be tweeted
	var tweet = {
		status: txt
	}

	//Post on Twitter
	T.post('statuses/update', tweet, tweeted);

	//Return wether the program completed task
	function tweeted(err, data, response) {
	  if (err) {
	  	console.log("Tweet was unsuccessful");
	  } else {
	    console.log("Tweet was successful");
	  }
	}
}
