import os
import sys
from sys import platform


xd = input("Would you like to update? (Y/N): ")
if xd == "Y":
    os.system("rm -rf Reaper ; git clone https://github.com/krisishere/Reaper ; cd Reaper ; python3 main.py")
    sys.exit()
else:
    print("ok")
    sys.exit()
