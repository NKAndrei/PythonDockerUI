from flask import Flask, redirect, request, render_template
from flask_restful import Resource, Api
from flask_cors import CORS
from python_docker_methods import get_docker_client, list_docker_images
from resources import CreateContainer, GetAllContainers, StopContainer, RemoveContainer, StartContainer, GetContainerProcesses, GetContainerLogs, GetContainerStats, RestartContainer, GetDockerContainerProcessStatus



app = Flask(__name__)
CORS(app)
api = Api(app)



## ---- innitiate the docker client
docker_client = get_docker_client()


@app.route('/')
def redirect_home():
    return redirect('/home',302)
@app.route('/home')
def home():
    image = list_docker_images(docker_client)
    return render_template('home.html', world=image)



api.add_resource(CreateContainer, '/createContainer', resource_class_kwargs={'docker_client' : docker_client})
api.add_resource(StopContainer, '/stopContainer', resource_class_kwargs={'docker_client' : docker_client})
api.add_resource(StartContainer, '/startContainer', resource_class_kwargs={'docker_client' : docker_client})
api.add_resource(RemoveContainer, '/removeContainer', resource_class_kwargs={'docker_client' : docker_client})
api.add_resource(RestartContainer, '/restartContainer', resource_class_kwargs={'docker_client' : docker_client})
api.add_resource(GetAllContainers, '/getAllContainers', resource_class_kwargs={'docker_client' : docker_client})
api.add_resource(GetContainerProcesses, '/getContainerProcesses', resource_class_kwargs={'docker_client' : docker_client})
api.add_resource(GetContainerLogs, '/getContainerLogs', resource_class_kwargs={'docker_client' : docker_client})
api.add_resource(GetContainerStats, '/getContainerStats', resource_class_kwargs={'docker_client' : docker_client})
api.add_resource(GetDockerContainerProcessStatus, '/getProcessStatus', resource_class_kwargs={'docker_client' : docker_client})



if __name__ == '__main__':
    app.run(debug=True)