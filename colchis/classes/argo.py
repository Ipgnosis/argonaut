''' class definition for argonaut
    takes one param on instantiation:
        fpath: the path to the json file being processed
'''

# import os
import json
from pathlib import Path
# import config


# the class definition for argonaut
class Argo:
    """ a class to facilitate json object operations """

    def __init__(self, json_path):

        self.file_path = json_path

        self.json_obj = self.__read_json_data(self.file_path)

    # write a json data file
    def write_json_data(self, file_path, wdata, mode):
        """Takes a file path, data, write mode and writes data to the file"""

        these_parms = [
            (file_path, Path),
            (wdata, dict),
            (mode, str)
        ]

        good_param_check = self.__good_params(these_parms)
        if not good_param_check:
            return good_param_check

        try:
            with open(file_path, mode, encoding="utf-8") as outfile:
                json.dump(wdata, outfile, indent=4, ensure_ascii=False)
            # The file is automatically closed when the 'with' block ends
            return True
        except OSError as error:
            print(error)
            print(f"File {file_path} cannot be saved")
            return False

    # #################### private methods ############################

    # PRIVATE - read a json data file
    def __read_json_data(self, file_path):
        """ Takes a file path and returns a file or an error """

        these_parms = [
            (file_path, Path)
        ]

        good_param_check = self.__good_params(these_parms)
        if not good_param_check:
            return good_param_check

        try:
            with open(file_path, "r", encoding="utf-8") as json_file:
                return json.load(json_file)
            # The file is automatically closed when the 'with' block ends
        except OSError as error:
            print(error)
            print(f"File {file_path} cannot be read")
            return False

    # PRIVATE - checks params for all other functions
    def __good_params(self, params):
        """ takes a list of tuples and returns True or raises a TypeError """

        for param in params:

            if not isinstance(param[0], param[1]):
                raise TypeError(f"Parameter {param[0]} is not of type {param[1]}")

        return True
