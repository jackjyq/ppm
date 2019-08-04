#!/bin/bash
rm -rf temp
mkdir temp
cd temp

ppm install
cp ../main.py main.py
ppm start