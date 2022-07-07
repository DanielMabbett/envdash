# Envdash

[![Django CI](https://github.com/DanielMabbett/envdash/actions/workflows/django.yml/badge.svg)](https://github.com/DanielMabbett/envdash/actions/workflows/django.yml)
[![Docker Image CI](https://github.com/DanielMabbett/envdash/actions/workflows/docker-image.yml/badge.svg)](https://github.com/DanielMabbett/envdash/actions/workflows/docker-image.yml)

![alt text](img/banner.png)

Envdash is an Infrastructure environment dashboard tool. 

The idea is to give groups in your organisation access to see what environment is on what version of the platform release (if you work via releases).

Its lightweight, based on REST commands, so can easily fit into almost any workflow (examples coming).

Quick example (using admin/admin for username/password): 
```bash
curl --location --request POST 'http://127.0.0.1:8000/api/environments/' \
--header 'Authorization: Basic YWRtaW46YWRtaW4=' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=3puWbsMc3aUwzqmmoZ6B25d5LqAwwxyC177x3oOfBM0LHwyFcjij7AAIAaU3vDR3' \
--data-raw '{
    "title": "Production001",
    "group": "myInternalGroupName",
    "location": "AzureNorthEurope",
    "description": "This is the main production environment for our company",
    "version": "1.0.2"
}'
```

Response:
```json
{
    "url": "http://127.0.0.1:8000/api/environments/1/",
    "id": 1,
    "title": "Production001",
    "group": "myInternalGroupName",
    "location": "AzureNorthEurope",
    "description": "This is the main production environment for our company",
    "highlight": "http://127.0.0.1:8000/api/environments/1/highlight/",
    "owner": "admin",
    "version": "1.0.2"
}
```

## Getting started 

### Docker

```sh
docker build . 
```

### Docker Compose 

Build easily with:
```sh
docker-compose build
```

Then run up to start
```sh
docker-compose up
```

### Creating admin user

NOTE: This will improve over time
You will need to run a terminal session into the pod to create your super user:

```bash
python manage.py createsuperuser
```

## Features 

### Dashboard

There are two dashboards (with more improvements coming!)...

One for Environments Overview, and one for Clusters Overview

Environments:
```
https://localhost:8000/
```
![alt text](img/overview.png)

Clusters:
```
https://localhost:8000/clusters/
```

### RESTful API 

root
```
https://localhost:8000/api
```
![alt text](img/api-root.png)

environments
```
https://localhost:8000/api/environments
```
![alt text](img/api-environments.png)

clusters
```
https://localhost:8000/api/environments
```

users
```
https://localhost:8000/api/users
```

## Contributors

Contributions are always welcome!
