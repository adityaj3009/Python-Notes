import os
import shutil

path = "D:\\Python\\folder"

try:
#    os.remove(path)         # to delete a file
#    os.rmdir(path)          # to delete an empty directory
    shutil.rmtree(path)     # use to delete a directory containing file (use import shutil)
except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print("You dont have permission to delete this file")
except OSError:
    print("You cannot delte using that function")
else:
    print(path + " was deleted")

