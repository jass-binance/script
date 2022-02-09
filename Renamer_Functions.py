import os
from datetime import datetime

# Initialize Variables
datetime_format = "%d-%b-%Y"
filename_dic = {}
directory_list = []


# Initialize the Access function, which renames the files in a given directory.
def access(dir_name):
    with os.scandir(dir_name) as dir_list:
        # Iterate through each entry of files or sub-directories in the directory.
        for each_entry in dir_list:
            # Check whether the entry is a File or a Directory.
            if each_entry.is_dir():
                # If the entry is a Directory, Iterate thorough sub-directory using recursion.
                print(r"{}{}".format("It is a directory | ", each_entry.name))
                access(each_entry)
            else:
                # Variable to store the formatted date of the file
                file_modified_date = datetime.fromtimestamp(each_entry.stat().st_mtime).strftime(datetime_format)
                filename_dic[each_entry.path] = file_modified_date
    return filename_dic


def renamer(file_dictionary, force=True):
    for old_name, date in file_dictionary.items():
        # Split extension from name
        name_and_extension = os.path.splitext(old_name)
        new_name = name_and_extension[0] + ' (' + date.upper() + ')' + name_and_extension[1]
        # Rename files
        print(old_name, new_name)
        if date.upper() not in old_name or force is True:
            os.rename(old_name, new_name)


#list = access(r"C:\Users\Jass\Desktop\Renamer\Test")
#renamer(list, "false")
