(function() {
	// Get some required handles
	var video = document.getElementById('v');
	var recStatus = document.getElementById('recStatus');
	var startRecBtn = document.getElementById('startRecBtn');
	var stopRecBtn = document.getElementById('stopRecBtn');

	// Define a new speech recognition instance
	var rec = null;
	try {
		rec = new webkitSpeechRecognition();
	} 
	catch(e) {
    	document.querySelector('.msg').setAttribute('data-state', 'show');
    	startRecBtn.setAttribute('disabled', 'true');
    	stopRecBtn.setAttribute('disabled', 'true');
    }
    if (rec) {
		rec.continuous = true;
		rec.interimResults = false;
		rec.lang = 'en';

		// Define a threshold above which we are confident(!) that the recognition results are worth looking at 
		var confidenceThreshold = 0.5;

		// Simple function that checks existence of s in str
		var userSaid = function(str, s) {
			return str.indexOf(s) > -1;
		}

		// Highlights the relevant command that was recognised in the command list for display purposes
		var highlightCommand = function(cmd) {
			var el = document.getElementById(cmd); 
			el.setAttribute('data-state', 'highlight');
			setTimeout(function() {
				el.setAttribute('data-state', '');
			}, 3000);
		}

		// Process the results when they are returned from the recogniser
		rec.onresult = function(e) {
			// Check each result starting from the last one
			for (var i = e.resultIndex; i < e.results.length; ++i) {
				// If this is a final result
	       		if (e.results[i].isFinal) {
	       			// If the result is equal to or greater than the required threshold
	       			if (parseFloat(e.results[i][0].confidence) >= parseFloat(confidenceThreshold)) {
		       			var str = e.results[i][0].transcript;
		       			console.log('Recognised: ' + str);
		       			alert(str)
		       			// If the user said 'video' then parse it further
		       			if (userSaid(str, 'video')) {
		       				// play the video
		       				if (userSaid(str, 'on')) {
		       					video.play();
		       					highlightCommand('vidPlay');
		       				}
		       				// Stop the video
		       				else if (userSaid(str, 'of')) {
		       					video.pause();
		       					highlightCommand('vidStop');
		       				}
		       			}
	       			}
	        	}
	    	}
		};

		// Start speech recognition
		var startRec = function() {
			rec.start();
			recStatus.innerHTML = ' Activado y en escucha';
		}
		// Stop speech recognition
		var stopRec = function() {
			rec.stop();
			recStatus.innerHTML = ' Desactivado y mudo';
		}
		// Setup listeners for the start and stop recognition buttons
		startRecBtn.addEventListener('click', startRec, false);
		stopRecBtn.addEventListener('click', stopRec, false);
	}
})();

document.getElementById('stopRecBtn').addEventListener('click', changeColor);
function changeColor() {
        startRecBtn.style.backgroundColor = "grey";
    this.style.backgroundColor = "red";
    return false;

}
document.getElementById('startRecBtn').addEventListener('click', changeColor);
function changeColor() {
        stopRecBtn.style.backgroundColor = "grey";
    this.style.backgroundColor = "red";
    return false;

}

