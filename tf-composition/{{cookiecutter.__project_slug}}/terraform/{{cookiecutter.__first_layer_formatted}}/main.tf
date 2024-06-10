# Modules declared in this files must have source from github or terraform registry
# To work with local modules instead, use the _override.tf file and uncomment it in the .gitignore file

# Example
# Create local file
resource "local_file" "this" {
  content  = var.content
  filename = local.filename
}

# Add Resources to create here
