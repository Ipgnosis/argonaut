''' class definition for Argo
    takes one param on instantiation:
        json_path: the path to the json file being processed

    where possible, type checking is performed on parameters
'''

# import os
import json
from pathlib import Path
# import config


# the class definition for argonaut
class Argo:
    """ a class to facilitate json object operations """

    def __init__(self, json_path):

        these_params = [
            (json_path, Path)
        ]

        param_check = self.__good_params(these_params)
        if param_check:
            print(f"Instantiating '{json_path}' as an Argo object.")

        self.file_path = json_path

        self.json_obj = self.__read_json_data(self.file_path)

    # write a json data file
    def write_json_data(self, file_path, wdata, mode):
        """Takes a file path, data, write mode and writes data to the file"""

        these_params = [
            (file_path, Path),
            (wdata, (list, dict)),
            (mode, str)
        ]

        param_check = self.__good_params(these_params)
        if not param_check:
            return param_check

        try:
            with open(file_path, mode, encoding="utf-8") as outfile:
                json.dump(wdata, outfile, indent=4, ensure_ascii=False)
            # The file is automatically closed when the 'with' block ends
            return True
        except json.decoder.JSONDecodeError as e:
            print(f"{e}: file {file_path} is not valid JSON")
            return False
        except OSError as error:
            print(f"{error}: file {file_path} cannot be saved")
            return False

    # validate a json object
    def validate_json_data(self, json_data):
        """checks the validity of a json object"""

        try:
            if json.dumps(json_data):
                return True
            return False
        except json.decoder.JSONDecodeError as e:
            print(f"Invalid JSON syntax: {e}")
            return False

    def depict_json(self, d=None):
        """ developer feature to show the object contents """

        # this gives the option of sending a random dict
        # no param means use the instantiated object
        if not d:
            this_obj = self.json_obj
            print(f"Object output for {self.file_path}")
        else:
            this_obj = d

        print(json.dumps(this_obj, indent=4))

    def depict_struct(self, d=None, level=0):
        """ developer feature to show the object structure """

        # this gives the option of sending a random dict
        # no param means use the instantiated object
        if not d:
            this_obj = self.json_obj
            print(f"Structure diagram for {self.file_path}")
        else:
            this_obj = d

        # calculate the indentation
        spaces = "     " * level

        for key, value in this_obj.items():
            if isinstance(key, str) and isinstance(value, dict):
                print(f"{spaces}key = {type(key)}: value = {type(value)}")

            if isinstance(value, dict):
                self.depict_struct(value, level + 1)
            else:
                print(f"{spaces}key = {type(key)}: value = {type(value)}")

    def create_key_list(self):
        """ create a list of keys """

    def create_value_list(self):
        """ create a list of valid values """

    def add_key_value(self):
        """ add a key value pair """

    def delete_key_value(self):
        """ delete a key:value pair """

    def update_key(self):
        """ update a key without changing the structure or the value """

    def update_value(self):
        """ update a value without changing the structure or the key """

    def find_key(self):
        """ find a key """

    def find_value(self):
        """ find or get all values """

    def find_except(self):
        """ find values except those in a list of values """

    def find_element(self):
        """ find an element in a list, return the index """

    def delete_element(self):
        """ delete an element from the list """

    def update_element(self):
        """ update an element in the same location in the list """

    def append_element(self):
        """ append an element to the end of a list """

    def insert_element(self):
        """ insert an element into a list in order """

    # #################### private methods ############################

    # PRIVATE - read a json data file
    def __read_json_data(self, file_path):
        """ Takes a file path and returns a file or an error """

        these_params = [
            (file_path, Path)
        ]

        param_check = self.__good_params(these_params)
        if not param_check:
            return param_check

        try:
            with open(file_path, "r", encoding="utf-8") as json_file:
                return json.load(json_file)
            # The file is automatically closed when the 'with' block ends
        except json.decoder.JSONDecodeError as e:
            print(f"{e}: file {file_path} is not valid JSON")
            return False
        except OSError as error:
            print(f"{error}: File {file_path} cannot be read")
            return False

    # PRIVATE - checks params for all other functions
    def __good_params(self, params):
        """ takes a list of tuples and returns True or raises a TypeError """

        for param in params:
            allowed_types = param[1]
            if not isinstance(param[0], allowed_types):
                raise TypeError(f"The parameter value '{param[0]}' is not of type {allowed_types}")

        return True
