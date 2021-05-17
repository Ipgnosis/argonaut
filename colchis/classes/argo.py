# the class definition for argonaut

import json
#import os

class Argo:

    def __init__(self, fPath):

        self.filePath = fPath

        if self.filePath.exists():
            self.jFile = self.read_json_data(self.filePath)


    # read a json data file
    def read_json_data(self, fname):

        try:
            with open(fname) as json_file:
                data = json.load(json_file)
            return data
        except OSError as error:
            print(error)
            print("File {} cannot be read".format(fname))
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
