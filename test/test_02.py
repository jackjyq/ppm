import sys
import os
if not ( os.getcwd() + "/python_modules/bin/python" == sys.executable):
    print("test failed!")
    exit()

try:
    import flask, flask_cors
except ModuleNotFoundError:
    print("failed")
    exit()
    
print("succeed")