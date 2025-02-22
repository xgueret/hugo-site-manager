from pathlib import Path
import os
import subprocess
from dotenv import load_dotenv
from colorama import Fore, Style, init

class HugoManager:
    """
    Gère la création, la suppression, l'exécution et la configuration de sites Hugo.

    Cette classe permet de :
    - Créer un nouveau site Hugo avec un thème spécifié.
    - Démarrer un serveur Hugo pour prévisualiser un site.
    - Supprimer un site existant.
    - Copier le contenu d'un exemple de site à partir du thème.

    Attributes:
        config_name (str): Le nom de la configuration (sans 'config-' et '.env').
        config_file (Path): Le chemin du fichier de configuration.
        site_name (str): Le nom du site Hugo, chargé depuis la configuration.
        theme_repo (str): L'URL du dépôt Git du thème, chargé depuis la configuration.
        theme_name (str): Le nom du thème, chargé depuis la configuration.
        showcase_dir (Path): Le répertoire où les sites sont créés (par défaut 'showcase').
        site_path (Path): Le chemin complet du site (showcase_dir / site_name).
    """
    def __init__(self, config_name):
        """
        Initialise une instance de HugoManager.

        Args:
            config_name (str): Le nom de la configuration (sans 'config-' et '.env').
        """
        self.config_name = config_name
        self.config_file = Path(f"configs/config-{config_name}.env")
        self.load_config()
        self.showcase_dir = Path("showcase")
        self.site_path = self.showcase_dir / self.site_name
        # Initialiser colorama
        init()

    def load_config(self):
        """
        Charge les variables de configuration depuis le fichier .env.

        Raises:
            FileNotFoundError: Si le fichier de configuration n'existe pas.
            ValueError: Si une variable de configuration requise est manquante.
        """
        if not self.config_file.exists():
            raise FileNotFoundError(f"Configuration file '{self.config_file}' not found")

        load_dotenv(self.config_file)
        self.site_name = os.getenv("SITE_NAME")
        self.theme_repo = os.getenv("THEME_REPO")
        self.theme_name = os.getenv("THEME_NAME")
        if not all([self.site_name, self.theme_repo, self.theme_name]):
            raise ValueError("Missing required configuration variables.")

    def _ensure_site_exists(self):
        """
        Crée un nouveau site Hugo.

        Args:
            run_server (bool): Si True, démarre le serveur Hugo après la création du site.
        """
        if not self.site_path.exists():
            print(f"{Fore.RED}Error: Site '{self.site_name}' does not exist.{Style.RESET_ALL}")  # Corrigez 'exsist' en 'exist'
            return False
        return True

    def create_site(self, run_server=False):
        """
        Crée un nouveau site Hugo.

        Args:
            run_server (bool): Si True, démarre le serveur Hugo après la création du site.
        """
        print(f"Creating site '{self.site_name}' at '{self.site_path}'...")
        try:
            # Vérifier que le site n'a pas déjà été créé
            if self.site_path.exists():
                raise FileExistsError(f"Site '{self.site_name}' already esists at '{self.site_path}.")

            # Créer un nouveau site Hugo
            subprocess.run(["hugo", "new", "site", str(self.site_path)], check=True)

            # Vérifier que le site a été créé
            if not self.site_path.exists():
                raise FileNotFoundError(f"Site '{self.site_name}' was not created at '{self.site_path}'.")

            print(f"{Fore.GREEN}Site created at '{self.site_path}'.{Style.RESET_ALL}")

            # Stocker le répertoire de travail courant
            original_dir = os.getcwd()

            try:
                # Naviguer vers le répertoire du site
                os.chdir(self.site_path)
                print(f"Changed directory to '{self.site_path}'.")

                # Initialiser un dépôt Git
                print("Initializing Git repository...")
                subprocess.run(["git", "init"], check=True)

                # Ajouter le thème comme sous-module Git
                print(f"Adding theme '{self.theme_name}' from '{self.theme_repo}'...")
                subprocess.run(["git", "submodule", "add", self.theme_repo, f"themes/{self.theme_name}"], check=True)

                # Configurer le thème dans hugo.toml
                with open("hugo.toml", "a", encoding="utf-8") as f:
                    f.write(f'theme = "{self.theme_name}"\n')
    
            finally:
                # Revenir au répertoire de travail original
                os.chdir(original_dir)
                print(f"Changed directory back to '{original_dir}'.")

            # Démarrer le serveur Hugo si l'option --run est spécifiée 
            if run_server:
                print(f"{Fore.GREEN}Starting Hugo server...{Style.RESET_ALL}")
                self.run_server()

        except (FileExistsError, FileNotFoundError) as e:
            print(f"{Fore.RED}Error: Failed to create site '{self.site_name}'. Reason: {e}{Style.RESET_ALL}")

    def run_server(self):
        """Démarre le serveur Hugo"""
        try:
            if not self._ensure_site_exists():
                return

            print(f"Starting Hugo server for site '{self.site_name}' at '{self.site_path}'...")
            os.chdir(self.site_path)
            subprocess.run(["hugo", "server"], check=True)

        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Error: Failed to start Hugo server for site '{self.site_name}'. Reason: {e}{Style.RESET_ALL}")

    def delete_site(self):
        """Supprime un site Hugo"""
        try:
            if not self._ensure_site_exists():
                return
            # pylint: disable=import-outside-toplevel
            import shutil
            # pylint: enable=import-outside-toplevel
            shutil.rmtree(self.site_path)
            print(f"{Fore.GREEN}Site '{self.site_name}' deleted.{Style.RESET_ALL}")
        except shutil.ExecError as e:
            print(f"{Fore.RED}Error: Failed to delete site '{self.site_name}'. Reason: {e}{Style.RESET_ALL}")

    def copy_example_site(self):
        """
        Copie le contenu de l'exemple de site à partir du thème.

        Raises:
            FileNotFoundError: Si le répertoire de l'exemple de site n'existe pas.
        """
        try:
            if not self._ensure_site_exists():
                return

            example_site_dir = self.site_path / "themes" / self.theme_name / "exampleSite"
            if not example_site_dir.exists():
                print(f"{Fore.RED}Error: Example site directory '{example_site_dir}' does not exist.{Style.RESET_ALL}")
                return

            # Copie le cointenu de l'exemple de site
            # pylint: disable=import-outside-toplevel
            import shutil
            # pylint: enable=import-outside-toplevel
            shutil.copytree(example_site_dir, self.site_path, dirs_exist_ok=True)
            print(f"{Fore.GREEN}Example site content copied successfully.{Style.RESET_ALL}")
        except shutil.ExecError as e:
            print(f"{Fore.RED}Error: Failed to copy example site content. Reason: {e}{Style.RESET_ALL}")
