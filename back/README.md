# Back
## Application Météo
Back d'une application Météo qui utilise l'API weatherapi pour récupérer la météo de Paris et les prévisions météo des 10 prochains jours. 

Les informations (avec Redis) pour éviter de faire plusieurs appels sur l'API

Nécessite d'être lancé depuis le compose.yml dans le dossier racine

### Structure du projet

```
.
└── back
  └── app
     ├── Dockerfile
     ├── requirements.txt
     └── app.py

```

### Ressources
https://github.com/docker/awesome-compose/tree/master/flask-redis