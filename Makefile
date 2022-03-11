#!/usr/bin/make
all: buildout

IMAGE_NAME=smartweb/directory:latest

buildout.cfg:
	ln -fs dev.cfg buildout.cfg

bin/buildout: bin/pip buildout.cfg
	bin/pip install -I -r requirements.txt

buildout: bin/instance

bin/instance: bin/buildout
	bin/buildout

bin/pip:
	python3 -m venv .

run: bin/instance
	bin/instance fg

cleanall:
	rm -fr develop-eggs downloads eggs parts .installed.cfg lib lib64 include bin .mr.developer.cfg local/ share/

upgrade-steps:
	bin/instance -O plone run scripts/run_portal_upgrades.py

docker-image: eggs  ## Build docker image
	docker build --pull --no-cache -t $(IMAGE_NAME) .

test-image:
	echo "test to do"

lint:
	pre-commit run --all
