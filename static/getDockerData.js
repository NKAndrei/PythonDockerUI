function callbackFunction(response) {
    console.log(response)
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