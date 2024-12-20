""" functions to read, write, move, copy, delete files """

import os
import shutil
import json


# read a json data file
def read_json_data(fname):
    """ Takes a file path and returns a file or an error """

    try:
        with open(fname, "r", encoding="utf-8") as json_file:
            return json.load(json_file)
        # The file is automatically closed when the 'with' block ends
    except json.decoder.JSONDecodeError as e:
        print(f"{e}: file {fname} is not valid JSON")
        return False
    except OSError as error:
        print(f"{error}: File {fname} cannot be read")
        return False


# write a json data file
def write_json_data(fname, wdata, mode):
    """ Takes a file path, data, write mode and writes data to the file
        Runs a validity check first
    """

    try:
        with open(fname, mode, encoding="utf-8") as outfile:
            json.dump(wdata, outfile, indent=4, ensure_ascii=False)
        # The file is automatically closed when the 'with' block ends
        return True
    except json.decoder.JSONDecodeError as e:
        print(f"{e}: file {fname} is not valid JSON")
        return False
    except OSError as error:
        print(f"{error}: file {fname} cannot be saved")
        return False


# validate a json object
def validate_json_data(json_data):
    """ checks the validity of a json object """

    try:
        if json.dumps(json_data):
            return True
        return False
    except json.decoder.JSONDecodeError as e:
        print(f"Invalid JSON syntax: {e}")
        return False


# delete a file given a path
def delete_file(fname):
    """ Delete the param file path """

    try:
        os.remove(fname)
        return True
    except OSError as error:
        print(f"{error}: file {fname} cannot be removed.")
        return False


# rename a file given 2 paths
def rename_file(fromf, tof):
    """ Rename a file in a path """

    try:
        os.rename(fromf, tof)
        return True
    except OSError as error:
        print(f"File {fromf} cannot be renamed: {error}")
        return False


# move all files given 2 paths
def move_files(fromPath, toPath):
    """ move all files in one directory to another """

    # Check if fromPath dir exists first, if not, return False
    if not os.path.exists(fromPath):
        return False

    # Check if toPath dir exists first, if not, create the folder
    if not os.path.exists(toPath):
        os.mkdir(toPath)

    success = True

    for file in os.listdir(fromPath):
        try:
            source = os.path.join(fromPath, file)
            destination = os.path.join(toPath, file)
            shutil.move(source, destination)
        except OSError as error:
            print(f"File {file} cannot be moved: {error}")
            success = False

    return success


# delete all files given a path
def delete_all_files(this_path):
    """ delete all files in a directory """

    # Check if path dir exists first, if not, return False
    if not os.path.exists(this_path):
        return False

    success = True

    for file in os.listdir(this_path):
        try:
            delete_file(file)
        except OSError as error:
            print(f"File {file} cannot be moved: {error}")
            success = False

    return success


# copy all files given 2 paths
def copy_all_files(here, there):
    """copy all files in a directory to another directory """

    # Check if 'here' path dir exists first, if not, return False
    if not os.path.exists(here):
        print(f"Directory {here} does not exist.")
        return False

    # Check if 'there' dir exists first, if not, create the folder
    if not os.path.exists(there):
        print(f"Creating directory {there}")
        os.mkdir(there)

    success = True

    for file in os.listdir(here):
        try:
            shutil.copy(os.path.join(here, file), there)
        except OSError as error:
            print(f"File {file} cannot be copied: {error}")
            success = False

    return success

def append_file(fpath, new_data):
    """ appends new data to existing file """

    old_data = read_json_data(fpath)

    # rename_file(fpath, old_version)




def main():
    """ test code """

    here = os.path.join(os.getcwd(), "data", "searches")
    there = os.path.join(os.getcwd(), "data", "logs")

    # if delete_all_files(there):
    #     print("All files deleted")
    # else:
    #     print("Files deleted")

    if copy_all_files(here, there):
        print("All files copied")
    else:
        print("Files not copied.")


if __name__ == "__main__":
    main()
