import os
import shutil

from_dir = "C:/Users/bmohi/Downloads"
to_dir = "C:/Users/bmohi/Downloads"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name,extenstion = os.path.splitext(file_name)

    if extenstion == "" :
        continue

    if extenstion in [".seb",".json",".exe",".apk",".dll",".msi"]:
        path1 = from_dir + '/' + file_name
        path2 = to_dir +"/" + "Others_file"
        path3 = to_dir +'/' + "Others_file" + "/" + file_name
        print("Path 1 ", path1)
        print("Path 3 ", path3)

        if os.path.exists(path2):
         print ("moving" + file_name + "....")
         shutil.move(path1,path3)

        else:
         os.makedirs(path2)
         print ("moving" + file_name + "....")
         shutil.move(path1,path3)