#!/bin/bash

docker build -t docker1-server server/ 
docker network create docker1-network
docker volume create servervol
docker run -d --name server --network docker1-network --volume "servervol:/serverdata" docker1-server --port 8001
