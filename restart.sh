#!/bin/sh

docker-compose down
sudo rm -rf db/data
docker-compose up -d --force-recreate