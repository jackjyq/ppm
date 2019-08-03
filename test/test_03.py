import sys
import os
if not ( os.getcwd() + "/python_modules/bin/python" == sys.executable):
    print("test failed!")
    exit()

try:
    import flask
except ModuleNotFoundError:
    print("flask import failed")
    exit()

try:
    import flask_cors
except ModuleNotFoundError:
    print("succeed")
    exit()
print("failed")
