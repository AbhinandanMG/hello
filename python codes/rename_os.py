import os
import string
def rename_files(path,file_type):
    '''Takes Path and File type as arguements and Renames all the files from 1 to n'''
    os.chdir(path) 
    files=os.listdir() 
    i=1
    for file in files:
        if file.endswith(f".{file_type}"):
            os.rename(f"{file}",f"{i}.{file_type}")
            i=i+1
    print("renamed successfully")
    
path =input("Enter the path:")
fileType= input("enter the file type:")
rename_files(path,fileType)