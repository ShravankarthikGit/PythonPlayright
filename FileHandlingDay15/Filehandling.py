# Example 1: Create/ writing a file

# appraoch 1: if the file does not exist a new file will be created
# w is for writing
# a is for appending
# r is for reading
# file=open("C:\\AADDrive\\Mystuff\\PlayWrightPython\\Automation\\automationFiles\\myfile.txt",'w')
# file.write("Welcome to python \n File handling")
# file.close()

#  If the file already exists then write will override the existing line
# In this case it will override first line "Welcome to python "
# file=open("C:\\AADDrive\\Mystuff\\PlayWrightPython\\Automation\\automationFiles\\myfile.txt",'w')
# file.write("Override \n File handling")
# file.close()

#Appraoch 2 : using with
# with open("C:\\AADDrive\\Mystuff\\PlayWrightPython\\Automation\\automationFiles\\myfile2.txt",'w') as file:
#     file.write("Welcome to python \n File handling")
#     file.close()


# Example 2: Appending data into file
# Note that append will not override data. It will insert as first line
# file=open("C:\\AADDrive\\Mystuff\\PlayWrightPython\\Automation\\automationFiles\\myfile.txt",'a')
# file.write("\n This line is appended...")
# file.close()


# Example 3: Reading data from text file
# read() - reads entire data
#readline() - read single line
#readlines() -- read all the lines in to list format

#
# file=open("C:\\AADDrive\\Mystuff\\PlayWrightPython\\Automation\\automationFiles\\myfile.txt",'r')
# Note that when we do read and readline together we will see empty line printed for readline
# When you read a file in Python, there is an invisible marker called the File Pointer (or cursor).
# It keeps track of where Python is currently reading.

# content=file.read()
# content2=file.readline()
# content3=file.readlines()
# print(content)
# print(content2)
# print(content3)
# file.close()


#4 Renaming the file
# import os
# os.rename("C:\\AADDrive\\Mystuff\\PlayWrightPython\\Automation\\automationFiles\\myfile.txt","C:\\AADDrive\\Mystuff\\PlayWrightPython\\Automation\\automationFiles\\myfilerename.txt")
# print("File renamed...")


#5 Deleting the file
# import os
#
# file="C:\\AADDrive\\Mystuff\\PlayWrightPython\\Automation\\automationFiles\\myfile2.txt"
#
# if os.path.exists(file):
#     os.remove(file)
# else:
#     print("File does not exist")


# 6. Creating a directory/folder
# import os
# os.mkdir("C:\\AADDrive\\Mystuff\\PlayWrightPython\\Automation\\automationFiles\\mydir")
# print("Directory created..")


#7. Check the directory exist or not
# import os
# mydir="C:\\AADDrive\\Mystuff\\PlayWrightPython\\Automation\\automationFiles\\mydir"
#
# if os.path.exists(mydir):
#     print("Directory exists")
# else:
#     print("Directory not exists")


#8. Rename the directory
# import os
#
# os.rename("C:\\AADDrive\\Mystuff\\PlayWrightPython\\Automation\\automationFiles\\mydir","C:\\AADDrive\\Mystuff\\PlayWrightPython\\Automation\\automationFiles\\mydir1")
# print("Directory renamed...")


#9. remove/delete the directory
# import os
# import shutil
# os.rmdir("C:\\AADDrive\\Mystuff\\PlayWrightPython\\Automation\\automationFiles\\mydir") # if folder/directory is empty.
# shutil.rmtree("C:\\AADDrive\\Mystuff\\PlayWrightPython\\Automation\\automationFiles\\test")  # if the folder/directory contains files


#10. get the current working directory

import os
print(os.getcwd()) # returns current working directory





