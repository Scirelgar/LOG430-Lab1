# LOG430-Lab0

## Description

L'application dans ce dépôt est un simple serveur asynchrone qui écoute sur le port 8000 et renvoie une réponse HTTP 200 OK avec le message "Hello World!" pour chaque requête reçue. Elle utilise le cadriciel de développement web FastAPI.

## Instructions

1. **Installation des dépendances** : Assurez-vous d'avoir Python 3.7 ou une version ultérieure installé sur votre machine. Installez les dépendances requises en exécutant la commande suivante dans le terminal :

    ```bash
    pip install -r requirements.txt
    ```

2. **Lancement du serveur** : Une fois les dépendances installées, vous pouvez démarrer le serveur en exécutant la commande suivante :

    ```bash
    fastapi dev main.py
    ```

3. **Accéder à l'application** : Ouvrez votre navigateur et accédez à l'URL suivante :

    ```bash
    http://localhost:8000
    ```

Vous devriez voir la réponse "Hello World!" s'afficher dans votre navigateur.

Il est aussi possible de faire une requête avec curl :

```bash
curl http://localhost:8000
```

Vous devriez également voir la réponse "Hello World!" s'afficher dans le terminal.

## Structure du projet

```

src
└── pkg
    ├── __init__.py
    └── main.py
tests
├── __init__.py
└── test_main.py
README.md
requirements.txt
```

### src

Le module `src` contient le code source de l'application. Le fichier `main.py` est le point d'entrée de l'application FastAPI.

### tests

Le module `tests` contient les tests unitaires pour l'application. Le fichier `test_main.py` contient des tests pour vérifier le bon fonctionnement de l'application.
