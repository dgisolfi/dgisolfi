# Marist Registration Script

####Original script was written by Evan Hopkins, Antony Liang, Bob Nisco

####Updated script was written by Daniel Gisolfi

The following script was written by Evan Hopkins, Antony Liang, and Bob Nisco in 2012 since then the registrar department has changed the banner system. To update the script, when helping my sister register, I found the new links to the new version of banner and have updated them with the file. The following is a basic guide on how to use this script.

Note: I take no credit for creating this script and give full credit to the above-mentioned creators all I have done is changed the links it is directed to.

##How-To

**Step 1**

Add [tampermonkey](https://tampermonkey.net) (or any other browser extension that allows you to run scripts on a site) to your browser of choice.

**Step 2**

Once you have added the web extension create a new script, in tampermonkey click the extension symbol and press "create new script" or dashboard if the extension is disabled.

**Step 3**

Once in a new script copy the entire [RegistrationScript](https://github.com/dgisolfi/dgisolfi/blob/master/MaristRegistrationScript/RegistrationScript.js) file and place it in the new script, replacing all pre-existing text.

Shortcut: **command(ctr)** + a then **command(ctr) + v** into the empty script

**Step 4**

Within the script there is crn array, within the array input your crns for the schedule you would like.

EX:

```js
//If you only have 5 or 4 classes just remove the extra commas and quotations
var crns = ["12339" , "10478" , "12292" , "10131" , "12315", "10677"];
```

**Step 5**

Save the script to tampermonkey using either **command(ctr) + s** or clicking floppy disk image in the top left.

**Step 6**

Open a new tab to the [registration](https://ssb1.banner.marist.edu:8012/MARPROD/bwskfreg.P_AltPin) page the script should immediately start running and refresh the page over and over until you are able to register when it puts all crn's from the script into the crn fields and submits the form.

**Step 7**

Run the script on a computer with a good internet connection a few minutes before your scheduled registration time and relax as the script registers for you.



###Troubleshooting

If the script is not refreshing the registration page check:
* That the tampermonkey is enabled
* That Registration Script is turned on
* That you are on the correct above-mentioned site

Make sure you have saved the script, otherwise, the random crn numbers I have put into the array will be used as your crns

If the script is broken and you have checked the above suggestions please report an [Issuee](https://github.com/dgisolfi/dgisolfi/issues) through GitHub 

