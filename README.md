# LOG430-Lab0

## Description

L'application dans ce dépôt est un simple serveur asynchrone qui écoute sur le port 8000 et renvoie une réponse HTTP 200 OK avec le message "Hello World!" pour chaque requête reçue. Elle utilise le cadriciel de développement web FastAPI.

## Installation et exécution

### Local

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

### Docker

Le projet contient un ficher `compose.yaml` qui permet de lancer l'application dans un conteneur Docker. Pour ce faire, il ne suffit que de lancer la commande suivante :

```bash
docker compose up
```

Cela va construire l'image Docker et démarrer le conteneur. Une fois le conteneur en cours d'exécution, vous pouvez accéder à l'application de la même manière que ci-dessus, en ouvrant votre navigateur à l'URL suivante :

```bash
http://localhost:8000
```

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

## CI/CD

Le projet utilise des GitHub Actions pour la CI/CD. Trois workflows sont configurés :

| Workflow | Description | Triggers |
| --- | --- | --- |
| `black_formatting.yml` | Vérifie le formatage du code avec Black | `push`, `pull_request` |
| `docker_publish.yml` | Construit l'image Docker et la pousse sur Docker Hub | `push` sur la branche `master` |
| `unit_test.yml` | Exécute les tests unitaires | `pull_request` |
