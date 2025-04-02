# Front
## Application Météo
Front d'une application Météo avec l'API weatherapi pour afficher la météo de Paris et les prévisions météo des 10 prochains jours

Le front a besoin du back pour fonctionner pour récupérer les informations de l'API.

Nécessite d'installer les modules avant de créer le container avec la commande dans le dossier front

```
npm install
```


Application pouvant être conteneurisé avec Docker en utilisant le Dockerfile avec les commandes

```
docker build -t vue-app .
docker run  -p 8080:8080 -v .:/app vue-app
```

### Structure du projet:
```
front
├── .devcontainer (permet de coder dans le container)
├── Dockerfile
├── src
├── public
├── package.json
└── package-lock.json
```

### Pour coder en local
```
npm install
npm run serve
```

### Ressources
https://v2.vuejs.org/v2/cookbook/dockerize-vuejs-app.html?redirect=true
