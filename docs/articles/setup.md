# SETUP

[![](http://ppm.jackjyq.com/images/logo.png)](http://ppm.jackjyq.com/)
[![](https://img.shields.io/badge/managed%20by-ppm-red)](http://ppm.jackjyq.com/)

## Requirements

- MacOS **OR** Linux
- [Anaconda (Python 3)](https://www.anaconda.com/distribution/#download-section) or 
**OR** ([Python venv](https://docs.Python.org/3/library/venv.html) and [pip](https://pypi.org/project/pip/))
- git

## Install

### 1. cd whatever directory you want to put ppm into

```shell
cd $HOME
```

### 2. run installation script

**bash user**

```shell
git clone https://github.com/Jiangyiqun/ppm.git && cd ppm && echo "export PATH=\"\$PATH:$(pwd)\"" >> $HOME/.bashrc && source $HOME/.bashrc
```

**zsh user**

```shell
git clone https://github.com/Jiangyiqun/ppm.git && cd ppm && echo "export PATH=\"\$PATH:$(pwd)\"" >> $HOME/.zshrc && source $HOME/.zshrc
```

### 3. test installation

```shell
ppm --version
```

## Uninstall

Remove the last line in `$HOME/.bashrc` or `$HOME/.zshrc`

## Trouble shooting

### 1. permission denied

```shell
chmod +x ppm
```

### 2. zsh or bash

```shell
echo $SHELL
```
