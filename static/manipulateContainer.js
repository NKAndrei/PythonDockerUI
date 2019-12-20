function callbackFunction(response) {
    jsonResponseFromApi = response
        //console.log(response)
    return response
}

// ---- create, run, delete, restart containers
function manipulateContainer(dockerCommand) {
    var xhttp = new XMLHttpRequest();
    var urlAddress = 'http://127.0.0.1:5000/' + dockerCommand
    containerType = document.getElementById("imageName").value
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            callbackFunction(xhttp.responseText);
        }
    }
    containerTypeJson = "{" + "\"name\"" + ":" + "\"" + containerType + "\"" + "}"
    console.log(containerTypeJson)
    xhttp.open("POST", urlAddress, true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send(containerTypeJson);
}