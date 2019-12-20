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