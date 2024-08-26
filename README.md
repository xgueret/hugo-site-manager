# Hugo Site Setup Script

This script automates the process of creating and configuring a new Hugo site. It uses external configuration files to customize site creation and theme setup.

## Features

- Creates a new Hugo site in a specified directory.
- Initializes a Git repository for the site.
- Adds a specified Hugo theme as a Git submodule.
- Configures the site to use the specified theme.
- Optionally starts the Hugo server to preview the site.

## Prerequisites

- [Hugo](https://gohugo.io/getting-started/installing/) installed on your system.
- [Git](https://git-scm.com/) installed on your system.



## Usage

1. **Prepare Configuration Files**

   Create configuration files in the `configs` directory. Each configuration file should follow the naming convention `config-<config-name>.env`, where `<config-name>` is a descriptive name for the configuration. Example:

   ```bash
   # configs/config-quickstart.env
   SITE_NAME="quickstart"
   THEME_REPO="https://github.com/theNewDynamic/gohugo-theme-ananke.git"
   THEME_NAME="ananke"

## Run

**:warning: <u>Take time to fully understand what this script does before running it</u>**

```shell
chmod +x hugo-site-manager.sh
./hugo-site-manager.sh --help
```



## Contributing

:facepunch: Contributions are welcome! Please fork the repository and submit a pull request.

