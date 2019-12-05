import subprocess
import os
import docker



#! -- a series of commmands defined for testing purposes
def terminalCommands(): 
    print("lala")
    pyCommand = subprocess.run(["ls", "-al"], stdout=subprocess.PIPE)
    print(pyCommand.stdout.decode())
    pyCommand2 = subprocess.run(["grep", "la"], input=pyCommand.stdout, stdout=subprocess.PIPE)
    print(pyCommand2.stdout.decode())
    print('olla2')

def terminalDockerCommands():
    dockerCommand1 = subprocess.run(["docker", "ps"], stdout=subprocess.PIPE)
    print(dockerCommand1.stdout.decode())
    dockerCommand2 = subprocess.run(["docker", "pull", "hello-world"], stdout=subprocess.PIPE)
    print(dockerCommand2.stdout.decode())
    dockerCommand3 = subprocess.run(["docker", "images"], stdout=subprocess.PIPE)
    print(dockerCommand3.stdout.decode())
    dockerCommand4 = subprocess.run(["grep", "latest"], input=dockerCommand3.stdout, stdout=subprocess.PIPE)
    print(dockerCommand4.stdout.decode())
    print(dockerCommand4.stdout)

def otherCommands(filename):

    fileName = filename
    pyCommand = subprocess.run(["cat", fileName], stdout=subprocess.PIPE)
    fileContents = pyCommand.stdout.decode()
    print(fileContents)
    return "ok"
#! -- a series of commmands defined for testing purposes


##TODO ---- need to refactor the names of the methods to be more intuitive
def getDockerClient():
    dockerClient = docker.from_env()
    return dockerClient

def listDockerImages(dockerClient):
    imageList = dockerClient.images.list(all=True)
    return imageList

def listDockerContainer(dockerClient):
    containerList = dockerClient.containers.list(all=True)
    return containerList

def getDockerContainers(dockerClient, containerList): #? -- how should we get them --- by id by name by order number
    return ""                                           #TODO -- need to implement

def getDockerContainerName(containerConnection): #? -- how should we get them --- by id by name by order number
    name = containerConnection.attrs['Name']
    return name                                           #TODO -- need to implement
    
def runDockerContainer(dockerClient, dockerImageName):
    containerLogs = dockerClient.containers.run(dockerImageName)
    return containerLogs

def closeDockerContainer(dockerClient, containerID): #? ---- should it return a message
     return dockerClient.api.remove_container(containerID)

def connectToDockerContainer(dockerClient, containerID):
    containerObject = dockerClient.containers.get(containerID)
    return containerObject

def getDockerContainerInfo(containerConnection):
    containerInfo = containerConnection.attrs
    return containerInfo

