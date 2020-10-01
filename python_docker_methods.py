import subprocess
import os
import docker

##TODO ---- refactor or create extra docker methos that are executed through subprocess and os

#! -- a series of commmands defined for testing purposes
def terminal_commands(): 
    print("lala")
    py_command = subprocess.run(["ls", "-al"], stdout=subprocess.PIPE)
    print(py_command.stdout.decode())
    py_command_2 = subprocess.run(["grep", "la"], input=py_command.stdout, stdout=subprocess.PIPE)
    print(py_command_2.stdout.decode())
    print('olla2')

def terminal_docker_commands():
    docker_command_1 = subprocess.run(["docker", "ps"], stdout=subprocess.PIPE)
    print(docker_command_1.stdout.decode())
    docker_command_2 = subprocess.run(["docker", "pull", "hello-world"], stdout=subprocess.PIPE)
    print(docker_command_2.stdout.decode())
    docker_command_3 = subprocess.run(["docker", "images"], stdout=subprocess.PIPE)
    print(docker_command_3.stdout.decode())
    docker_command_4 = subprocess.run(["grep", "latest"], input=docker_command_3.stdout, stdout=subprocess.PIPE)
    print(docker_command_4.stdout.decode())
    print(docker_command_4.stdout)

def other_commands(filename):

    file_name = filename
    py_command = subprocess.run(["cat", file_name], stdout=subprocess.PIPE)
    file_contents = py_command.stdout.decode()
    print(file_contents)
    return "ok"
#! -- a series of commmands defined for testing purposes


##TODO ---- need to refactor the names of the methods to be more intuitive
def get_docker_client():
    docker_client = docker.from_env()
    return docker_client

def pull_docker_image(docker_client, image_name):
    docker_image_name = docker_client.images.pull(image_name, "latest")
    return docker_image_name

def list_docker_images(docker_client):
    image_list = docker_client.images.list(all=True)
    return image_list

def list_docker_containers(docker_client):
    container_list = docker_client.containers.list(all=True)
    return container_list

def get_docker_container_name(container_connection):
    name = container_connection.attrs['Name']
    return name                                           #TODO -- need to implement
    
def run_docker_container(docker_client, docker_image_name, detach_container, commands=None):
    if commands != '':
        container = docker_client.containers.run(docker_image_name, detach=detach_container, command=commands)
        return container
    else:
        container = docker_client.containers.run(docker_image_name, detach=detach_container)
        return container

##TODO ---- the start/stop/remove container methods can be grouped into one with conditionals
def start_docker_container(container_connection):
    return container_connection.start()

def stop_docker_container(container_connection):
    return container_connection.stop()

def remove_docker_container(container_connection):
    return container_connection.remove()

def restart_docker_container(container_connection, time=None):
    if time is None:
        container_restart = container_connection.restart()
    else:
        container_restart = container_connection.restart(time=time)
    return container_restart

def get_docker_container(docker_client, containder_id):
    container_object = docker_client.containers.get(containder_id)
    return container_object

def get_docker_container_info(container_connection):
    container_info = container_connection.attrs
    return container_info

def execute_command_in_container(container_connection, command):
    response = container_connection.exec_run(command, stream=False, demux=False)
    return response.output

def get_docker_processes(container_connection):
    docker_processes = container_connection.top()
    return docker_processes

def get_docker_logs(container_connection):
    docker_logs = container_connection.logs()
    return docker_logs

def get_docker_stats(container_connection, stream=None):
    if stream is None:
        docker_stats = container_connection.stats(stream=False)
    else:
        docker_stats = container_connection.stats(stream = stream)
    return docker_stats
