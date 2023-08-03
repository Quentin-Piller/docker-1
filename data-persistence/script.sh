#!/bin/bash

# Écrire "bonjour" dans le fichier bonjour.txt
echo "bonjour" > /var/opt/project/bonjour.txt

# Attendre 10 minutes (600 secondes)
sleep 600

# Exécuter une invite de commande bash pour observer le contenu du dossier
docker run -it -v /var/opt/project:/app bash:latest bash
