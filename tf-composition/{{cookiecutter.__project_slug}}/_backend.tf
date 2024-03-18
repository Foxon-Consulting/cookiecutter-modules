# Exemple to test with local tfstate
# For dev env:
# terraform {
#   backend "local" {
#     path = "./env/dev/terraform.tfstate"
#     workspace_dir = "./env/dev"
#   }
# }

terraform {
  backend "s3" {}
}
