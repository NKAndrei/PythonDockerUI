from __future__ import print_function
import sys
from flask import Flask, redirect, request, render_template
from flask_restful import Resource, Api
import python_docker_methods
import parser
import json
import random



##! ---- Container manipulation classes
##! ---- Used to spin up, delete, modify containers

## ---- Create a container og the given image name
class CreateContainer(Resource):
    def __init__(self, **kwargs):
        self.docker_client = kwargs['docker_client']
    def get(self):
        return ''
    def post(self):
        image_name = request.get_json(True)
        
        if image_name['name'] != '':
            try:
                container_status = python_docker_methods.run_docker_container(self.docker_client, image_name['name'], True)
                return parser.parse_elements_to_response("create", image_name['name'], "Container Created")
            except:
                return parser.parse_elements_to_response("error", image_name['name'], "No such Image")
        else:
            return parser.parse_elements_to_response("error", image_name['name'], "Empty value")


## ---- stop a container with the given id or name
class StopContainer(Resource):
    def __init__(self, **kwargs):
        self.docker_client = kwargs['docker_client']
    def get(self):
        return ''
    def post(self):
        container_name = request.get_json(True)
        
        if container_name['name'] != '':
            try:
                docker_connection = python_docker_methods.get_docker_container(self.docker_client, container_name['name'])
                python_docker_methods.stop_docker_container(docker_connection)
                return parser.parse_elements_to_response("stop", container_name['name'], "Stopped Container")
            except:
                return parser.parse_elements_to_response("error", container_name['name'], "No such container name")
        else:
            return parser.parse_elements_to_response("error", container_name['name'], "Empty value")

## ---- remove a container
class RemoveContainer(Resource):
    def __init__(self, **kwargs):
        self.docker_client = kwargs['docker_client']
    def get(self):
        return ''
    def post(self):
        container_name = request.get_json(True)
        
        if container_name['name'] != '':
            try:
                docker_connection = python_docker_methods.get_docker_container(self.docker_client, container_name['name'])
                python_docker_methods.remove_docker_container(docker_connection)
                return parser.parse_elements_to_response("remove", container_name['name'], "Removed container")
            except:
                return parser.parse_elements_to_response("error", container_name['name'], "No such container name")
        else:
            return parser.parse_elements_to_response("error", container_name['name'], "Empty value")


## ---- start a container
class StartContainer(Resource):
    def __init__(self, **kwargs):
        self.docker_client = kwargs['docker_client']
    def get(self):
        return ''
    def post(self):
        container_name = request.get_json(True)
        
        if container_name['name'] != '':
            try:
                docker_connection = python_docker_methods.get_docker_container(self.docker_client, container_name['name'])
                python_docker_methods.start_docker_container(docker_connection)
                return parser.parse_elements_to_response("start", container_name['name'], "Started new container")
            except:
                return parser.parse_elements_to_response("error", container_name['name'], "No such container name")
        else:
            return parser.parse_elements_to_response("error", container_name['name'], "Empty value")

## ---- restart a running container
class RestartContainer(Resource):
    def __init__(self, **kwargs):
        self.docker_client = kwargs['docker_client']
    def get(self):
        return ''
    def post(self):
        container_name = request.get_json(True)
        
        if container_name['name'] != '':
            try:
                docker_connection = python_docker_methods.get_docker_container(self.docker_client, container_name['name'])
                python_docker_methods.restart_docker_container(docker_connection)
                return parser.parse_elements_to_response("restart", container_name['name'], "Restarted container")
            except:
                return parser.parse_elements_to_response("error", container_name['name'], "Empty value")
        else:
            return parser.parse_elements_to_response("error", container_name['name'], "No such container name")
##! ---- Container manipulation classes



##! ---- Container data classes
##! ---- used to get/refresh certain attributes/data from running containers

## ---- return a name : id pair of all running containers
class GetAllContainers(Resource):
    def __init__(self, **kwargs):
        self.docker_client = kwargs['docker_client']
    def get(self):
        container_ids         = python_docker_methods.list_docker_containers(self.docker_client)
        container_nameid_pair = "{"
        
        for item in range(len(container_ids)):
            docker_container      = python_docker_methods.get_docker_container(self.docker_client, parser.parse_container_id(container_ids[item]))
            container_names       = python_docker_methods.get_docker_container_name(docker_container)
            container_nameid_pair = container_nameid_pair + "\"" + container_names + "\"" + ":" + "\"" + parser.parse_container_id(container_ids[item]) + "\"" + ","
        
        container_nameid_pair = container_nameid_pair.rstrip(',') + "}"
        return parser.parse_elements_to_response("name", container_nameid_pair ,"Returned container names")

##TODO ---- Need to implement separate ajax request to handle get info requests that containe json payloads
## ---- return the container logs
class GetContainerLogs(Resource):
    def __init__(self, **kwargs):
        self.docker_client = kwargs['docker_client']
    def post(self):
        container_name = request.get_json(True)
        
        if container_name['name'] != '':
            try:
                docker_connection = python_docker_methods.get_docker_container(self.docker_client, container_name['name'])
                container_logs    = python_docker_methods.get_docker_logs(docker_connection)
                return parser.parse_elements_to_response("logs", container_logs ,"Returning logs")
            except:
                return parser.parse_elements_to_response("error", container_name['name'], "No such container name")
        else:
            return parser.parse_elements_to_response("error", container_name['name'], "Empty value")

## ---- get a list of processes running inside this container
class GetContainerProcesses(Resource):
    def __init__(self, **kwargs):
        self.docker_client = kwargs['docker_client']
    def post(self):
        container_name = request.get_json(True)
        
        if container_name['name'] != '':
            try:
                docker_connection   = python_docker_methods.get_docker_container(self.docker_client, container_name['name'])
                container_processes = python_docker_methods.get_docker_processes(docker_connection)
                return parser.parse_elements_to_response("processes", container_processes ,"Returning processes")
            except:
                return parser.parse_elements_to_response("error", container_name['name'], "No such container name")
        else:
            return parser.parse_elements_to_response("error", container_name['name'], "Empty Value")


## ---- return the cpu memory network usage of a running container
## ---- default method returns the stats instead of a stream ---- need to test moth methods
## ---- would require a separate ajax request to update the requested stats at certain intervals
class GetContainerStats(Resource):
    def __init__(self, **kwargs):
        self.docker_client = kwargs['docker_client']
    def post(self):
        container_name = request.get_json(True)
        
        if container_name['name'] != '':
            try:
                docker_connection = python_docker_methods.get_docker_container(self.docker_client, container_name['name'])
                container_stats   = python_docker_methods.get_docker_stats(docker_connection)
                return parser.parse_elements_to_response("stats", container_stats ,"Returning stats")
            except:
                return parser.parse_elements_to_response("error", container_name['name'], "No such container name")
        else:
            return parser.parse_elements_to_response("error", container_name['name'], "Empty Value")
##! ---- Container data classes



##! ---- Image manipulation and data retrieval classes
##! ---- used to retieve images, get the names, remove images
##! ---- Image manipulation and data retrieval classes



##! ---- To Be Implemented
##TODO ---- implement systemctl 'process' status and return the status of the running processes inside the container
##TODO ---- to be used with GetContainer Processes to see what process is running inside the container
class GetDockerContainerProcessStatus(Resource):
    def __init__(self, **kwargs):
        self.docker_client = kwargs['docker_client']
    def post(self):
        container_data = request.get_json(True)
        container_name = container_data['name']
        process_name   = container_data['process']
        
        if container_name != '' and process_name != '':
            cmd               = '/bin/sh -c "echo hello stdout ; echo hello stderr >&2"'
            command           = 'systemctl status ' + process_name + '| grep Active'
            docker_connection = python_docker_methods.get_docker_container(self.docker_client, container_name)
            container_logs    = python_docker_methods.execute_command_in_container(docker_connection, command)
            return {"Container Process Status " : str(container_logs) }
        else:
            return 'Image Name does not exist'
        return ''



##TODO ---- Pull docker images
class PullDockerImage(Resource):
    def __init__(self, **kwargs):
        self.docker_client = kwargs['docker_client']
        ##self.docker_image_name = kwargs['docker_image_name']
    def get(self):
        return ''
    def post(self):
        image_data      = request.get_json(True)
        image_name      = image_data['name']
        docker_image    = python_docker_methods.pull_docker_image(self.docker_client, image_name)
        return {"Pulled Image" : str(docker_image)}

## ---- get all available image names
class GetAllImages(Resource):
    def __init__(self, **kwargs):
        self.docker_client = kwargs["docker_client"]
    def get(self):
        image_list      = "{"
        id_number       = 0
        raw_image_list  = python_docker_methods.list_docker_images(self.docker_client)
        
        for item in range(len(raw_image_list)):
            n           = random.randint(1,30)
            id_number   = id_number + n
            image_name  = parser.parse_image_name(str(raw_image_list[item]))
            image_list  = image_list + "\"" + str(id_number) + "\"" + ":" + "\"" + str(image_name) + "\"" + ","
        
        image_list = image_list.rstrip(',') + "}"
        return parser.parse_elements_to_response("name", image_list ,"Returned image names")
        
class RemoveDockerImage(Resource):
    def __init__(self, **kwargs):
        self.docker_client = kwargs["docker_client"]
    def post(self):
        image_data      = request.get_json(True)
        image_name      = image_data['name']
        docker_image    = python_docker_methods.remove_docker_image(self.docker_client, image_name)
        return {"Removed Image" : str(docker_image)}

##TODO ---- return the container network type, name and used ports, ip
class GetDockerContainerNetwork(Resource):
    def __init__(self, **kwargs):
        self.docker_client = kwargs['docker_client']
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
        self.docker_client = kwargs['docker_client']
    def get(self):
        return ''
    def post(self):
        return ''