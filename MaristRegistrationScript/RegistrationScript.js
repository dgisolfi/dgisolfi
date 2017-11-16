// ==UserScript==
// @name Super Registration Sniper
// @namespace https://github.com/dgisolfi/dgisolfi/blob/master/MaristRegistrationScript/MaristRegistrationScript.md
// @version 2.1.2
// @description Registers user for classes in under a second
// @include https://ssb1.banner.marist.edu:8012/MARPROD/bwskfreg.P_AltPin
// @copyright 2012+, Evan Hopkins, Antony Liang, Bob Nisco
// ==/UserScript==
//USAGE: Add in the CRN numbers of your classes into the crns array on line 25.
// Load script on the 'Student' tab of the 'Banner Self Service' tab
// of My Marist. The script will launch upon clicking the 'add or drop classes' option.
//verifies user is on pre-registration page and then adds CRN's then submits form

if (window.location == 'https://ssb1.banner.marist.edu:8012/MARPROD/bwskfreg.P_AltPin') {
	// continuously refreshes the page until the textfields are there
	if (document.getElementById('crn_id1') === null) {
		location.reload();
	} else {
		// Put your CRNS in this array
		var crns = ["00000" , "11111" , "22222" , "33333" , "44444", "55555"];
		for (var i = 0; i < crns.length; i++) {
		document.getElementById('crn_id' + (i + 1)).value = crns[i];
	}
	//submits form
	document.getElementsByName('REG_BTN')[1].click();
}
} else if(window.location == 'https://ssb1.banner.marist.edu:8012/MARPROD/bwckcoms.P_Regs') {
	alert("Success!");
}
return;