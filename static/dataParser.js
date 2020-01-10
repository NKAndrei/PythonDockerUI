// ---- get container names from api and populate the dropdown list
function getContainerNames() {
    var containerListElement = document.getElementById("dockerContainerNames");
    var containerList = containerNames;
    console.log("Getting container names")
    console.log(containerList)
    for (i = 0; i < containerList.length; i++) {
        var selectOption = document.createElement("option");
        selectOption.appendChild(document.createTextNode(containerList[i]))
        selectOption.setAttribute("value", containerList[i])
        containerListElement.appendChild(selectOption);
    }
}

// ---- get the selected value from the dropdown list and assign it to a global variable
function getSelectedDropValue(dropDownList) {
    selectedContainerName = dropDownList.options[dropDownList.selectedIndex].text;
}

//TODO ---- define methods
//TODO ---- create dropdown list containing all of the below 
//TODO ---- another dropdown list will be populated with the filter options
//TODO ---- select both and return the result
function getContainerLogs(PLACEHOLDER) {
    // ---- gel all logs or get certain information from logs with the given keys
    // ---- neet to offer a set of given keys
    // ---- get logs by key
    // ---- get logs by date/time
    // ---- get logs by type error/info/warning
    return ''

}

function getContainerErrors(PLACEHOLDER) {
    // ---- get all errors
    // ---- filter as the logs
    return ''
}

function getContainerStats(PLACEHOLDER) {
    // ---- get CPU
    // ---- memory
    // ---- HDD
    return ''
}

function getContainerProcesses(PLACEHOLDER) {
    // ---- get list of running processes
    // ---- get the status of the selected process
    // ---- get information related to the process ---- port, ip, dir, etc
    return ''
}

function filterData(GLOBALVAR, FILTERMETHOD, PLACEHOLDER) {
    // ---- takes a global variable and filter method(key, date, type etc)
    // ---- returns result
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
function parseAPIResponse() {
    var jsonObject = JSON.parse(jsonResponseFromApi);
    var keys = Object.keys(jsonObject)
    var firstKey = jsonObject[keys[0]]
    console.log("KEY AND JSON OBJECT")
    console.log(jsonObject)
    if (firstKey == "create") {
        //     // ---- do something
    }
    // else if(firstKey == "stop"){
    //     // ---- do something
    // }
    // else if(firstKey == "remove"){
    //     // ---- do something
    // }
    // else if(firstKey == "start"){
    //     // ---- do something
    // }
    // else if(firstKey == "restart"){
    //     // ---- do something
    // }
    else if (firstKey == "name") {
        listOfNames = []
        listOfNames = loopThroughJsonObject(keys, jsonObject);
        containerNames = listOfNames
        console.log(containerNames)
    } else if (firstKey == "logs") {
        containerLogs = jsonObject
    } else if (firstKey == "processes") {
        containerProcesses = jsonObject
    } else if (firstKey == "stats") {
        containerStats = jsonObject
    } else if (firstKey == "error") {
        containerError = jsonObject
    }
    return "";
}

function loopThroughJsonObject(key, jsonObject) {
    //! ---- get the depth of the object to make the method as generic as possible
    //! ---- could make the method recursive and extract e new key every time
    var result = [];
    for (item in jsonObject[key[1]]) {
        result.push(jsonObject[key[1]][item])
    }
    return result;
}