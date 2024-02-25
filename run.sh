#!/bin/bash

OPTION=$1

usage(){
	echo -e "Usage: './run <arg>'"
	echo -e "\t<arg>: one of 'build_app'o or 'tests'"
    echo -e "buid_app: builds the api and db containers and launches the api"
    echo -e "tests: runs the unit test suite"
}

build_app(){
    docker-compose up -d --build && \
    docker-compose exec api python manage.py migrate
}

tests() {
    docker-compose exec api pytest "$@"
}

nuke() {
    docker-compose down -v
}

if [[ "$1" == "" ]]; then
	usage
	exit 1
fi

"$@"
