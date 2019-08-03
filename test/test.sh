#!/bin/bash
TEST_PATH="temp"

rm -rf $TEST_PATH
mkdir $TEST_PATH
cd $TEST_PATH
ppm install
cp "../test_01.py" main.py
ppm start

ppm install flask flask-cors
cp "../test_02.py" main.py
ppm start

ppm uninstall flask-cors
cp "../test_03.py" main.py
ppm start

cp "../test_04.txt" package.txt
ppm i