# Env Dash

Envdash is an Infrastructure environment dashboard tool. 

The idea is to give groups in your organisation access to see what environment is on what version of the platform release (if you work via releases).

## Getting started 

### Docker

```
docker build . 
```

### Docker Compose 

```sh
docker-compose build
```

## Features 

### Dashboard

```
https://localhost:8000/
```
![alt text](img/dashboard.png)

### RESTful API 
```
https://localhost:8000/api
```
![alt text](img/api-root.png)
```
https://localhost:8000/api/environments
```
![alt text](img/api-environments.png)

## Contributors

Contributions are always welcome!