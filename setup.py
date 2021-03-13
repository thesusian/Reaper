import os
import sys
from sys import platform

if os.getuid():
    print("Script By KrisIsHere | Setup Tool Built 0.3")
    exit('\nroot access required\n')

if platform == "linux" or platform == "linux2":
    xd = input("Would you like to proceed with the instalation?: (Y/N) ")
    if xd == "y" or xd == "Y":
        os.system("apt install lolcat putty ; pip3 install bane pysocks ; mkdir .info")
    else:
        print("Setup stopped.")
elif platform == "darwin":
    print("This script is not currently supported for the Mac OS")
elif platform == "win32":
    print("This script is not currently supported for Windows 10 or bellow.")
else:
    print("Platform not recognised...")
    sys.exit()
