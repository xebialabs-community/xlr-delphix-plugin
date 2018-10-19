#!/usr/bin/env bash
set -ev

docker run --rm -d -p 28080:8080 --name delphix xebialabsunsupported/xl-docker-demo-delphix:latest
./gradlew compileDocker
docker stop delphix
