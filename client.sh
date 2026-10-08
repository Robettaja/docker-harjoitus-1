#!/bin/bash

docker build -t docker1-client client/ 
docker volume create clientvol 
docker run -d --name client --network docker1-network --volume "clientvol:/clientdata" docker1-client http://server:8001
docker logs -f client 
