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
            containerStatus = python_docker_methods.runDockerContainer(self.dockerClient, imageName['name'])
            print(containerStatus, file=sys.stderr)
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
            python_docker_methods.closeDockerContainer(self.dockerClient, imageName['name'])
            return 'Stopping container container ' + imageName['name']
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
            dockerContainer = python_docker_methods.connectToDockerContainer(self.dockerClient, parser.parse_container_id(containerIds[item]))
            containerNames = python_docker_methods.getDockerContainerName(dockerContainer)
            containerNameIdPair = containerNameIdPair + "\"" + containerNames + "\"" + ":" + "\"" + parser.parse_container_id(containerIds[item]) + "\"" + ","
        containerNameIdPair = containerNameIdPair.rstrip(',') + "}"
        print(containerNameIdPair, file= sys.stderr)
        return str(containerNameIdPair).replace("/","")

##! ---- Container data classes



##! ---- Image manipulation and data retrieval classes
##! ---- used to retieve images, get the names, remove images

## ---- get a new image from the repo
class GetNewImage(Resource):
    def get(self):
        return ''

## ---- get all available image names
class GetAllImages(Resource):
    def get(self):
        return ''
        
##! ---- Image manipulation and data retrieval classes
