from __future__ import print_function
import sys
from flask import Flask, redirect, request, render_template
from flask_restful import Resource, Api
import python_docker_methods
import parser



##! ---- Container manipulation classes
##! ---- Used to spin up, delete, modify containers

## ---- Create a container og the given image name
class CreateContainer(Resource):
    def __init__(self, **kwargs):
        self.dockerClient = kwargs['dockerClient']
    def get(self):
        return ''
    def post(self):
        imageName = request.get_json(True)
        if imageName['name'] != '':
            containerStatus = python_docker_methods.runDockerContainer(self.dockerClient, imageName['name'], True)
            return {"status" : 200}
            ##return { "\"" + imageName['name'] + "\"" + ":" + "\"" + str(containerStatus) + "\"" }
        else:
            return 'Image Name does not exist'

## ---- stop a container with the given id or name
class StopContainer(Resource):
    def __init__(self, **kwargs):
        self.dockerClient = kwargs['dockerClient']
    def get(self):
        return ''
    def post(self):
        imageName = request.get_json(True)
        if imageName['name'] != '':
            ## ---- stop container code here ---- name or id
            dockerConnection = python_docker_methods.getDockerContainer(self.dockerClient, imageName['name'])
            python_docker_methods.stopDockerContainer(dockerConnection)
            return {"Stopping container container " : imageName['name'] }
        else:
            return 'Image Name does not exist'

## ---- remove a container
class RemoveContainer(Resource):
    def __init__(self, **kwargs):
        self.dockerClient = kwargs['dockerClient']
    def get(self):
        return ''
    def post(self):
        imageName = request.get_json(True)
        if imageName['name'] != '':
            ## ---- stop container code here ---- name or id
            dockerConnection = python_docker_methods.getDockerContainer(self.dockerClient, imageName['name'])
            python_docker_methods.removeDockerContainer(dockerConnection)
            return {"Removing container container " : imageName['name'] }
        else:
            return 'Image Name does not exist'

## ---- start a container
class StartContainer(Resource):
    def __init__(self, **kwargs):
        self.dockerClient = kwargs['dockerClient']
    def get(self):
        return ''
    def post(self):
        imageName = request.get_json(True)
        if imageName['name'] != '':
            ## ---- stop container code here ---- name or id
            dockerConnection = python_docker_methods.getDockerContainer(self.dockerClient, imageName['name'])
            python_docker_methods.startDockerContainer(dockerConnection)
            return {"Starting  container " : imageName['name'] }
        else:
            return 'Image Name does not exist'

## ---- restart a running container
class RestartContainer(Resource):
    def __init__(self, **kwargs):
        self.dockerClient = kwargs['dockerClient']
    def get(self):
        return ''
    def post(self):
        imageName = request.get_json(True)
        if imageName['name'] != '':
            ## ---- stop container code here ---- name or id
            dockerConnection = python_docker_methods.getDockerContainer(self.dockerClient, imageName['name'])
            python_docker_methods.restartDockerContainer(dockerConnection)
            return {"Restarting  container " : imageName['name'] }
        else:
            return 'Image Name does not exist'
##! ---- Container manipulation classes



##! ---- Container data classes
##! ---- used to get/refresh certain attributes/data from running containers

## ---- return a name : id pair of all running containers
class GetAllContainers(Resource):
    def __init__(self, **kwargs):
        self.dockerClient = kwargs['dockerClient']
    def get(self):
        containerIds = python_docker_methods.listDockerContainer(self.dockerClient)
        containerNameIdPair = "{"
        for item in range(len(containerIds)):
            dockerContainer = python_docker_methods.getDockerContainer(self.dockerClient, parser.parse_container_id(containerIds[item]))
            containerNames = python_docker_methods.getDockerContainerName(dockerContainer)
            containerNameIdPair = containerNameIdPair + "\"" + containerNames + "\"" + ":" + "\"" + parser.parse_container_id(containerIds[item]) + "\"" + ","
        containerNameIdPair = containerNameIdPair.rstrip(',') + "}"
        return str(containerNameIdPair).replace("/","")

##TODO ---- Need to implement separate ajax request to handle get info requests that containe json payloads
## ---- return the container logs
class GetContainerLogs(Resource):
    def __init__(self, **kwargs):
        self.dockerClient = kwargs['dockerClient']
    def post(self):
        imageName = request.get_json(True)
        if imageName['name'] != '':
            dockerConnection = python_docker_methods.getDockerContainer(self.dockerClient, imageName['name'])
            containerLogs = python_docker_methods.getDockerLogs(dockerConnection)
            return {"Container Logs " : str(containerLogs) }
        else:
            return 'Image Name does not exist'
        return ''

## ---- get a list of processes running inside this container
class GetContainerProcesses(Resource):
    def __init__(self, **kwargs):
        self.dockerClient = kwargs['dockerClient']
    def post(self):
        imageName = request.get_json(True)
        if imageName['name'] != '':
            dockerConnection = python_docker_methods.getDockerContainer(self.dockerClient, imageName['name'])
            containerProcesses = python_docker_methods.getDockerProcesses(dockerConnection)
            return {"Running Processes " : containerProcesses }
        else:
            return 'Image Name does not exist'
        return ''

## ---- return the cpu memory network usage of a running container
## ---- default method returns the stats instead of a stream ---- need to test moth methods
## ---- would require a separate ajax request to update the requested stats at certain intervals
class GetContainerStats(Resource):
    def __init__(self, **kwargs):
        self.dockerClient = kwargs['dockerClient']
    def post(self):
        imageName = request.get_json(True)
        if imageName['name'] != '':
            dockerConnection = python_docker_methods.getDockerContainer(self.dockerClient, imageName['name'])
            containerStats = python_docker_methods.getDockerStats(dockerConnection)
            return {"Container stats " : containerStats }
        else:
            return 'Image Name does not exist'
        return ''
##! ---- Container data classes



##! ---- Image manipulation and data retrieval classes
##! ---- used to retieve images, get the names, remove images

        
##! ---- Image manipulation and data retrieval classes


##! ---- To Be Implemented
##TODO ---- implement systemctl 'process' status and return the status of the running processes inside the container
##TODO ---- to be used with GetContainer Processes to see what process is running inside the container
class GetDockerContainerProcessStatus(Resource):
    def __init__(self, **kwargs):
        self.dockerClient = kwargs['dockerClient']
    def post(self):
        containerData = request.get_json(True)
        imageName = containerData['name']
        processName = containerData['process']
        if imageName != '' and processName != '':
            cmd = '/bin/sh -c "echo hello stdout ; echo hello stderr >&2"'
            command = 'systemctl status ' + processName + '| grep Active'
            print(command, file=sys.stderr)
            dockerConnection = python_docker_methods.getDockerContainer(self.dockerClient, imageName)
            containerLogs = python_docker_methods.executeCommandInContainer(dockerConnection, command)
            return {"Container Process Status " : str(containerLogs) }
        else:
            return 'Image Name does not exist'
        return ''

##TODO ---- return the container network type, name and used ports, ip
class GetDockerContainerNetwork(Resource):
    def __init__(self, **kwargs):
        self.dockerClient = kwargs['dockerClient']
    def get(self):
        return ''
    def post(self):
        return ''
    def getNetworkTypeName(self):
        return ''
    def getPorts(self):
        return ''

## ---- get a new image from the repo
class GetNewImage(Resource):
    def get(self):
        return ''

## ---- get all available image names
class GetAllImages(Resource):
    def get(self):
        return ''