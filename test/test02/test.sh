#!/bin/bash
rm -rf temp
mkdir temp
cd temp


cp ../main.py main.py
cp ../package-lock.txt package-lock.txt
cp ../package.txt package.txt
ppm install
ppm start main.py flask