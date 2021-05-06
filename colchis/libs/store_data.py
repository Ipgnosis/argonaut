# utility functions for managing JSON files


import json
import os
import requests
import config, modify

# read a json data file
def read_json_data(fname):

    try:
        with open(fname) as json_file:
            data = json.load(json_file)
        return data
    except OSError as error:
        print(error)
        print("File {} cannot be read".format(fname))
        return False


# write a json data file
def write_json_data(fname, wdata):

    try:
        with open(fname, 'w') as outfile:
            json.dump(wdata, outfile)
        return True
    except OSError as error:
        print(error)
        print("File {} cannot be saved".format(fname))
        return False


# delete a file
def delete_file(fname):

    try:
        os.remove(fname)
        return True
    except OSError as error:
        print(error)
        print("File {} cannot be removed".format(fname))
        return False


# rename a file
def rename_file(fromf, tof):

    try:
        os.rename(fromf, tof)
        return True
    except OSError as error:
        print(error)
        print("File {} cannot be removed".format(fromf))
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
