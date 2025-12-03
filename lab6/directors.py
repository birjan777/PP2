#1 Write a Python program to list only directories, files and all directories, files in a specified path.
import os
path = input("way to direc: ")
if not os.path.exists(path):
    print("unreal.")
else:
    file_count = 0
    folder_count = 0
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            file_count += 1
        elif os.path.isdir(full_path):
            folder_count += 1
    print("count files:", file_count)
    print("count foulders:", folder_count)


#2 Write a Python program to check for access to a specified path.
# Test the existence, readability, writability and executability of the specified path
import os
path = input("way to file: ")
if os.path.exists(path):
    print("exist")
    if os.access(path, os.R_OK):
        print("can read.")
    else:
        print("cannot read.")
    if os.access(path, os.W_OK):
        print("can write")
    else:
        print("cannot write")
    if os.access(path, os.X_OK):
        print("can execute")
    else:
        print("cannot execute.")
else:
    print("doesn't exist.")


#3 Write a Python program to test whether a given path exists or not.
# If the path exist find the filename and directory portion of the given path.
import os
path = input("way: ")
if os.path.exists(path):
    print("its exist.")
    directory = os.path.dirname(path)
    filename = os.path.basename(path)
    print("directory:", directory)
    print("fle:", filename)
else:
    print("doesn't exist.")

#4 Write a Python program to count the number of lines in a text file.

import os
file=r'c:/Users/khalenovbirzhan/Desktop/LAB6/directors.py/task3.py'
count=0
with open(file, 'r') as file:
    for line in file:
        count+=1
print("numbers lines:", count)

#5 Write a Python program to write a list to a file.

my_list = ["apple", "banana", "cherry", "orange"]
file_path = input("way: ")
with open(file_path, 'w') as file:
    for item in my_list:
        file.write(item + '\n')
print("it was written")


#6  Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import string
folder = input("way foulder: ")
for letter in string.ascii_uppercase:
    file_path = folder + '/' + letter + '.txt'
    with open(file_path, 'w') as file:
        file.write("This is file " + letter)
print("files from a to z were created.")

#7 Write a Python program to copy the contents of a file to another file

source_file = "c:/Users/user/Desktop/PP2/lab6/source.txt"
destination_file = "c:/Users/user/Desktop/PP2/lab6/destination.txt"
with open(source_file, "r") as src:
    content = src.read()
with open(destination_file, "w") as dst:
    dst.write(content)
print(f"copy the contents of a {source_file} to {destination_file}.")


#8 Write a Python program to delete file by specified path.
# Before deleting check for access and whether a given path exists or not.


import os
file_path = input("file you want to delete: ")
if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print("File deleted")
    else:
        print("cannot to delete")
else:
    print("doesn't exist.")