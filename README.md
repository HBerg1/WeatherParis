## Application Météo de Paris

Une application Météo avec l'API weatherapi pour afficher la météo de Paris et les prévisions météo des 10 prochains jours avec un front en Vue.js, un back en Flask et l'utilisation de Redis comme cache.

### Structure du projet

```
.
├──compose.yaml
├──front
    ├── Dockerfile
    └── app.py
└── back
  └── app
     └──  Dockerfile


```

[_compose.yaml_](compose.yaml)

```
services:
  redis:
    image: redislabs/redismod
    ports:
      - '6379:6379'
  flask-app: 
    build:
      context: ./back/app
      target: builder
    stop_signal: SIGINT
    ports:
      - '8000:8000'
    environment:
      - FLASK_ENV=development
      - FLASK_APP=app.py  
    volumes:
      - ./back/app:/app
    command: flask run --host=0.0.0.0 --port 8000 --debug
  vue-app:
    build: ./front
    working_dir: /app
    volumes:
      - ./front:/app
    depends_on:
      - flask-app
    ports:
      - "8080:8080"
    command: npm run serve
```

## Deploy with docker compose

```
$ docker compose up -d                                                                                                                                                                                            0.0s
[+] Running 4/4
 ✔ Network project_default        Created                                                                                                                                                                                                                          0.0s 
 ✔ Container project-flask-app-1  Created                                                                                                                                                                                                                          0.2s 
 ✔ Container project-redis-1      Created                                                                                                                                                                                                                          0.2s 
 ✔ Container project-vue-app-1    Created  
```

## Résultat attendu
Liste des containers qui doivent être affichés avec leur port mappé:
```
$ docker ps
CONTAINER ID   IMAGE                COMMAND                     STATUS          PORTS                    NAMES
7e3ee768b7b7   project-vue-app      "docker-entrypoint.s…"      Up 47 seconds   0.0.0.0:8080->8080/tcp   project-vue-app-1
d511ff0c9ff4   redislabs/redismod   "redis-server --load…"      Up 48 seconds   0.0.0.0:6379->6379/tcp   project-redis-1
10336816c473   project-flask-app    "flask run --host=0.…"      Up 48 seconds   0.0.0.0:8000->8000/tcp   project-flask-app-1

```

L'application peut être accéder avec `http://localhost:8080` pour le front en vue.js et `http://localhost:8000` pour l'application flask

```
$ curl localhost:8000
Hello World!
```

Stop and remove the containers
Pour arrêter et retirer les containers
```
$ docker compose down
```