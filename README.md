# Python Package Manager —— ppm

- Author: Jack Jiang
- Date: Jul. 2019

ppm allows you to manage python virtual environment packages as easy as using npm

ppm is just a wrapper of [python venv](https://docs.python.org/3/library/venv.html) module and [pip](https://pypi.org/project/pip/).

## Setup:

### Method 1: Symbolic link

```shell
git clone https://github.com/Jiangyiqun/ppm.git && cd ppm && sudo ln -s $(pwd)/ppm /usr/bin/ppm
```

to uninstall, just type

```shell
sudo rm /usr/bin/ppm
```

### Method 2: Add to $PATH

```shell
git clone https://github.com/Jiangyiqun/ppm.git && cd ppm && echo "export PATH=\"\$PATH:$(pwd)\"" >> ~/.bashrc && source ~/.bashrc
```

to unisntall, you need to mannually remove the last line in ~/.bashrc

## Usage:

### ppm install

Install Packages from package.txt

Alias: ppm i

### ppm install <pkg1> <pkg2> ... <pkgn>

Install package <pkg1> <pkg2> ... <pkgn> and add to package.txt

Alias: ppm i

### ppm uninstall <pkg1> <pkg2> ... <pkgn>

Uninstall package <pkg1> <pkg2> ... <pkgn> and remove from package.txt

### ppm list

Show installed packages

Alias: ppm ls

### ppm start

Start main.py in current directory

### ppm start <py>

start python file <py> in currrent directory

### ppm create-python-app <folder>

create a hello world app in <folder>

### ppm create-flask-app <folder>

create a flask app in <folder>

## FAQ:

### 1. permission denied

```shell
chmod +x ppm
```

### 2. No module named venv / command not found: pip

Install either [Anaconda (Python 3)](https://www.anaconda.com/distribution/#download-section)
or [python venv](https://docs.python.org/3/library/venv.html) and [pip](https://pypi.org/project/pip/)

## System Compatibility:

Does not support Windows