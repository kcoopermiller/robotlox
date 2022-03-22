# Getting Started

## Virtual Environment

### Installing Docker

For Windows & MacOS:

- You can install Docker using [Docker Desktop](https://www.docker.com/products/docker-desktop/)

For Linux:

- Follow these [installation instructions](https://docs.docker.com/engine/install/) for your distribution and architecture

### VSCode Extensions (optional)

Download the [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) and the [Remote Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) Extensions

### Create a container

For VSCode users:

1. In VSCode, run the `Remote-Container: Open Folder in Container` command.
2. Open the folder that contains this Git repo
3. For the container configuration, choose `From 'Dockerfile'`

For everyone else:

1. Open terminal navigate to the Git directory, and building the container using the `docker build -t [image title]` command
2. Start the container using the `docker run -dp 3000:3000 [image title]` command
