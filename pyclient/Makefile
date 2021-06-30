
REGISTRY_URL ?= registry.test.pensando.io:5000
PYCLIENT_CONTAINER ?= pyclient:0.2

default:
	mkdir -p bin && mv /opt/openapi-generator-cli.jar bin
	make getswagger
	make genclient

e2e:
	make getswagger
	make build-generator
	make genclient
	make tests

getswagger:
	python3 getswagger.py

genclient:
	bash gen.sh

build-generator:
	cd openapi-generator && mvn clean install -U -DskipTests
	mkdir -p bin
	mv openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar bin/openapi-generator-cli.jar

tests:
	cd utils && python3 test_apps.py

clean:
	find ./apigroups -mindepth 1 ! -regex '^./apigroups/test/.*' -delete

run-container:
	docker run -it -v ~/.psm:/root/.psm -v `pwd`:/pyclient ${REGISTRY_URL}/${PYCLIENT_CONTAINER} /bin/bash

build-container:
	docker build -t ${REGISTRY_URL}/${PYCLIENT_CONTAINER} .
