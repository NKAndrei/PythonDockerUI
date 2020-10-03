function callbackFunction(response) {
    jsonResponseFromApi = response
    parseAPIResponse() // ---- added 
        //console.log(response)
    return response;
}
//TODO ---- will need to split this asynchronous request into multiple parts
//TODO ---- and add a timer to be able to refresh the container data automatically
// ---- get name, id, status, a
function getDockerData(dataEndpoint) {
    var urlAddress = "http://127.0.0.1:5000/" + dataEndpoint;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            callbackFunction(xhttp.responseText);
        }
    }
    xhttp.open('GET', urlAddress);
    xhttp.send();
}
function pullDockerImage(dataEndpoint) {
    var urlAddress = "http://127.0.0.1:5000/" + dataEndpoint;
    var xhttp = new XMLHttpRequest();
    var imageName = document.getElementById("imageName").value;
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            callbackFunction(xhttp.responseText);
        }
    }
    containerJson = "{" + "\"name\"" + ":" + "\"" + imageName + "\"" + "}"
    xhttp.open('POST', urlAddress, true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send(containerJson);
}

function getDockerProcess(dockerCommand) {
    var xhttp = new XMLHttpRequest();
    var urlAddress = 'http://127.0.0.1:5000/' + dockerCommand
    containerType = document.getElementById("imageName").value
    containerProcess = document.getElementById("containerProcess").value
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            callbackFunction(xhttp.responseText);
        }
    }
    containerJson = "{" + "\"name\"" + ":" + "\"" + containerType + "\"" + "," + "\"process\"" + ":" + "\"" + containerProcess + "\"" + "}"
    xhttp.open("POST", urlAddress, true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send(containerJson);
}