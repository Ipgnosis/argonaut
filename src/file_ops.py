""" file-management helpers that aren't JSON-specific and don't belong on Argo """

import os
import shutil

# NOTE: path params are written out in full (`str | os.PathLike[str]`) at
# every use below rather than factored into a named type alias - see
# src/argo.py's top-of-file note for why (a named alias triggered a Pylance
# strict-mode false positive even with an explicit `TypeAlias` annotation).


def delete_file(fname: str | os.PathLike[str]) -> bool:
    """ Delete the param file path """

    try:
        os.remove(fname)
        return True
    except OSError as error:
        print(f"{error}: file {fname} cannot be removed.")
        return False


def rename_file(fromf: str | os.PathLike[str], tof: str | os.PathLike[str]) -> bool:
    """ Rename a file in a path """

    try:
        os.rename(fromf, tof)
        return True
    except OSError as error:
        print(f"File {fromf} cannot be renamed: {error}")
        return False


def move_files(from_path: str | os.PathLike[str], to_path: str | os.PathLike[str]) -> bool:
    """ move all files in one directory to another """

    # Check if from_path dir exists first, if not, return False
    if not os.path.exists(from_path):
        return False

    # Check if to_path dir exists first, if not, create the folder
    if not os.path.exists(to_path):
        os.mkdir(to_path)

    success = True

    for file in os.listdir(from_path):
        try:
            source = os.path.join(from_path, file)
            destination = os.path.join(to_path, file)
            shutil.move(source, destination)
        except OSError as error:
            print(f"File {file} cannot be moved: {error}")
            success = False

    return success


def delete_all_files(this_path: str | os.PathLike[str]) -> bool:
    """ delete all files in a directory """

    # Check if path dir exists first, if not, return False
    if not os.path.exists(this_path):
        return False

    success = True

    for file in os.listdir(this_path):
        if not delete_file(os.path.join(this_path, file)):
            success = False

    return success


def copy_all_files(here: str | os.PathLike[str], there: str | os.PathLike[str]) -> bool:
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
