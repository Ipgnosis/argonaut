""" file-management helpers that aren't JSON-specific and don't belong on Argo """

import os
import shutil


def delete_file(fname):
    """ Delete the param file path """

    try:
        os.remove(fname)
        return True
    except OSError as error:
        print(f"{error}: file {fname} cannot be removed.")
        return False


def rename_file(fromf, tof):
    """ Rename a file in a path """

    try:
        os.rename(fromf, tof)
        return True
    except OSError as error:
        print(f"File {fromf} cannot be renamed: {error}")
        return False


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


def delete_all_files(this_path):
    """ delete all files in a directory """

    # Check if path dir exists first, if not, return False
    if not os.path.exists(this_path):
        return False

    success = True

    for file in os.listdir(this_path):
        if not delete_file(os.path.join(this_path, file)):
            success = False

    return success


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
