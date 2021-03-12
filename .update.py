import os
import sys
from sys import platform
path = os.getcwd()
parent = os.path.abspath(os.path.join(path, os.pardir))
os.system("cd " + parent)
os.chdir(parent*)
print(os.getcwd())
xd = input("Would you like to update? (Y/N): ")
if xd == "Y":
    os.system("rm -rf Reaper ; git clone https://github.com/krisishere/Reaper ; cd Reaper ; python3 main.py")
    sys.exit()
if xd == "y":
    os.system("rm -rf Reaper ; git clone https://github.com/krisishere/Reaper ; cd Reaper ; python3 main.py")
    sys.exit()
else:
    print("ok")
    sys.exit()
