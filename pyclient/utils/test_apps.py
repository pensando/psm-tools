import subprocess as sp
import os

print("Testing apps:\n")
apps_directory = "../apps/"
index = 0
success = 0
for i in os.listdir(apps_directory):
    if i.endswith(".py"):
        child = sp.Popen(["python3", apps_directory+i], stdout=sp.PIPE, stderr=sp.PIPE)
        child.communicate()
        rc = child.returncode
        index += 1
        success = success + (1 if rc == 0 else 0)
        print("{0:<5} {1:<25} {2:<25}".format(index, i, "Success" if rc == 0 else "Failure"))

print("\n{}/{} tests passed.".format(success, index))