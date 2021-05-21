#!/bin/sh

echo "Installing docker"
sudo pacman -Syu docker
sudo systemctl start docker.service
sudo systemctl enable docker.service

sudo groupadd docker
sudo usernod -aG docker "${USERNAME}"

echo "Successfully installed docker"
./run.sh
