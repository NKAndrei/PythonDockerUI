from flask import Flask, redirect, request, render_template
from flask_restful import Resource, Api
from python_docker_methods import getDockerClient, listDockerImages
from resources import CreateContainer, GetAllContainers, StopContainer, RemoveContainer, StartContainer, GetContainerProcesses, GetContainerLogs, GetContainerStats, RestartContainer, GetDockerContainerProcessStatus

app = Flask(__name__)
api = Api(app)

## ---- innitiate the docker client
dockerClient = getDockerClient()
hello = 'hello world'

@app.route('/home')
def home():
    image = listDockerImages(dockerClient)
    return render_template('home.html', world=image)

api.add_resource(CreateContainer, '/createContainer', resource_class_kwargs={'dockerClient' : dockerClient})
api.add_resource(StopContainer, '/stopContainer', resource_class_kwargs={'dockerClient' : dockerClient})
api.add_resource(StartContainer, '/startContainer', resource_class_kwargs={'dockerClient' : dockerClient})
api.add_resource(RemoveContainer, '/removeContainer', resource_class_kwargs={'dockerClient' : dockerClient})
api.add_resource(RestartContainer, '/restartContainer', resource_class_kwargs={'dockerClient' : dockerClient})
api.add_resource(GetAllContainers, '/getAllContainers', resource_class_kwargs={'dockerClient' : dockerClient})
api.add_resource(GetContainerProcesses, '/getContainerProcesses', resource_class_kwargs={'dockerClient' : dockerClient})
api.add_resource(GetContainerLogs, '/getContainerLogs', resource_class_kwargs={'dockerClient' : dockerClient})
api.add_resource(GetContainerStats, '/getContainerStats', resource_class_kwargs={'dockerClient' : dockerClient})
api.add_resource(GetDockerContainerProcessStatus, '/getProcessStatus', resource_class_kwargs={'dockerClient' : dockerClient})




if __name__ == '__main__':
    app.run(debug=True)