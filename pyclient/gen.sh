#!/bin/bash

for file in ./swagger/*
do
  str1="${file/\.json/}"
  str2="${str1/\.\/swagger\//}"
  str3="${str2/\//}"
  str4="${str3/svc_/}"

  java -jar bin/openapi-generator-cli.jar generate -i "$file" -p group=$str4 -c genconfig.json -g python -o apigroups/

  echo "$str4"
done
