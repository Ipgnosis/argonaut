""" class definition for Argo
    takes one param on instantiation:
        json_path: the path to the json file being processed

    where possible, type checking is performed on parameters

    there are also some methods that are public that will work on separate (non-instantiated)
    json structures: this is intentional to aid development
"""

import json
from pathlib import Path


# the class definition for argonaut
# see the README
class Argo:
    """ a class to facilitate json object operations """

    # instantiate
    def __init__(self, json_path):

        # type checking on params
        these_params = [
            (json_path, Path)
        ]

        param_check = self.__good_params(these_params)
        if param_check:
            print(f"\nInstantiating '{json_path}' as an Argo object.")

        # create global objects
        self.file_path = json_path

        self.json_obj = self.__read_json_data(self.file_path)

        self.obj_struct = type(self.json_obj)

        self.line_count = 0

    # write a json data file
    def write_json_data(self, file_path, wdata, mode):
        """Takes a file path, data, write mode and writes data to the file"""

        # type checking on params
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

    # validate an external json object
    def validate_json_data(self, j_obj):
        """ developer productivity feature: check the validity of a json object """

        # type checking on params
        these_params = [(j_obj, (list, dict))]

        param_check = self.__good_params(these_params)
        if not param_check:
            return param_check

        # validate
        try:
            if json.dumps(j_obj):
                print("Valid JSON syntax.")
                return True
            return False
        except json.decoder.JSONDecodeError as e:
            print(f"Invalid JSON syntax: {e}")
            return False

    # print out the file to the terminal with indentation
    def print_json(self, j_obj=None):
        """ developer feature to show the object contents """

        # this gives the option of sending a random dict
        # no param means use the instantiated object
        if not j_obj:
            this_obj = self.json_obj
            print(f"Object output for {self.file_path}")
        else:
            # type checking on params
            these_params = [(j_obj, (list, dict))]

            param_check = self.__good_params(these_params)
            if not param_check:
                return param_check

            this_obj = j_obj

        # output the j_obj
        print(json.dumps(this_obj, indent=4))

        return True

    # print out a json structure to the terminal with types and indentation
    # def depict_struct(self, j_obj=None, lines=10, level=0, line_count=0):
    def depict_struct(self, j_obj=None, lines=10, level=0):
        """developer productivity feature to show a json object structure"""

        # this gives the option of sending a random dict
        # no param means use the instantiated object
        if not j_obj:
            this_obj = self.json_obj
            print(f"Structure diagram for {self.file_path}:")
        else:
            # type checking on params
            these_params = [
                (j_obj, (list, dict)),
                (lines, int),
                (level, int)
                # (line_count, int),
            ]

            param_check = self.__good_params(these_params)
            if not param_check:
                return param_check

            this_obj = j_obj

        # calculate the indentation
        spaces = "     " * level

        # run the output
        if isinstance(this_obj, dict):
            if level == 0:
                print(f"\nThe object is of type {type(this_obj)}")
            for key, value in this_obj.items():
                if isinstance(value, dict):
                    print(f"\n{spaces}key = {type(key)}: value = {type(value)}")
                    # manage the scrolling
                    # line_count = self.__line_counter(line_count, lines)
                    # self.depict_struct(value, lines, level + 1, line_count)
                    self.__line_counter(lines)
                    self.depict_struct(value, lines, level + 1)

                else:
                    print(f"{spaces}key = {type(key)}: value = {type(value)}")

        elif isinstance(this_obj, list):
            if level == 0:
                print(f"\nThe object is of type {type(this_obj)}")
            for index, item in enumerate(this_obj):
                if isinstance(item, (dict, list)):
                    print(f"\n{spaces}index = {index}: value = {type(item)}")
                    # manage the scrolling
                    # line_count = self.__line_counter(line_count, lines)
                    # self.depict_struct(item, lines, level + 1, line_count)
                    self.__line_counter(lines)
                    self.depict_struct(item, lines, level + 1)
                else:
                    print(f"{spaces}index = {index}: value = {type(item)}")

        else:  # Handle other data types like strings, numbers, etc.
            print(f"{spaces}value = {type(this_obj)}: {this_obj}")
            # manage the scrolling
            # line_count = self.__line_counter(line_count, lines)
            self.__line_counter(lines)

        return True

    # atomic function
    def create_key_list(self, this_dict):
        """ create a list of keys """

        these_params = [(this_dict, dict)]

        param_check = self.__good_params(these_params)
        if not param_check:
            return param_check

        return list(this_dict)

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

    # atomic function
    def get_value(self, this_dict, this_key):
        """ get value from a dict given a key """

        these_params = [
            (this_dict, dict),
            (this_key, (str))
        ]

        param_check = self.__good_params(these_params)
        if not param_check:
            return param_check

        return this_dict.get(this_key, f"get_value: key {this_key} not found.")

    def find_except(self, this_list, exceptions_list):
        """ find values except those in a list of values """

    def find_element_index(self, this_list, val):
        """ find an element in a list, return the index """

        these_params = [
            (this_list, list),
            (val, (str, int, float, bool))
        ]

        param_check = self.__good_params(these_params)
        if not param_check:
            return param_check

        return this_list.index(val)

    def delete_element(self):
        """ delete an element from the list """

    def update_element(self):
        """ update an element in the same location in the list """

    # atomic function
    def append_element(self, this_list, elem):
        """ append an element to the end of a list """

        these_params = [
            (this_list, list),
            (elem, (str, int, float, bool, dict, list))
        ]

        param_check = self.__good_params(these_params)
        if not param_check:
            return param_check

        if this_list.append(elem):
            return True

        return False

    # atomic function
    def extend_list(self, this_list, new_list):
        """append an element to the end of a list"""

        these_params = [
            (this_list, list),
            (new_list, (list))]

        param_check = self.__good_params(these_params)
        if not param_check:
            return param_check

        if this_list.extend(this_list):
            return True

        return False

    # atomic function
    def insert_element(self):
        """ insert an element into a list in order """

    # #################### private methods ############################

    # PRIVATE - read a json data file
    # called only by __init__ (maybe others later??)
    # there's a case to be made that this method should be public, so that any json file can be read
    # but the purpose of argonaut is to improve productivity on json wrangling
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

    # PRIVATE - type checking on params for all other functions
    def __good_params(self, params):
        """ takes a list of tuples and returns True or raises a TypeError """

        for param in params:
            allowed_types = param[1]
            if not isinstance(param[0], allowed_types):
                raise TypeError(f"The parameter value '{param[0]}' is not of type {allowed_types}")

        return True

    # PRIVATE - manage the line count for depict_struct
    # this doesn't work perfectly: the recursion breaks the line count
    # but it works well enough for now
    # def __line_counter(self, line_count, lines):
    def __line_counter(self, lines):
        """ manage the line-count and implement pause as required """

        # increment line count since we have just printed a line
        self.line_count += 1

        # have we breached the line limit?
        if self.line_count > lines:

            while True:
                input("Press 'Enter' to continue, or 'CTRL-C' to stop...")
                break

            self.line_count = 0

        # return line_count
