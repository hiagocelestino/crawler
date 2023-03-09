#!/bin/env bash

LOCAL_PORT=${LOCAL_PORT:-5000}
LOCAL_DIR="$PWD"
CONTAINER_NAME="crawlerbackend"

docker build -t crawlerbackend:latest .

launch_container() {
  docker run -it \
      --name="$CONTAINER_NAME" \
      -p "$LOCAL_PORT":5000 \
      -v "$LOCAL_DIR":/app \
      crawlerbackend:latest
}

EXISTING_CONTAINER_ID=$(docker ps -a -q -f name="$CONTAINER_NAME")

if [ -z "$EXISTING_CONTAINER_ID" ]
then
  launch_container
else
  docker container rm "$CONTAINER_NAME"
  launch_container
fi


