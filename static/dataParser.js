// ---- get container names from api and populate the dropdown list
function getContainerNames(type) {
    var containerListElement = document.getElementById(type);
    var containerList = containerNames;
    if(containerListElement.options.length <1){
        var selectOption = document.createElement("option");
        selectOption.appendChild(document.createTextNode(containerList[1])) // ---- needs to be modified to remove text nodes
        selectOption.setAttribute("value", containerList[1])
        containerListElement.appendChild(selectOption);
    }
    for (i = 0; i < containerList.length; i++) {
        for (x = 0; x < containerListElement.options.length; x++) {
            if(containerListElement.options[x].value == containerList[i]){
                break;
            }
            else if(x == containerListElement.options.length -1) {
                var selectOption = document.createElement("option");
                selectOption.appendChild(document.createTextNode(containerList[i])) // ---- needs to be modified to remove text nodes
                selectOption.setAttribute("value", containerList[i])
                containerListElement.appendChild(selectOption);
            }
        }
    }
}

// ---- get the selected value from the dropdown list and assign it to a global variable
function getSelectedDropValue(dropDownList) {
    selectedContainerName = dropDownList.options[dropDownList.selectedIndex].text;
    console.log(selectedContainerName)
}

//TODO ---- define methods
//TODO ---- create dropdown list containing all of the below 
//TODO ---- another dropdown list will be populated with the filter options
//TODO ---- select both and return the result
function getContainerLogs() {
    textArea = document.getElementById("temporaryTextArea");
    textArea.innerHTML = containerLogs;
    // ---- gel all logs or get certain information from logs with the given keys
    // ---- neet to offer a set of given keys
    // ---- get logs by key
    // ---- get logs by date/time
    // ---- get logs by type error/info/warning
    return ''
}

function getContainerErrors() {
    // ---- get all errors
    // ---- filter as the logs
    textArea = document.getElementById("temporaryTextArea");
    textArea.innerHTML = containerError;
    return ''
}

function getContainerStats() {
    // ---- get CPU
    // ---- memory
    // ---- HDD
    textArea = document.getElementById("temporaryTextArea");
    textArea.innerHTML = containerStats;
    return ''
}

function getContainerStatus() {
    textArea = document.getElementById("temporaryTextAreaStatus");
    textArea.innerHTML = containerProcesses;
    // ---- start restart remove stop
    return ''
}

function getContainerProcesses() {
    // ---- get list of running processes
    // ---- get the status of the selected process
    // ---- get information related to the process ---- port, ip, dir, etc
    textArea = document.getElementById("temporaryTextArea");
    textArea.innerHTML = containerProcesses;
    return ''
}

function filterData() {
    // ---- takes a global variable and filter method(key, date, type etc)
    // ---- returns result
    textArea = document.getElementById("temporaryTextArea");
    textArea.innerHTML = containerLogs;
    return ''
}

//TODO ---- get the first name key/value and assign an appropriate variable 
//TODO ---- can use switch
// error
// create
// remove
// stats
// stop
// process
// logs
// name
// restart
// start
// ---- can create an api call to get all available key names from the API and loop through them
// ---- need to create variable dynamically according to the number of keys and names from api
// ---- create the simple method first
// ---- rename the method
function parseAPIResponse(type) {
    var jsonObject = JSON.parse(jsonResponseFromApi);
    var keys = Object.keys(jsonObject)
    var firstKey = jsonObject[keys[0]]
    console.log(jsonObject);
    if (firstKey == "create") {
        containerCrete = jsonObject
    } else if (firstKey == "stop") {
        containerStop = jsonObject
    } else if (firstKey == "remove") {
        containerRemove = jsonObject
    } else if (firstKey == "start") { // ---- the rest of these variables will be temporary based on the action on the containers from the name
        containerStart = jsonObject
    } else if (firstKey == "restart") {
        containerRestart = jsonObject
    } else if (firstKey == "name") { // ---- this variable will contain all container name
        listOfNames = []
        listOfNames = loopThroughJsonObject(keys, jsonObject);
        containerNames = ""
        containerNames = listOfNames
        console.log(containerNames)
        getContainerNames(type);
    } else if (firstKey == "logs") {
        containerLogs = jsonObject
    } else if (firstKey == "processes") {
        containerProcesses = jsonObject
    } else if (firstKey == "stats") {
        containerStats = jsonObject
    } else if (firstKey == "error") {
        containerError = jsonObject
    }else{
        console.log(jsonObject);
    }
    return "";
}

function loopThroughJsonObject(key, jsonObject) {
    //! ---- get the depth of the object to make the method as generic as possible
    //! ---- could make the method recursive and extract e new key every time
    var result = [];
    for (item in jsonObject[key[1]]) {
        result.push(jsonObject[key[1]][item])
            //TODO ---- modify this to return the names instead of container id
    }
    return result;
}