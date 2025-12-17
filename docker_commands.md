# Docker Commands

Fill in the Docker commands you used to complete the test.

## Volume

### Create the volume

```bash
docker volume create fastapi-db
```

### Seed the volume (via Docker Desktop)

```bash

```

## Server 1

### Build the image

```bash
docker build -t shopping-server1:v1 .
```

### Run the container

```bash
docker run -it --rm -p 8000:8000 -v fastapi-db:/app/db shopping-server1:v1
```

## Server 2

### Build the image

```bash
docker build -t shopping-server2:v1 .
```

### Run the container

```bash
docker run -it --rm -p 8000:8000 -v fastapi-db:/app/db shopping-server2:v1
```


#### after bonus
```bash
docker run -it --rm -p 8000:8000 -v fastapi-db:/app/db  -v ./data:/app/data shopping-server2:v1
```

