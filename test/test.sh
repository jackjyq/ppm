#!/bin/bash
rm -rf temp
mkdir temp
cd temp
ppm install
if ! [ $? == 0 ]; then
    echo "Bad return value, test failed"
    exit 1
fi

cp "../interpreter_path.py" main.py
if [ $(ppm start) == "$(pwd)/python_modules/bin/python" ]; then
    echo "succeed"
fi