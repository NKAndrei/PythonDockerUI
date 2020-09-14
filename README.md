# PythonDockerUI
Web UI created with Python, Flask and docker SDK

The purpose of this project is to control the docker containers of a host through a web ui.
Technologies used:
 - python
 - flask
 - docker sdk
 - javascript
 - jinja templates

The project is divided into modules each with a specific task:
 - main_flask module is the entry point of the project.
 - resource module is used to create the api calls that are used to get, send and execute all commands related to docker through javascript calls.
 - parser is used to extract specific values and elements from a container such as name, id, networks and so on to be used and represented inside the ui.
 - python_docker_methods is used to contain all the methods used with docker sdk.
 - python_docker_commandline_tests is only used for testing purposes
