# CONFIGURATION

You can edit `package.txt` to change the default configuration 

## `main.py`

The default main Python file. When you run `ppm start`, it will run `MAIN_FILE` with `DEFAULT_ARGS` in current virtual environment

### configuration

```shell
MAIN_FILE="main.py"
DEFAULT_ARGS=""
```

## `python_modules/`

The installed Python packages of the virtual environment

### configuration

```shell
PACKAGE_PATH="python_modules"
```

## `package-lock.txt`

The list of python packages of the virtual environment

### configuration

```shell
PACKAGE_LIST="package-lock.txt"
```