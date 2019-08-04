import sys
import os
import importlib
current_path = os.getcwd()
interpreter_path = sys.executable
print("Current Path:", current_path)
print("Interpreter Path:", interpreter_path)
print("Current File: ", sys.argv[0])
if (len(sys.argv) == 1):
    print("No arguments")
else:
    for i in range(1, len(sys.argv)):
        try:
            importlib.import_module(sys.argv[i])
            print(sys.argv[i], "exists")
        except ImportError:
            print(sys.argv[i], "not found")
        
