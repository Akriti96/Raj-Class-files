import time
import os
import shutil


import random
# print(dir(time))
# print(time.gmtime())


# print(os.getcwd())

path="C:/Users/Mamatha-Win10/Downloads/yamuna"


# spliting files
# path2=r"C:\Users\Mamatha-Win10\Downloads\yamuna\Screenshot 2023-04-26 195106.png"
# spliting= os.path.splitext(path2)
# print(spliting[1])


# checking path exists or not
# path3=r"C:\Users\Mamatha-Win10\Downloads\dhivya"
# print(os.path.exists(path3))
# # print(os.listdir(path))


# renaming folder or file using os 

# source=r"C:\Users\Mamatha-Win10\Downloads\yamuna"
# destination=r"C:\Users\Mamatha-Win10\Downloads\Raj"
# renaming= os.rename(source,destination)


# moving and copying files using shutil module

# source=r"C:\Users\Mamatha-Win10\Downloads\Raj\Screenshot 2023-04-26 195106.png"
# destination=r"C:\Users\Mamatha-Win10\Downloads\y"

# copy= shutil.move(source,destination)
# print("copied done")



# creating new folder using os
mypath=r"C:\Users\Mamatha-Win10\Downloads\students"
os.makedirs(mypath)