# USAGE

[![](http://ppm.jackjyq.com/images/logo.png)](http://ppm.jackjyq.com/)
[![](https://img.shields.io/badge/managed%20by-ppm-red)](http://ppm.jackjyq.com/)

## VERSION

### `ppm --version`

Show ppm version

### Alias `ppm -v`

## INSTALL

### `ppm install`

Install Packages from `package-lock.txt`;

If `package-lock.txt` does not exits, create a new Python virtual environment in current directory.

### `ppm install <package> [<package> ... <package>]`

Install packages and save to `package-lock.txt`;

### Alias `ppm i`

## START

### `ppm start`

Start main.py in current directory

### `ppm start <Python_file> [<arguments>]`

Start <Python_file> with <arguments> in current directory

### Alias `ppm s`

## UNINSTALL

### `ppm uninstall <package> [<package> ... <package>]`

Uninstall packages and save to `package-lock.txt`;

## UPGRADE

### `ppm upgrade`

Upgrade ppm itself