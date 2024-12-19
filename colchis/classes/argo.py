''' class definition for argonaut
    takes one param on instantiation:
        json_path: the path to the json file being processed
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
        except json.decoder.JSONDecodeError:
            print(f"File {file_path} is not valid JSON")
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
            print("Invalid JSON syntax:", e)
            return False

    def depict_json(self):
        """ developer feature to show the object structure """

        print(json.dumps(self.json_obj, indent=4))

    def depict_struct(self, sub_obj=None):
        """ developer feature to show the object structure """

        if not sub_obj:
            this_obj = self.json_obj
        else:
            this_obj = sub_obj

        print(type(this_obj))
        print("{----+")
        print("     |")
        print("     |")
        print(f"     {this_obj.keys()[0]}")

        if sub_obj and sub_obj.values() != -1:
            self.depict_struct(list(this_obj.values())[0])

    def create_key_list(self):
        """ create a list of keys """
        pass

    def create_value_list(self):
        """ create a list of valid values """
        pass

    def add_key_value(self):
        """ add a key value pair """
        pass

    def delete_key_value(self):
        """ delete a key:value pair """
        pass

    def update_key(self):
        """ update a key without changing the structure or the value """
        pass

    def update_value(self):
        """ update a value without changing the structure or the key """
        pass

    def find_key(self):
        """ find a key """
        pass

    def find_value(self):
        """ find or get all values """
        pass

    def find_except(self):
        """ find values except those in a list of values """
        pass

    def find_element(self):
        """ find an element in a list, return the index """
        pass

    def delete_element(self):
        """ delete an element from the list """
        pass

    def update_element(self):
        """ update an element in the same location in the list """
        pass

    def append_element(self):
        """ append an element to the end of a list """
        pass

    def insert_element(self):
        """ insert an element into a list in order """
        pass

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
        except json.decoder.JSONDecodeError:
            print(f"File {file_path} is not valid JSON")
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
                raise TypeError(f"Parameter {param[0]} is not of type {allowed_types}")

        return True
