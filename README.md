# spotify_wsk

Ce dépôt contient une séquence d'actions à déployer. Les actions sont exécutées à l'aide d'Apache OpenWhisk (OpenWhisk est un framework serverless open source).

## Prérequis
Avant de commencer, assurez-vous d'avoir les éléments suivants :

Apache OpenWhisk installé et configuré sur votre système
Voici les étapes à suivre pour déployer correctement la séquence de traitement :

### 1. Créez les actions en exécutant les commandes suivantes :

./wsk -i action create filterTracks filterTracks.py --kind python:default
./wsk -i action create platformsComparison platformsComparison.py --kind python:default
./wsk -i action create logSpotifyData logSpotifyData.js --kind nodejs:default

### 2. Créer la séquence suivante :

./wsk -i action create spotifySequence --sequence filterTracks,platformsComparison,logSpotifyData

### 3. Test de la séquence suivante :

./wsk -i action invoke spotifySequence --result