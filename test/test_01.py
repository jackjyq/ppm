import sys
import os
if ( os.getcwd() + "/python_modules/bin/python" == sys.executable):
    print("test passed!")
else:
    print("test failed!")