import os
from datetime import datetime

current_working_directory = os.getcwd()
print(current_working_directory)

# Initialize Variables
datetime_format = "%d-%b-%Y"
filename_dic = {}
directory_list = []

# Take user input wheather to include sub-folders
include_sub_folders = input("Do you want to include sub-folders? Y or N: ")
print(include_sub_folders)
if include_sub_folders.upper() in ["YES","Y"]:
    include_sub_folders = "Jass"

# Initialize the Access function, which renames the files in a given directory.
def access(dir_name):
    with os.scandir(dir_name) as dir_list:
        # Iterate through each entry of files or sub-directories in the directory.
        for each_entry in dir_list:
            # Check whether the entry is a File or a Directory.
            if each_entry.is_dir() and include_sub_folders == "Jass":
                # If the entry is a Directory, Iterate thorough sub-directory using recursion.
                print(r"{}{}".format("It is a directory | ", each_entry.name))
                access(each_entry)
            else:
                # Variable to store the formatted date of the file
                file_modified_date = datetime.fromtimestamp(each_entry.stat().st_mtime).strftime(datetime_format)
                filename_dic[each_entry.path] = file_modified_date
    return filename_dic

files_info_dictionary = access(str(current_working_directory))

print("List of files")
for key, val in files_info_dictionary.items(): 
    print(key, ' : ', val)


def renamer(file_dictionary, force=True):
    for old_name, date in file_dictionary.items():
        # Split extension from name
        name_and_extension = os.path.splitext(old_name)
        new_name = name_and_extension[0] + ' (' + date.upper() + ')' + name_and_extension[1]
        # Rename files
        print(old_name, new_name)
        if date.upper() not in old_name or force is True:
            os.rename(old_name, new_name)


# renamer(files_info_dictionary, "false")
