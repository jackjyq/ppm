# ppm Documentation

ppm allows you to manage Python virtual environment packages as easy as using [npm](https://docs.npmjs.com/);

ppm is just a wrapper of [Python venv](https://docs.Python.org/3/library/venv.html) module and [pip](https://pypi.org/project/pip/).

[![GitHub stars](https://img.shields.io/github/stars/Jiangyiqun/ppm)](https://github.com/Jiangyiqun/ppm/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Jiangyiqun/ppm)](https://github.com/Jiangyiqun/ppm/network)
[![GitHub issues](https://img.shields.io/github/issues/Jiangyiqun/ppm)](https://github.com/Jiangyiqun/ppm/issues)
<!-- [![GitHub license](https://img.shields.io/github/license/Jiangyiqun/ppm)](https://github.com/Jiangyiqun/ppm) -->
![](https://img.shields.io/badge/compatible-macOS-brightgreen)
![](https://img.shields.io/badge/compatible-Linux-orange)

## [Example](./articles/example.html)

To manage Python virtual environment, using ppm(left) is easier than traditional method(right)

![](./images/compare.png)

## [Setup](./articles/setup.html)

**bash user(default)**

```shell
git clone https://github.com/Jiangyiqun/ppm.git && cd ppm && echo "export PATH=\"\$PATH:$(pwd)\"" >> $HOME/.bashrc && source $HOME/.bashrc
```

**zsh user**

```shell
git clone https://github.com/Jiangyiqun/ppm.git && cd ppm && echo "export PATH=\"\$PATH:$(pwd)\"" >> $HOME/.zshrc && source $HOME/.zshrc
```

## Usage

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
DOCS="http://ppm.jackjyq.com/"
MAIN_FILE="main.py"
DEFAULT_ARGS=""
PACKAGE_LIST="package-lock.txt"
PACKAGE_PATH="python_modules"
```

## [Logo and Badge](./articles/logo.html)

[![](./images/logo.png)](http://ppm.jackjyq.com/)
[![](https://img.shields.io/badge/managed%20by-ppm-red)](http://ppm.jackjyq.com/)