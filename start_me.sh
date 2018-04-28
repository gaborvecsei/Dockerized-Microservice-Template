#!/bin/bash

# Creates persistent DB folder for Postgres
DB_DIRECTORY=db_data
if ! [ -d "$DB_DIRECTORY" ]; then
    mkdir "$DB_DIRECTORY"
    echo "Folder created for db service: $DB_DIRECTORY"
fi

# Created the DB service
docker-compose up -d db
echo "Waiting for the db service to start"

# We need to wait for the service to start
sleep 3

# Start everything else
echo "DB is up, starting other containers"
docker-compose up -d
