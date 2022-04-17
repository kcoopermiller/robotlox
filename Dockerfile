# create a layer from the Alpine Linux Docker image
FROM alpine:latest

# update & upgrade Alpine package manager
RUN apk update
RUN apk upgrade 

# install Rust & Cargo
RUN apk add --no-cache rust cargo

# install zsh
RUN apk add --no-cache zsh

ENTRYPOINT zsh