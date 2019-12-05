from python_docker_methods import terminalCommands, getDockerClient,listDockerImages, runDockerContainer, listDockerContainer, closeDockerContainer, connectToDockerContainer
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
containerLog = runDockerContainer(dockerClient, trimmedString)
print(containerLog.decode())
time.sleep(5)

## ---- get the container list and connect to a container
containerList = listDockerContainer(dockerClient)
print("TRIMMING THE LIST")
print(str(containerList))
print(str(containerList))
trimmedContainerList = re.search(': (.+?)>', str(containerList)).group().replace(":","").replace(">","").replace(" ","")
print(trimmedContainerList)
containerConnection = connectToDockerContainer(dockerClient, trimmedContainerList)
time.sleep(5)
containerConnection.reload()
print('Configuration ' + containerConnection.attrs['Config']['Image'])
print('ID ' + containerConnection.attrs['Id'])
print('ID ' + containerConnection.attrs['Name'])
pp.pprint(containerConnection.attrs)
print(containerConnection.logs())

## ---- stop, remove and check if the docker container has been removed
stopContainer = closeDockerContainer(dockerClient, trimmedContainerList)
listDockerContainer(dockerClient)
print(stopContainer)