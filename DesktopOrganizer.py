import os
import shutil

desktop_path = os.path.expanduser("~/Desktop/Path") #using a folder from desktop for testing
desktop_items = os.listdir(desktop_path)

files_by_extension = {}
for item in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, item)
    if os.path.isfile(file_path):
        file_extenstion = os.path.splitext(item)[1]
        if file_extenstion not in files_by_extension:
            files_by_extension[file_extenstion] = [] # creating a list for a  new specific extension in the dictionary

        files_by_extension[file_extenstion].append(item) # add to existing list

#create folders and move files
for extension,files in files_by_extension.items():
    folder_name = extension[1:].upper() + " files"
    folder_path = os.path.join(desktop_path, folder_name)
    #create folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    #move files to folder
    for file in files:
        source_file_path = os.path.join(desktop_path, file)
        shutil.move(source_file_path,folder_path)