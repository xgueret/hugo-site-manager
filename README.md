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



## How to install the latest version of Hugo on Ubuntu

Visit the [Hugo releases page](https://github.com/gohugoio/hugo/releases) on GitHub to get the download link for the latest version.

Once on the page, find the link to download the binary for your architecture (`hugo_extended_X.X.X_Linux-64bit.tar.gz`).

**Download the latest version using `wget`:**

```shell
wget https://github.com/gohugoio/hugo/releases/download/v0.124.0/hugo_extended_0.124.0_Linux-64bit.tar.gz
```

<u>:sunglasses: ​Replace `0.124.0` with the version you want to install if a newer one is available.</u>

**Extract the downloaded file:**

```shell
tar -xzf hugo_extended_0.124.0_Linux-64bit.tar.gz
```

**Move the `hugo` binary to a globally accessible directory like `/usr/local/bin`:**

```shell
sudo mv hugo /usr/local/bin/
```

**To verify that Hugo is correctly installed and globally accessible, run:**

```shell
hugo version
```



## :facepunch: Contribution

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. **Fork the repository** to your own GitHub account.
2. **Clone your fork** locally:

```shell
git clone https://github.com/yourusername/hugo-site-manager.git
cd manage-repo
```

**Create a new branch** for your feature or bug fix:

```shell
git checkout -b my-new-feature
```

**Make your changes** and commit them with a clear message:

```shell
git commit -m "Add new feature"
```

**Push your branch** to your fork:

1. ```shell
   git push origin my-new-feature
   ```

2. **Open a Pull Request** on the original repository and describe your changes.

By following these steps, you can help improve the project for everyone!

