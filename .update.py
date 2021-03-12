import os
import sys
from sys import platform
path = os.getcwd()
parent = os.path.abspath(os.path.join(path, os.pardir))
os.chdir(parent)
print(os.getcwd())
xd = input("Would you like to update? (Y/N): ")
if xd == "Y":
    os.system("rm -rf Reaper ; git clone https://github.com/krisishere/Reaper ; mkdir Reaper/.info ; touch Reaper/.info/tos_agree.py ; python3 " + parent + "Reaper/main.py")
    os.chdir(parent + "/Reaper")
    sys.exit()
if xd == "y":
    os.system("rm -rf Reaper ; git clone https://github.com/krisishere/Reaper ; mkdir Reaper/.info ; touch Reaper/.info/tos_agree.py ; python3 " + parent + "Reaper/main.py")
    os.chdir(parent + "/Reaper")
    sys.exit()
else:
    print("ok")
    sys.exit()
