import os

# 1. create a directory

# directory
directory = "test_dir"

# Parent directory
parent_dir = "C:/Users/Walee"

# Path
path = os.path.join(parent_dir, directory)

# #Create the DIR
# os.mkdir(path)
# print("Directory '%s' created" % directory)

# 2 make a file in new directory

filename = "testfile.txt"
filepath = os.path.join(path, filename)

# Write to the new file
with open(os.path.join(path, filename),"w",) as file1:
    toFile = "Contents of my new file"
    file1.write(toFile)
print("File" + filename + " created in " + directory + "folder")