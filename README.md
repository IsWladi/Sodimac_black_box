# Sodimac Black Box

## Cómo levantar el ambiente de Jenkins y probar el pipeline

### 1: Levantar Jenkins de manera local
    - Tener instalado Docker Desktop o en su defecto Docker engine
    - Tener abierto Docker Desktop para que el demonio de docker este activo
    - Ejecutar los siguentes comandos (para mas información revisar la [documentación](https://www.jenkins.io/doc/book/installing/docker/) de Jenkins):
        - `docker network create jenkins`
        - Levantar contenedor para que Jenkins pueda ejecutar comandos de Docker`docker run --name jenkins-docker --rm --detach --privileged --network jenkins --network-alias docker --env DOCKER_TLS_CERTDIR=/certs --volume jenkins-docker-certs:/certs/client --volume jenkins-data:/var/jenkins_home --publish 2376:2376 docker:dind`
        - Crear Dockerfile con el siguente contenido:
            """
            FROM jenkins/jenkins:2.414.3-jdk17
            USER root
            RUN apt-get update && apt-get install -y lsb-release
            RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
            https://download.docker.com/linux/debian/gpg
            RUN echo "deb [arch=$(dpkg --print-architecture) \
            signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
            https://download.docker.com/linux/debian \
            $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
            RUN apt-get update && apt-get install -y docker-ce-cli
            USER jenkins
            RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"
            """
        - Crear imagen a partir del Dockerfile(ejecutar comando en la misma ruta del Dockerfile): `docker build -t myjenkins-blueocean:2.414.3-1 .`
        - Levantar contenedor de jenkins con el comando: `docker run --name jenkins-blueocean --restart=on-failure --detach --network jenkins --env DOCKER_HOST=tcp://docker:2376 --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 --volume jenkins-data:/var/jenkins_home --volume jenkins-docker-certs:/certs/client:ro --publish 8080:8080 --publish 50000:50000 myjenkins-blueocean:2.414.3-1`
        - Abrir en el navegador la url `http://localhost:8080/` y seguir los pasos de instalación de Jenkins(En los logs del contenedor de jenkins esta la contraseña de administrador)

### 2: Configurar Jenkins y ejecutar el pipeline
    - Instalar los plugins recomendados por Jenkins
    - Crear una nueva tarea de tipo pipeline con el nombre que desee
    - En la sección de pipeline seleccionar la opción de `pipeline script from SCM`
    - En la sección de SCM seleccionar la opción de `Git`
    - En la sección de `Repository URL` ingresar la url: `https://github.com/IsWladi/Sodimac_black_box.git`
    - En la sección de `Branch Specifier (blank for 'any')`: poner `*/main`
    - En la sección de `Script Path`: poner `Jenkinsfile`
    - Dar click en `Apply` y luego en `Guardar`
    - Dar click en `Build Now` para ejecutar el pipeline
