#!/bin/bash

# Function to display help message
function show_help {
  echo "Usage: $0 <action> <config-name> [options]"
  echo
  echo "Actions:"
  echo "  create               Create a new Hugo site using the specified configuration."
  echo "  delete               Delete an existing Hugo site based on the specified configuration."
  echo "  run                  Start the Hugo server for an existing site."
  echo "  copy-example-site    Copy example site content from theme to site."
  echo
  echo "Options for 'create':"
  echo "  --run                Create and immediately start the Hugo server."
  echo "  --no-run             Create the site without starting the server (default)."
  echo
  echo "Arguments:"
  echo "  <action>             The action to perform: 'create', 'delete', 'run', or 'copy-example-site'."
  echo "  <config-name>        The name of the configuration file (without 'config-' and '.env')."
  echo
  echo "Example:"
  echo "  $0 create quickstart --run          # Creates a new site and starts the Hugo server"
  echo "  $0 create quickstart                # Creates a new site without starting the server"
  echo "  $0 run quickstart                   # Starts the Hugo server for an existing site"
  echo "  $0 delete quickstart                # Deletes the site named 'quickstart' from the showcase directory"
  echo "  $0 copy-example-site quickstart     # Copies example site content to the 'quickstart' site"
}

# Function to create a new Hugo site
function create_site {
  # Create the showcase directory if it does not exist
  if [ ! -d "$SHOWCASE_DIR" ]; then
    echo "Directory '$SHOWCASE_DIR' does not exist. Creating directory..."
    mkdir "$SHOWCASE_DIR"
  fi

  # Check if the site already exists in the showcase directory
  if [ -d "$SITE_PATH" ]; then
    echo "Error: Site '$SITE_NAME' already exists in the '$SHOWCASE_DIR' directory. No action taken."
    exit 0
  fi

  # Create a new Hugo site in the showcase directory
  hugo new site "$SITE_PATH"

  # Navigate to the site directory
  cd "$SITE_PATH" || exit

  # Initialize a new Git repository
  git init

  # Add the theme as a Git submodule
  git submodule add "$THEME_REPO" "themes/$THEME_NAME"

  # Add the theme configuration to the hugo.toml file
  echo "theme = '$THEME_NAME'" >> hugo.toml

  # Check options and run Hugo server if specified
  if [[ "$OPTIONS" == *"--run"* ]]; then
    echo "Creating site '$SITE_NAME' and starting the Hugo server..."
    hugo server
  else
    echo "Site '$SITE_NAME' created. Use '$0 run $CONFIG_NAME' to start the server."
  fi
}

# Function to start the Hugo server
function run_server {
  # Check if the site directory exists
  if [ ! -d "$SITE_PATH" ]; then
    echo "Error: Site '$SITE_NAME' does not exist in the '$SHOWCASE_DIR' directory."
    exit 1
  fi

  # Navigate to the site directory and start the Hugo server
  cd "$SITE_PATH" || exit
  echo "Starting the Hugo server for site '$SITE_NAME'..."
  hugo server
}

# Function to delete a Hugo site
function delete_site {
  # Check if the site directory exists
  if [ ! -d "$SITE_PATH" ]; then
    echo "Error: Site '$SITE_NAME' does not exist in the '$SHOWCASE_DIR' directory."
    exit 1
  fi

  # Remove the site directory and its contents
  echo "Deleting site '$SITE_NAME' from '$SHOWCASE_DIR'..."
  rm -rf "$SITE_PATH"
}

# Function to copy example site content
function copy_example_site {
  # Define the path to the example site directory and the destination directory
  EXAMPLE_SITE_DIR="showcase/$THEME_NAME/themes/$THEME_NAME/exampleSite"
  DESTINATION_DIR="$SITE_PATH"

  # Check if the example site directory exists
  if [ ! -d "$EXAMPLE_SITE_DIR" ]; then
    echo "Error: Example site directory '$EXAMPLE_SITE_DIR' does not exist."
    exit 1
  fi

  # Check if the destination directory exists
  if [ ! -d "$DESTINATION_DIR" ]; then
    echo "Error: Destination directory '$DESTINATION_DIR' does not exist."
    exit 1
  fi

  # Copy the example site content to the destination directory
  echo "Copying example site content from '$EXAMPLE_SITE_DIR' to '$DESTINATION_DIR'..."
  cp -R "$EXAMPLE_SITE_DIR"/* "$DESTINATION_DIR/"

  echo "Example site content copied successfully."
}

# Check if help is requested
if [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
  show_help
  exit 0
fi

# Check if an action and configuration name are provided
if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Error: Missing arguments."
  show_help
  exit 1
fi

ACTION="$1"
CONFIG_NAME="$2"
OPTIONS="${@:3}"  # Capture any additional options

# Define the path to the configuration file
CONFIG_DIR="configs"
CONFIG_FILE="$CONFIG_DIR/config-$CONFIG_NAME.env"

# Check if the configuration file exists
if [ ! -f "$CONFIG_FILE" ]; then
  echo "Error: Configuration file '$CONFIG_FILE' does not exist."
  exit 1
fi

source "$CONFIG_FILE"

# Define the directory where sites will be created
SHOWCASE_DIR="showcase"
# Define the full path for the site
SITE_PATH="$SHOWCASE_DIR/$SITE_NAME"

# Handle actions
case "$ACTION" in
  create)
    create_site
    ;;
  run)
    run_server
    ;;
  delete)
    delete_site
    ;;
  copy-example-site)
    copy_example_site
    ;;
  *)
    echo "Error: Invalid action '$ACTION'. Use 'create', 'delete', 'run', or 'copy-example-site'."
    show_help
    exit 1
    ;;
esac
