default:
	make getswagger
	make build-generator
	make genclient

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
