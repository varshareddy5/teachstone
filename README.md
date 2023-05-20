This repo consists of the code for TeachStone Assignment.

# Build the docker image
```
cd teachstone
docker build -t repo-generator:v1.0 .
```

# run the docker container.
```
docker run -d repo-generator:v1.0 
```

# exec into the container and find the output files
```
docker exec -it <container-id> /bin/bash
ls /tmp
cat /tmp/final-report.txt
```
