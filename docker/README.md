Docker Architecture
-------------------

Docker is used, both for repeatability and to support
some degree of platform agnosticism.

There are three docker files with slightly different intents.

* *jenkins* - This `Dockerfile` will build a `(project)-jenkins` image. The intent of this 
  image is to provide an environment for creating and publishing
  build artifacts. It should be run as follows: 
  `docker run --rm -it -v $PWD/dist:/tsne/dist -v $PWD/.git:/tsne/.git:ro (project)-jenkins /bin/bash`.
   
   Volume `/tsne/dist` is mounted to allow the container to "unload" build artifacts.
   Volume `/tsne/.git` is mounted to allow the versioning code to run correctly
* *dev* - This `Dockerfile` will build a `(project)-dev` image. The intent of this
  image is to provide a repeatable environment to host an active development loop. (edit, test, repeat). 
  It should be run as follows: `docker run --rm -it -v $PWD:/tsne (project)-dev /bin/bash`.
  
  Volume `/tsne` is mounted to allow for editing the project files either within or outside of
  container.
  
* *prod* - This `Dockerfile` will build a `(project)-prod image`. The intent
  of this image is to provide an environment for installing the a built artifact in
  an environment that we anticipate a consumer of (project) would expect. It should be
  run as follows:  `docker run --rm -it (project)-prod /bin/bash`.
  
  

  
