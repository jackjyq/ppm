# ppm —— Python Package Manager

- Author: Jack Jiang
- Date: Jul. 2019

ppm allows you to manage python virtual environment packages as easy as using npm

ppm is just a wrapper of [python venv](https://docs.python.org/3/library/venv.html) module and [pip](https://pypi.org/project/pip/).

# Example

### Install Python virtual environment modules from package.txt

```python
python3 -m venv python_modules          # create python environment
source ./python_modules/bin/activate    # activate python environment
python3 -m pip install -r package.txt   # install python modules from package.txt
deactivate                              # deactivate python environment
```

```shell
ppm install
```

### Install new Python virtual environment modules and save it to package.txt

```shell
python3 -m venv python_modules          # create python environment
pip install new-package					# install new-package
python -m pip freeze > package.txt		# save new-package to package.txt
deactivate      
```

```
ppm install new-package
```

### Run main.py with Python virtual environment modules

```shell
source ./python_modules/bin/activate    # activate python environment
python main.py                          # run back-end server
deactivate                              # deactivate python environment
```

```
ppm start
```

# Setup

ppm file is self-contained, you only need one single file to run. However, I recommend you to clone the repository in order to get the update.

### Method 1: Add to $PATH

```shell
git clone https://github.com/Jiangyiqun/ppm.git && cd ppm && echo "export PATH=\"\$PATH:$(pwd)\"" >> ~/.bashrc && source ~/.bashrc
```

### Method 2: Symbolic link

```shell
git clone https://github.com/Jiangyiqun/ppm.git && cd ppm && sudo ln -s $(pwd)/ppm /usr/bin/ppm
```

To uninstall, just type

```shell
sudo rm /usr/bin/ppm
```

To uninstall, you need to manually remove the last line in `~/.bashrc`

# Commands

![](./badges/-planned-yellow.svg)
![](./badges/-implemented-blue.svg)
![](./badges/-tested-green.svg)
![](./badges/-deprecated-red.svg)

## Init

### `ppm init`

![](./badges/-planned-yellow.svg)

create python virtual environment in current directory

___

## Start

### `ppm start`

![](./badges/-implemented-blue.svg)

Start main.py in current directory

### `ppm start <py>`

![](./badges/-implemented-blue.svg)

start python file `<py>` in currrent directory

___

## Install (Alias: i)

### `ppm install`

![](./badges/-implemented-blue.svg)

Install Packages from package.txt

### `ppm install <pkg1> <pkg2> ... <pkgn>`

![](./badges/-implemented-blue.svg)

Install package `<pkg1> <pkg2> ... <pkgn>` and add to package.txt

___

## Uninstall

### `ppm uninstall <pkg1> <pkg2> ... <pkgn>`

![](./badges/-implemented-blue.svg)

Uninstall package `<pkg1> <pkg2> ... <pkgn>` and remove from package.txt

## list (**Alias**: ls)

### `ppm list`

![](./badges/-implemented-blue.svg)

Show installed packages

___

## Update

### `ppm update`

![](./badges/-planned-yellow.svg)

Update all installed packages and synchronize it with package.txt

### `ppm update <pkg1> <pkg2> ... <pkgn>`

![](./badges/-planned-yellow.svg)

Update package `<pkg1> <pkg2> ... <pkgn>` and synchronize it with package.txt

___

## list (Alias: ls)

### `ppm list`

![](./badges/-planned-yellow.svg)

Show installed packages

___

## Create Apps

### `ppm create-python-app <folder>`

![](./badges/-deprecated-red.svg)

create a hello world app in `<folder>`

### `ppm create-flask-app <folder>`

![](./badges/-implemented-blue.svg)

create a flask app in `<folder>`

# FAQ:

### 1. permission denied

```shell
chmod +x ppm
```

### 2. No module named venv / command not found: pip

Install either [Anaconda (Python 3)](https://www.anaconda.com/distribution/#download-section)

or [python venv](https://docs.python.org/3/library/venv.html) and [pip](https://pypi.org/project/pip/)

### 3. System Compatibility:

Does not support Windows