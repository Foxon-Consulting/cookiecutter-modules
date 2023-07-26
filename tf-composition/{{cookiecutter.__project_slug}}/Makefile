.PHONY: init plan apply destroy
.ONESHELL:
.SHELL := /bin/ash

# Check necessary tools
ifeq (, $(shell which aws))
	$(error "No aws in $(PATH), consider installing awscli")
endif
ifeq (, $(shell which terraform))
	$(error "No terraform in $(PATH), consider installing terraform")
endif

check-env:
ifndef ENV
	$(error ENV is undefined)
endif

init: check-env
	@echo "Initializing terraform"
	terraform init -backend-config="./env/$(ENV)/config.tfbackend" -reconfigure

plan: check-env
	@echo "Planning terraform"
	terraform plan -var-file="./env/$(ENV)/vars.tfvars"

apply: check-env
	@echo "Applying terraform"
	terraform apply -var-file="./env/$(ENV)/vars.tfvars"

destroy: check-env
	@echo "Destroying terraform"
	terraform destroy -var-file="./env/$(ENV)/vars.tfvars"
