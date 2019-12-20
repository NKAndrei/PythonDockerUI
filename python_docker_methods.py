import subprocess
import os
import docker

##TODO ---- refactor or create extra docker methos that are executed through subprocess and os

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

def getDockerContainerName(containerConnection):
    name = containerConnection.attrs['Name']
    return name                                           #TODO -- need to implement
    
def runDockerContainer(dockerClient, dockerImageName, detachContainer, commands=None):
    if commands != '':
        container = dockerClient.containers.run(dockerImageName, detach=detachContainer, command=commands)
        return container
    else:
        container = dockerClient.containers.run(dockerImageName, detach=detachContainer)
        return container

##TODO ---- the start/stop/remove container methods can be grouped into one with conditionals
def startDockerContainer(containerConnection):
    return containerConnection.start()

def stopDockerContainer(containerConnection):
    return containerConnection.stop()

def removeDockerContainer(containerConnection):
    return containerConnection.remove()

def restartDockerContainer(containerConnection, time=None):
    if time is None:
        containerRestart = containerConnection.restart()
    else:
        containerRestart = containerConnection.restart(time=time)
    return containerRestart

def getDockerContainer(dockerClient, containerID):
    containerObject = dockerClient.containers.get(containerID)
    return containerObject

def getDockerContainerInfo(containerConnection):
    containerInfo = containerConnection.attrs
    return containerInfo

def executeCommandInContainer(containerConnection, command):
    response = containerConnection.exec_run(command, stream=False, demux=False)
    return response.output

def getDockerProcesses(containerConnection):
    dockerProcesses = containerConnection.top()
    return dockerProcesses

def getDockerLogs(containerConnection):
    dockerLogs = containerConnection.logs()
    return dockerLogs

def getDockerStats(containerConnection, stream=None):
    if stream is None:
        dockerStats = containerConnection.stats(stream=False)
    else:
        dockerStats = containerConnection.stats(stream = stream)
    return dockerStats

##! ---- Docker commands with Python os and subprocess
def getDockerClientOS():
    return ''

def listDockerImagesOS():
    dockerCommand3 = subprocess.run(["docker", "images"], stdout=subprocess.PIPE)
    print(dockerCommand3.stdout.decode())
    return dockerCommand3.stdout.decode()

def listDockerContainerOS():
    return ''

def getDockerContainerNameOS():
    return ''
    
def runDockerContainerOS():
    return ''

def startDockerContainerOS():
    return ''

def stopDockerContainerOS():
    return ''

def removeDockerContainerOS():
    return ''

def restartDockerContainerOS():
    return ''

def getDockerContainerOS():
    return ''

def getDockerContainerInfoOS():
    return ''

def executeCommandInContainerOS():
    return ''

def getDockerProcessesOS():
    return ''

def getDockerLogsOS():
    return ''

def getDockerStatsOS():
    return ''