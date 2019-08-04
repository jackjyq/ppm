# [ppm](https://jiangyiqun.github.io/ppm/)

[ppm](https://jiangyiqun.github.io/ppm/) allows you to manage Python virtual environment packages as easy as using [npm](https://docs.npmjs.com/);

ppm is just a wrapper of [Python venv](https://docs.Python.org/3/library/venv.html) module and [pip](https://pypi.org/project/pip/).

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

## Read the [documentation](https://jiangyiqun.github.io/ppm/) for detail