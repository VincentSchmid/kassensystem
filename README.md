# Kassensystem

Point of Sales system.

## Setup
The docker-compose file sets up the backend and the frontend.  
Frontend development can be done using the frontend container.  
Hotreloading works with the frontend deployed in docker.  
This allows for any edits in the code to instantly be visible in the deployed frontend docker container.

### Docker-compose
By running:  

```bash
docker-compose up
```
The frontend and backend are deployed and connected.  

By running:  

```bash
docker-compose up --build
```
a rebuild of the images can be forced.

### Access

the frontend will be reachable on:

```
localhost:3000
```

and the backend on:

```bash
localhost:8081
```


