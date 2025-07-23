import os
import shutil

path = input("Enter the path of the directory to organize: ")
files = os.listdir(path)

for file in files:
    file_path = os.path.join(path, file)
    
    if os.path.isdir(file_path):
        continue

    filename, extension = os.path.splitext(file)
  
    if not extension:
        continue
    
    extension = extension[1:]
    destination_folder = os.path.join(path, extension)
    
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    shutil.move(file_path, os.path.join(destination_folder, file))

print("Files organized successfully.")
