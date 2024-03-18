# Stop the script if any command returns an error
$ErrorActionPreference = "Stop"

# Install the Python module in development mode
pip install -e .
pip install .[ci]

# Initialize the repository
git init
git branch -M main
git add .
git commit -m "feat!: :tada: cookiecutter scaffold"

pre-commit install
