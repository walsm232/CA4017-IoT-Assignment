/* JavaScript */

function runScript() {
    var request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if (request.readyState === 4) {
            if (request.status === 200) {
                alert('Successfully ran the MQTT application' + request.responseText);
            } else {
                alert('Application failed to launch' + request.status);
            }
        }
    };
    request.open('POST', '../../app.py', true);
    request.send(null);
    return false;  
};

document.getElementById('script-button').onclick = runScript;