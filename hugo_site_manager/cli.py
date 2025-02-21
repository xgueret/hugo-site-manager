import argparse
from .core import HugoManager

def main():
    """
    Point d'entrée principal pour l'interface en ligne de commande (CLI) de Hugo Site Manager.

    Ce script permet de gérer des sites Hugo en utilisant des actions telles que :
    - Créer un nouveau site.
    - Démarrer un serveur Hugo.
    - Supprimer un site existant.
    - Copier le contenu d'un exemple de site.

    Utilisation :
        python main.py <action> <config-name> [options]

    Exemples :
        python main.py create quickstart --run
        python main.py run quickstart
        python main.py delete quickstart
        python main.py copy-example-site quickstart
    """
    parser = argparse.ArgumentParser(
        description="Gère la création, la suppression, l'exécution et la configuration de sites Hugo."
    )
    parser.add_argument(
        "action",
        choices=["create", "delete", "run", "copy-example-site"],
        help="Action à effectuer : créer, supprimer, exécuter ou copier un exemple de site."
    )
    parser.add_argument(
        "config_name",
        help="Nom du fichier de configuration (sans 'config-' et '.env')."
    )
    parser.add_argument(
        "--run",
        action="store_true",
        help="Démarre le serveur Hugo après la création du site (uniquement pour l'action 'create')."
    )

    # Analyse les arguments de la ligne de commande
    args = parser.parse_args()

    # Initialiser HugoManager avec la configuration spécifiée
    manager = HugoManager(args.config_name)

    # Exécuter l'action demandée
    if args.action == "create":
        manager.create_site(run_server=args.run)
    elif args.action == "run":
        manager.run_server()
    elif args.action == "delete":
        manager.delete_site()
    elif args.action == "copy-example-site":
        manager.copy_example_site()

if __name__ == "__main__":
    main()
