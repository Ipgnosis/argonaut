# utility functions for managing JSON files


import json
import os
import requests
import config, modify

# read a json data file
def read_json_data(fname):
    """ Takes a file path and returns a file or an error """

    try:
        with open(fname, "r", encoding="utf-8") as json_file:
            return json.load(json_file)
        # The file is automatically closed when the 'with' block ends
    except OSError as error:
        print(error)
        print(f"File {fname} cannot be read")
        return False


# write a json data file
def write_json_data(fname, wdata, mode):
    """ Takes a file path, data, write mode and writes data to the file """

    try:
        with open(fname, mode, encoding="utf-8") as outfile:
            json.dump(wdata, outfile, indent=4, ensure_ascii=False)
        # The file is automatically closed when the 'with' block ends
        return True
    except OSError as error:
        print(error)
        print(f"File {fname} cannot be saved")


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


# test function

def main():

    #import os
    import sys

    proj_loc = "c:\\Users\\Ipgnosis\\Documents\\Github\\argonaut"

    sys.path.append(proj_loc)

    import config, modify


# stand alone test run
# don't forget to flip the import statements
if __name__ == "__main__":
    main()
