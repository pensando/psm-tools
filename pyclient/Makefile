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

clean:
	find ./apigroups -mindepth 1 ! -regex '^./apigroups/test/.*' -delete