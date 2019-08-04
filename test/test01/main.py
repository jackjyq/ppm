import sys
import os
import importlib
current_path = os.getcwd()
interpreter_path = sys.executable
print("Current Path:", current_path)
print("Interpreter Path:", interpreter_path)
print("The file you are running: ", sys.argv[0])
if (len(sys.argv) == 1):
    print("No arguments")
else:
    for i in range(1, len(sys.argv)):
        try:
            importlib.import_module(sys.argv[i])
            print("     has module named: ", sys.argv[i])
        except ImportError:
            print("     No module named ", sys.argv[i])
        
