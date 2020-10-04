from python_docker_methods import terminal_commands, get_docker_client,list_docker_images, run_docker_container, list_docker_containers, stop_docker_container, get_docker_container, execute_command_in_container, remove_docker_container, get_docker_processes, pull_docker_image, remove_docker_image
import re
import time
import pprint

def tests1():
    pp = pprint.PrettyPrinter(indent=4)
    ## ---- random terminal commands for testing purposes
    terminal_commands()

    ## ---- pull and list the downloaded docker image##TODO ---- need to define the following methods

    docker_client = get_docker_client()
    pull_docker_image(docker_client, "httpd")
    dockerImages = list_docker_images(docker_client)
    print("printing images")
    print(dockerImages)

    ## ---- get docker image name and spin up a container
    dockerImageStr = str(dockerImages)
    string = re.search('\'(.+?)\'',dockerImageStr)
    trimmedString = string.group().replace("'", "")
    print(trimmedString)
    print("BELOW IS CONTAINER LOG")
    command = "bash -c 'for i in {1..100}; sleep 2s; done'"
    ##containerLog = run_docker_container(docker_client, trimmedString, command)
    containerLog = run_docker_container(docker_client, trimmedString, True)
    print(containerLog)
    print("ABOVE IS CONTAINER LOG")
    time.sleep(5)

    ## ---- get the container list and connect to a container
    container_list = list_docker_containers(docker_client)
    print("TRIMMING THE LIST")
    print(str(container_list))
    trimmedContainerList = re.search(': (.+?)>', str(container_list)).group().replace(":","").replace(">","").replace(" ","")
    print(trimmedContainerList)
    print("TRIMMING THE LIST")

    container_connection = get_docker_container(docker_client, trimmedContainerList)
    time.sleep(5)
    print("EXECUTING A COMMAND")
    cmd = '/bin/sh -c "echo hello stdout ; echo hello stderr >&2"'
    print(execute_command_in_container(container_connection, cmd))
    print("EXECUTING A COMMAND")

    print("PRINTING CONTAINER ATTRIBUTES")
    container_connection.reload()
    print('Configuration ' + container_connection.attrs['Config']['Image'])
    print('ID ' + container_connection.attrs['Id'])
    print('ID ' + container_connection.attrs['Name'])
    ##pp.pprint(container_connection.attrs)
    print("PRINTING CONTAINER ATTRIBUTES")

    print("PRINTING CONTAINER LOGS")
    ##print(container_connection.logs())
    print("PRINTING CONTAINER LOGS")

    print("EXECUTING COMMAND")
    cmd = '/bin/sh -c "echo hello stdout ; echo hello stderr >&2"'
    containerCommandExecution = execute_command_in_container(container_connection, cmd)
    print(containerCommandExecution)
    print("EXECUTING COMMAND")
    container_processes = get_docker_processes(container_connection)
    print("RUNNING PROCESSES ARE")
    print(container_processes)
    ## ---- stop, remove and check if the docker container has been removed
    stopContainer = stop_docker_container(container_connection)
    removeContainer = remove_docker_container(container_connection)
    list_docker_containers(docker_client)
    ##print(stopContainer)
tests1()