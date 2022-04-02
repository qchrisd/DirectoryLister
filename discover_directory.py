"""
This module aims to discover the contents of a directory and output the file/subdirectory names,
the absolute path, and the file type as a CSV.

"""

## Imports
import os
import pandas as pd


def discover_directory(dir_path: str):
    """Discovers the contents of a directory and returns it as a list."""
    try:
        os.path.exists(dir_path)
    except:
        print(f"Path {dir_path} was bad. Please try again.")
        return None
    dir_contents = os.listdir(dir_path)

    # Only return files
    dir_contents = [file for file in dir_contents if os.path.isfile(os.path.join(dir_path, file))]

    return dir_contents
    

def split_extension(file_name: str):
    """Strips the extension of a file name and returns the file name and extension as strings."""
    file_name_parts = file_name.split(".")

    if len(file_name_parts) == 1:
        return file_name_parts[0], None

    extension = "." + file_name_parts[-1]
    new_file_name = file_name_parts[0]

    # If the file is a hidden file and only have an extension, make the 
    if file_name_parts[0] == "":
        new_file_name = extension

    # If there is a period in the name that does not separate the extension, cat the parts
    if len(file_name_parts) > 2:
        file_name_parts.pop(-1)  # get rid of extension since we already have it
        cat_file_name = ""
        for part in file_name_parts:
            cat_file_name = cat_file_name + "." + part
        new_file_name = cat_file_name

    return new_file_name, extension


def create_directory_list(dir_path):
    """Compiles a list of files and extensions in a table."""
    dir_list = discover_directory(dir_path)
    data = []

    for item in dir_list:
        file_name, extension = split_extension(item)
        if extension == None:
            extension = "none"
        item_path = os.path.join(dir_path, item)
        data.append([file_name, item_path])

    df = pd.DataFrame(data=data, columns=["File Name", "Abs Path"])

    df.to_csv(f"{dir_path}/contents.csv", index=False, encoding="utf-8-sig")


if __name__ == "__main__":
    dir = r"\\usridata01\groups\Haircolor Metier\Joe\Shadebank Carton images\Starting pdf documents\jpgs"
    # dir = r"C:\Users\christopher.quartara\OneDrive - L'Oréal\Documents\Python\Discover_Directory"
    create_directory_list(dir)