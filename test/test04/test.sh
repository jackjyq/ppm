#!/bin/bash
rm -rf temp
mkdir temp
cd temp


cp ../main.py main.py
ppm install
ppm install flask
ppm u flask
ppm start main.py flask
cat ./package-lock.txt