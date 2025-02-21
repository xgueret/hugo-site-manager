
# 🚀 Hugo Site Manager

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Hugo](https://img.shields.io/badge/Hugo-Static%20Site%20Generator-orange?logo=hugo)

Ce projet fournit un script Python pour automatiser la création, la configuration et la gestion de sites Hugo. Il utilise des fichiers de configuration pour personnaliser la création de sites et l'installation de thèmes.

## Fonctionnalités

- Crée un nouveau site Hugo dans un répertoire spécifié.
- Initialise un dépôt Git pour le site.
- Ajoute un thème Hugo spécifié comme sous-module Git.
- Configure le site pour utiliser le thème spécifié.
- Démarre le serveur Hugo pour prévisualiser le site.
- Supprime un site existant.
- Copie le contenu d'un exemple de site à partir du thème.

## Prérequis

- [Python 3.x](https://www.python.org/downloads/)
- [Hugo](https://gohugo.io/getting-started/installing/)
- [Git](https://git-scm.com/)

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/votre-utilisateur/hugo-site-manager.git
   cd hugo-site-manager
   ```
2. Créez un environnement virtuel et activez-le :

   ```shell
   python3 -m venv hugo-site-manager-env
   source hugo-site-manager-env/bin/activate
   ```
3. Installez les dépendances :

   ```shell
   pip install -r requirements.txt
   ```

## Utilisation

### Préparer les Fichiers de Configuration

Créez un fichier de configuration dans le répertoire `configs`.

Chaque fichier doit suivre la convention de nommage `config-<nom-config>.env`.

Exemple :

```properties
# configs/config-quickstart.env
SITE_NAME="mon-site"
THEME_REPO="https://github.com/theNewDynamic/gohugo-theme-ananke.git"
THEME_NAME="ananke"
```

### Exécuter le Script

Le script prend deux arguments principaux : une action et un nom de configuration. Voici les actions disponibles :

- **Créer un site** :

  ```bash
  python main.py create quickstart --run
  ```

  L'option `--run` démarre le serveur Hugo après la création du site.
- **Démarrer le serveur** :

  ```shell
  python main.py run quickstart
  ```
- **Supprimer un site** :

  ```bash
  python main.py delete quickstart
  ```
- **Copier le contenu de l'exemple de site** :

  ```shell
  python main.py copy-example-site quickstart
  ```

### Afficher l'Aide

Pour afficher l'aide et les options disponibles :

```shell
python main.py --help
```

Pour consulter la documentation des classes et méthodes, utilisez la fonction `help()` de Python :

```shell
from hugo_site_manager.core import HugoManager
help(HugoManager)
```

## Contribution

Les contributions sont les bienvenues ! Pour contribuer, suivez ces étapes :

1. **Forker le dépôt** sur votre compte GitHub.
2. **Cloner votre fork** localement :

   ```bash
   git clone https://github.com/votre-utilisateur/hugo-site-manager.git
   cd hugo-site-manager
   ```
3. **Créer une nouvelle branche** pour votre fonctionnalité ou correctif :

   ```bash
   git checkout -b ma-nouvelle-fonctionnalite
   ```
4. **Faire vos modifications** et les committer avec un message clair :

   ```bash
   git commit -m "Ajouter une nouvelle fonctionnalité"
   ```
5. **Pousser votre branche** vers votre fork :

   ```bash
   git push origin ma-nouvelle-fonctionnalite
   ```
6. **Ouvrir une Pull Request** sur le dépôt original et décrire vos modifications.
