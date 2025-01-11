""" class definition for Argo
    takes one param on instantiation:
        json_path: the path to the json file being processed

    where possible, type checking is performed on parameters

    there are also some methods that are public that will work on separate
    (non-instantiated) json structures: this is intentional to aid development
"""

import json
from pathlib import Path


# the class definition for argonaut (aka colchis)
# see the README
class Argo:
    """ a class to facilitate json object operations and reduce development effort """

    # instantiate
    def __init__(self, json_path):

        # type checking on params
        these_params = [(json_path, Path)]

        param_check = self.__good_params(these_params)
        if param_check:
            print(f"\nInstantiating '{json_path}' as an Argo object.")

        # create global objects
        self.file_path = json_path

        self.json_obj = self.__read_json_data(self.file_path)

        self.obj_struct = type(self.json_obj)

        self.line_count = 0

    # write a json data file
    def write_json_data(self, file_path=None, wdata=None, mode=None):
        """Takes a file path, data, write mode and writes data to the file"""

        # insert the default params
        if file_path is None:
            file_path = self.file_path

        if wdata is None:
            wdata = self.json_obj

        if mode is None:
            mode = "w"

        # type checking on params
        these_params = [(file_path, Path), (wdata, (list, dict)), (mode, str)]

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
    # node that self.json_obj is pre-validated
    def validate_json_data(self, j_obj=None):
        """developer productivity feature: check the validity of a json object"""

        # this gives the option of sending a random dict
        # no param means use the instantiated object
        if not j_obj:
            j_obj = self.json_obj
            print(f"Object output for {self.file_path}")
        else:
            # quick param check
            if not isinstance(j_obj, (list, dict)):
                return False

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
        """developer feature to show the object contents"""

        # this gives the option of sending a random dict
        # no param means use the instantiated object
        if not j_obj:
            j_obj = self.json_obj
            print(f"Object output for {self.file_path}")
        else:
            # quick param check
            if not isinstance(j_obj, (list, dict)):
                return False

        # output the data
        print(json.dumps(j_obj, indent=4))

        return True

    # print out a json structure to the terminal with types and indentation
    def depict_struct(self, j_obj=None, lines=10, level=0):
        """developer productivity feature to show a json object structure"""

        # this gives the option of sending a random dict
        # no param means use the instantiated object
        if not j_obj:
            j_obj = self.json_obj
            print(f"Structure diagram for {self.file_path}:")
        else:
            # type checking on params
            these_params = [
                (j_obj, (list, dict)),
                (lines, int),
                (level, int)
            ]

            param_check = self.__good_params(these_params)
            if not param_check:
                return param_check

        # calculate the indentation
        spaces = "     " * level

        # run the output
        if isinstance(j_obj, dict):
            if level == 0:
                print(f"\nThe object is of type {type(j_obj)}")
            for key, value in j_obj.items():
                if isinstance(value, (dict, list)):
                    print(f"\n{spaces}key = {type(key)}: value = {type(value)}")
                    self.__line_counter(lines)
                    self.depict_struct(value, lines, level + 1)

                else:
                    print(f"{spaces}key = {type(key)}: value = {type(value)}")

        elif isinstance(j_obj, list):
            if level == 0:
                print(f"\nThe object is of type {type(j_obj)}")
            for index, item in enumerate(j_obj):
                if isinstance(item, (dict, list)):
                    print(f"\n{spaces}index = {index}: value = {type(item)}")
                    self.__line_counter(lines)
                    self.depict_struct(item, lines, level + 1)
                else:
                    print(f"{spaces}value = {type(item)}")

        else:  # Handle other data types like strings, numbers, etc.
            print(f"{spaces}value = {type(j_obj)}: {j_obj}")
            self.__line_counter(lines)

        return True

    # reads the instantiated json object and returns True or False
    # this ALMOST works - needs more testing at level 3
    def is_symmetrical(self, j_obj=None):
        """
        Checks if the given JSON object has a symmetrical structure recursively.

        Args:
        j_obj: The JSON object to check. This can be an external jSON but
        the default is the instantiated object.

        Returns:
        True if the structure is symmetrical, False otherwise.
        """

        # quick param check
        if j_obj:
            if not isinstance(j_obj, (list, dict)):
                return False
        # substitute default param
        else:
            j_obj = self.json_obj

        if isinstance(j_obj, list):
            # Check if all elements in the list have the same type
            if not j_obj:  # Empty list is considered symmetrical
                return True
            first_item_type = type(j_obj[0])
            return all(isinstance(item, first_item_type) for item in j_obj) and all(
                self.is_symmetrical(item) for item in j_obj
            )

        elif isinstance(j_obj, dict):
            # Check if all values in the dictionary have the same type
            if not j_obj:  # Empty dictionary is considered symmetrical
                return True
            first_key = next(iter(j_obj))
            first_value_type = type(j_obj[first_key])
            return all(
                isinstance(value, first_value_type) for value in j_obj.values()
            ) and all(self.is_symmetrical(value) for value in j_obj.values())

        else:
            # Base case: simple types are considered symmetrical
            return True

    # returns the number of keys in a dict and the value types
    def analyze_object(self, j_obj):
        """analyze a dict in a json object"""

        # quick param check
        if not isinstance(j_obj, dict):
            return False

        num_keys = len(j_obj)
        val_list = []

        for val in j_obj.values():
            val_list.append(type(val))

        return (num_keys, val_list)

    # returns the number of elements in a list and the value types
    def analyze_array(self, this_list):
        """analyze a list in a json object"""

        # quick param check
        if not isinstance(this_list, list):
            return False

        num_vals = len(this_list)
        val_list = []

        for val in this_list:
            val_list.append(type(val))

        return (num_vals, val_list)

    # #################### private methods ############################

    # PRIVATE - read a json data file
    # called only by __init__ (maybe others later??)
    # but should this method be public, so that any json file can be read?
    # the purpose of argonaut is to improve the productivity of json wrangling
    def __read_json_data(self, file_path):
        """Takes a file path and returns a file or an error"""

        # quick param check
        if not isinstance(file_path, Path):
            return False

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
        """takes a list of tuples and returns True or raises a TypeError"""

        for param in params:
            allowed_types = param[1]
            if not isinstance(param[0], allowed_types):
                raise TypeError(
                    f"The parameter value '{param[0]}' is not of type {allowed_types}"
                )

        return True

    # PRIVATE - manage the line count for depict_struct
    # this doesn't work perfectly: the recursion breaks the line count
    # but it works well enough for now
    def __line_counter(self, lines):
        """manage the line-count and implement pause as required"""

        # increment line count since we have just printed a line
        self.line_count += 1

        # have we breached the line limit?
        if self.line_count > lines:

            while True:
                input("Press 'Enter' to continue, or 'CTRL-C' to stop...")
                break

            self.line_count = 0
