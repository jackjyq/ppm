# ppm Documentation

[![](./images/logo.png)](./articles/logo.html)

ppm allows you to manage Python virtual environment packages as easy as using [npm](https://docs.npmjs.com/);

ppm is just a wrapper of [Python venv](https://docs.Python.org/3/library/venv.html) module and [pip](https://pypi.org/project/pip/).

[![](https://img.shields.io/badge/managed%20by-ppm-red)](./articles/logo.html)
[![GitHub stars](https://img.shields.io/github/stars/Jiangyiqun/ppm)](https://github.com/Jiangyiqun/ppm/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Jiangyiqun/ppm)](https://github.com/Jiangyiqun/ppm/network)
[![GitHub issues](https://img.shields.io/github/issues/Jiangyiqun/ppm)](https://github.com/Jiangyiqun/ppm/issues)
<!-- [![GitHub license](https://img.shields.io/github/license/Jiangyiqun/ppm)](https://github.com/Jiangyiqun/ppm) -->

## Example

Using ppm to manage Python virtual environment is easy

```shell
ppm i
```

which is equivalent to

```shell
python3 -m venv Python_modules               # create Python environment
source ./Python_modules/bin/activate         # activate Python environment
python3 -m pip install -r package-lock.txt   # install Python modules from package-lock.txt
deactivate                                   # deactivate Python environment
```

## Setup

ppm file is self-contained, you only need one single file to run. However, I recommend you to clone the repository in order to get the update.

### install

**bash user(default)**

```shell
git clone https://github.com/Jiangyiqun/ppm.git && cd ppm && echo "export PATH=\"\$PATH:$(pwd)\"" >> ~/.bashrc && source ~/.bashrc
```

**zsh user**

```shell
git clone https://github.com/Jiangyiqun/ppm.git && cd ppm && echo "export PATH=\"\$PATH:$(pwd)\"" >> ~/.zshrc && source ~/.zshrc
```

**to know which shell you are using**

```shell
echo $SHELL
```

### uninstall

Remove the last line in `~/.bashrc` or `~/.zshrc`

### [trouble shooting](./articles/trouble_shooting.html)

## Commands

### [install](./articles/install.html)

```shell
ppm install
ppm install <package> [<package> ... <package>]
```

### [start](./articles/start.html)

```shell
ppm start
ppm start <Python_file> [<arguments>]
```

### [uninstall](./articles/uninstall.html)

```shell
ppm uninstall <package> [<package> ... <package>]
```

## [Configuration](./articles/configuration.html)

```shell
DOCS="https://jiangyiqun.github.io/ppm/"
MAIN_FILE="main.py"
DEFAULT_ARGS=""
PACKAGE_LIST="package-lock.txt"
PACKAGE_PATH="python_modules"
```
