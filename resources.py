from __future__ import print_function
import sys
from flask import Flask, redirect, request, render_template
from flask_restful import Resource, Api
import python_docker_methods
import parser
import json



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
            try:
                containerStatus = python_docker_methods.runDockerContainer(self.dockerClient, imageName['name'], True)
                return parser.parse_elements_to_response("create", imageName['name'], "Container Created")
            except:
                return parser.parse_elements_to_response("error", imageName['name'], "No such Image")
        else:
            return parser.parse_elements_to_response("error", imageName['name'], "Empty value")


## ---- stop a container with the given id or name
class StopContainer(Resource):
    def __init__(self, **kwargs):
        self.dockerClient = kwargs['dockerClient']
    def get(self):
        return ''
    def post(self):
        containerName = request.get_json(True)
        if containerName['name'] != '':
            try:
                dockerConnection = python_docker_methods.getDockerContainer(self.dockerClient, containerName['name'])
                python_docker_methods.stopDockerContainer(dockerConnection)
                return parser.parse_elements_to_response("stop", containerName['name'], "Stopped Container")
            except:
                return parser.parse_elements_to_response("error", containerName['name'], "No such container name")
        else:
            return parser.parse_elements_to_response("error", containerName['name'], "Empty value")

## ---- remove a container
class RemoveContainer(Resource):
    def __init__(self, **kwargs):
        self.dockerClient = kwargs['dockerClient']
    def get(self):
        return ''
    def post(self):
        containerName = request.get_json(True)
        if containerName['name'] != '':
            try:
                dockerConnection = python_docker_methods.getDockerContainer(self.dockerClient, containerName['name'])
                python_docker_methods.removeDockerContainer(dockerConnection)
                return parser.parse_elements_to_response("remove", containerName['name'], "Removed container")
            except:
                return parser.parse_elements_to_response("error", containerName['name'], "No such container name")
        else:
            return parser.parse_elements_to_response("error", containerName['name'], "Empty value")


## ---- start a container
class StartContainer(Resource):
    def __init__(self, **kwargs):
        self.dockerClient = kwargs['dockerClient']
    def get(self):
        return ''
    def post(self):
        containerName = request.get_json(True)
        if containerName['name'] != '':
            try:
                dockerConnection = python_docker_methods.getDockerContainer(self.dockerClient, containerName['name'])
                python_docker_methods.startDockerContainer(dockerConnection)
                return parser.parse_elements_to_response("start", containerName['name'], "Started new container")
            except:
                return parser.parse_elements_to_response("error", containerName['name'], "No such container name")
        else:
            return parser.parse_elements_to_response("error", containerName['name'], "Empty value")

## ---- restart a running container
class RestartContainer(Resource):
    def __init__(self, **kwargs):
        self.dockerClient = kwargs['dockerClient']
    def get(self):
        return ''
    def post(self):
        containerName = request.get_json(True)
        if containerName['name'] != '':
            try:
                dockerConnection = python_docker_methods.getDockerContainer(self.dockerClient, containerName['name'])
                python_docker_methods.restartDockerContainer(dockerConnection)
                return parser.parse_elements_to_response("restart", containerName['name'], "Restarted container")
            except:
                return parser.parse_elements_to_response("error", containerName['name'], "Empty value")
        else:
            return parser.parse_elements_to_response("error", containerName['name'], "No such container name")
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
        return parser.parse_elements_to_response("name", containerNameIdPair ,"Returned container names")

##TODO ---- Need to implement separate ajax request to handle get info requests that containe json payloads
## ---- return the container logs
class GetContainerLogs(Resource):
    def __init__(self, **kwargs):
        self.dockerClient = kwargs['dockerClient']
    def post(self):
        containerName = request.get_json(True)
        if containerName['name'] != '':
            try:
                dockerConnection = python_docker_methods.getDockerContainer(self.dockerClient, containerName['name'])
                containerLogs = python_docker_methods.getDockerLogs(dockerConnection)
                return parser.parse_elements_to_response("logs", containerLogs ,"Returning logs")
            except:
                return parser.parse_elements_to_response("error", containerName['name'], "No such container name")
        else:
            return parser.parse_elements_to_response("error", containerName['name'], "Empty value")

## ---- get a list of processes running inside this container
class GetContainerProcesses(Resource):
    def __init__(self, **kwargs):
        self.dockerClient = kwargs['dockerClient']
    def post(self):
        containerName = request.get_json(True)
        if containerName['name'] != '':
            try:
                dockerConnection = python_docker_methods.getDockerContainer(self.dockerClient, containerName['name'])
                containerProcesses = python_docker_methods.getDockerProcesses(dockerConnection)
                return parser.parse_elements_to_response("processes", containerProcesses ,"Returning processes")
            except:
                return parser.parse_elements_to_response("error", containerName['name'], "No such container name")
        else:
            return parser.parse_elements_to_response("error", containerName['name'], "Empty Value")


## ---- return the cpu memory network usage of a running container
## ---- default method returns the stats instead of a stream ---- need to test moth methods
## ---- would require a separate ajax request to update the requested stats at certain intervals
class GetContainerStats(Resource):
    def __init__(self, **kwargs):
        self.dockerClient = kwargs['dockerClient']
    def post(self):
        containerName = request.get_json(True)
        if containerName['name'] != '':
            try:
                dockerConnection = python_docker_methods.getDockerContainer(self.dockerClient, containerName['name'])
                containerStats = python_docker_methods.getDockerStats(dockerConnection)
                return parser.parse_elements_to_response("stats", containerStats ,"Returning stats")
            except:
                return parser.parse_elements_to_response("error", containerName['name'], "No such container name")
        else:
            return parser.parse_elements_to_response("error", containerName['name'], "Empty Value")
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
        containerName = containerData['name']
        processName = containerData['process']
        if containerName != '' and processName != '':
            cmd = '/bin/sh -c "echo hello stdout ; echo hello stderr >&2"'
            command = 'systemctl status ' + processName + '| grep Active'
            dockerConnection = python_docker_methods.getDockerContainer(self.dockerClient, containerName)
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

##TODO ---- docker inspect container
class InspectDockerContainer(Resource):
    def __init__(self, **kwargs):
        self.dockerClient = kwargs['dockerClient']
    def get(self):
        return ''
    def post(self):
        return ''

## ---- get a new image from the repo
class GetNewImage(Resource):
    def get(self):
        return ''

## ---- get all available image names
class GetAllImages(Resource):
    def get(self):
        return ''