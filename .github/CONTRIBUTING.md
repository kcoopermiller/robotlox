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

VSCode:

1. In VSCode, run the `Remote-Container: Open Folder in Container` command.
2. Open the folder that contains this Git repo
3. For the container configuration, choose `From 'Dockerfile'`

CLI:

1. Open terminal, navigate to the Git directory, and build the container using the `docker build -t [image title]` command
2. Start the container using the `docker run -dp 3000:3000 [image title]` command

# Getting Started with Roblox Development

## [Rojo](https://rojo.space/)

VSCode:
Install the [Rojo](https://marketplace.visualstudio.com/items?itemName=evaera.vscode-rojo) VSCode Extension

CLI:
Check out Rojo's [documentation](https://rojo.space/docs/v6/getting-started/installation/)

## Live-Syncing into Roblox Studio​

todo
