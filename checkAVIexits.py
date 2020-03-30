import os

rootdir = os.path.dirname(os.path.realpath(__file__))

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = subdir + os.sep + file 
        if filepath os.:
            print("folder is full")
        else:
            print("Folder is empty")