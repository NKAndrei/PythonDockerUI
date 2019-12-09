from python_docker_methods import terminalCommands, getDockerClient,listDockerImages, runDockerContainer, listDockerContainer, stopDockerContainer, getDockerContainer, executeCommandInContainer, removeDockerContainer
import re
import time
import pprint

pp = pprint.PrettyPrinter(indent=4)
## ---- random terminal commands for testing purposes
terminalCommands()

## ---- pull and list the downloaded docker image
dockerClient = getDockerClient()
dockerImages = listDockerImages(dockerClient)
print(dockerImages)

## ---- get docker image name and spin up a container
dockerImageStr = str(dockerImages)
string = re.search('\'(.+?)\'',dockerImageStr)
trimmedString = string.group().replace("'", "")
print(trimmedString)
print("BELOW IS CONTAINER LOG")
command = "bash -c 'for i in {1..100}; sleep 2s; done'"
##containerLog = runDockerContainer(dockerClient, trimmedString, command)
containerLog = runDockerContainer(dockerClient, trimmedString, True)
print(containerLog)
print("ABOVE IS CONTAINER LOG")
time.sleep(5)

## ---- get the container list and connect to a container
containerList = listDockerContainer(dockerClient)
print("TRIMMING THE LIST")
print(str(containerList))
trimmedContainerList = re.search(': (.+?)>', str(containerList)).group().replace(":","").replace(">","").replace(" ","")
print(trimmedContainerList)
print("TRIMMING THE LIST")

containerConnection = getDockerContainer(dockerClient, trimmedContainerList)
time.sleep(5)
print("EXECUTING A COMMAND")
cmd = '/bin/sh -c "echo hello stdout ; echo hello stderr >&2"'
print(executeCommandInContainer(containerConnection, cmd))
print("EXECUTING A COMMAND")

print("PRINTING CONTAINER ATTRIBUTES")
containerConnection.reload()
print('Configuration ' + containerConnection.attrs['Config']['Image'])
print('ID ' + containerConnection.attrs['Id'])
print('ID ' + containerConnection.attrs['Name'])
##pp.pprint(containerConnection.attrs)
print("PRINTING CONTAINER ATTRIBUTES")

print("PRINTING CONTAINER LOGS")
print(containerConnection.logs())
print("PRINTING CONTAINER LOGS")


## ---- stop, remove and check if the docker container has been removed
stopContainer = stopDockerContainer(containerConnection)
removeContainer = removeDockerContainer(containerConnection)
listDockerContainer(dockerClient)
##print(stopContainer)