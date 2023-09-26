# Stop the script if any command returns an error
$ErrorActionPreference = "Stop"

# Step 1: Create a Python virtual environment

# Initialize the repository
git init
git add .
git commit -m "feat!: :tada: cookiecutter scaffold"

pre-commit install

docker-compose up -d

echo "Please connect vscode and attach it to the container"
