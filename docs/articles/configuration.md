# CONFIGURATION

[![](http://ppm.jackjyq.com/images/logo.png)](http://ppm.jackjyq.com/)
[![](https://img.shields.io/badge/managed%20by-ppm-red)](http://ppm.jackjyq.com/)

## Description

You can edit `package.txt` to change the default configuration

### main.py

The default main Python file. When you run `ppm start`, it will run `MAIN_FILE` with `DEFAULT_ARGS` in current virtual environment

```shell
MAIN_FILE="main.py"
DEFAULT_ARGS=""
```

### python_modules/

The installed Python packages of the virtual environment

```shell
PACKAGE_PATH="python_modules"
```

### package-lock.txt

The list of python packages of the virtual environment

```shell
PACKAGE_LIST="package-lock.txt"
```

## Example

if you want to use ppm to manage an existing virtual environment create by venv, you may want to change `package.txt` like this:

```shell
MAIN_FILE="view.py"
PACKAGE_LIST="requirement.txt"
PACKAGE_PATH="venv"
```