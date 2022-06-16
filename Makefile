.PHONY: attach-mongo black build up help
.DEFAULT_GOAL := help

black:  ## Run black formatter
	black main.py

build:  ## Build a local docker image
	docker build -t hoanhan/dani:latest .

up: black build  ## Run a local development
	docker-compose -f docker-compose.yml up

push: black build  ## Push to github, dockerhub and digitalocean
	git push origin master && docker push hoanhan/dani && sleep 60 && doctl apps create-deployment ${DEPLOYMENT_ID} --force-rebuild

help:  ## Print usage information
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort
