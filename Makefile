.PHONY: attach-mongo black build up help
.DEFAULT_GOAL := help

black:  ## Run black formatter
	black app

build:  ## Build a local docker image
	docker-compose -f docker-compose.yml build

up: black build  ## Run a local development
	docker-compose -f docker-compose.yml up

help:  ## Print usage information
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort
