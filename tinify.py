# -*- coding: utf-8 -*-
"""
Created on Apr  3 11:30:08 2020

@author: Andrew.S

This utilizes the libraries tinify and os to make pngs or jpgs 'tiny' for web dev

This script will guide you after running the first time.
"""

import tinify
import os

tinify.key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" #insert API KEY HERE

currentDirectory = os.getcwd() + "/"
currentDirectory = currentDirectory.replace("\\", "/")

imagesDirectory = currentDirectory+"images/unoptimized/"
optimImagesDirectory = currentDirectory+"images/optimized/"

try:
    # Create target Directory
    os.makedirs(imagesDirectory)
    print("Directory \"" + imagesDirectory +  "\" was created,\n\tPlease load images into directory and run again") 
except FileExistsError:
    print("Directory " , imagesDirectory ,  " already exists")
    
    try:
        # Create target Directory
        os.makedirs(optimImagesDirectory)
        print("Directory " , optimImagesDirectory ,  " Created ") 
    except FileExistsError:
        print("Directory " , optimImagesDirectory ,  " already exists\n\nProcessing Images...")
    
    
    imageNames = os.listdir(imagesDirectory)
     
    
    for imageName in imageNames:
        if imageName.endswith(".png") or imageName.endswith(".jpg") or imageName.endswith(".jpeg"):
            unOptDir = imagesDirectory + imageName
            optDir = optimImagesDirectory+imageName
            
            if(not os.path.isfile(optDir)):
                source = tinify.from_file(unOptDir)
                source.to_file(optDir)
                print("File " , optDir ,  " Created ") 
            else:
                print("File " , optDir ,  " already exists")
        else:
            print ("Can't process: " + imageName)
    
print("End of Processing")
    
