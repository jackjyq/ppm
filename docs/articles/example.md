# EXAMPLE

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