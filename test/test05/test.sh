#!/bin/bash
rm -rf temp
mkdir temp
cd temp


cp ../main.py start.py
cp ../package.txt package.txt
ppm install
ppm i flask
ppm s