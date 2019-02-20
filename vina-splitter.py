#Title            :vina-splitter.py
#Description      :iterates over all files in a directory and separates poses from pdbqt output file
#Author           :Carter Gottschalk(https://github.com/cgott98)
#Date             :2019-02-20
#Version          :0.1
#Notes            :Special thank you to Matt Ritzinger(https://github.com/mritzing) for extensive help
#=====================================================================================================#

import os # Import necessary os module

cwd = os.getcwd() #retrieves current directory that the script is in
for file in os.listdir(cwd): #iterates through all files in current directory
    filename = os.fsdecode(file)
    if filename.endswith(".pdbqt"): #only opens pdbqt files
        reading_file = open(filename, "r")
        baseFileName = os.path.splitext(filename)[0]; # = file name ending with pdbqt
        count = 1; # pose count
        fName = baseFileName+"_pose" + str(count) + ".pdb" 

        writing_file = open(fName, "w") 
        for line in reading_file:
            if "ENDMDL" not in line: 
                writing_file.write(line)
            else:
                writing_file.write("ENDMDL")
                writing_file.close() # close current file open new one
                count = count + 1; #increment pose count
                fName = baseFileName+"_pose" + str(count) + ".pdb" 
                writing_file = open(fName, "w") #open new file to write
    else:
        continue