"""class definition for Argo
takes one param on instantiation:
    json_path: the path to the json file being processed

where possible, type checking is performed on parameters

there are also some methods that are public that will work on separate
(non-instantiated) json structures: this is intentional to aid development
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Literal

# NOTE: a JSON object/array is written out in full (`dict[str, Any] | list[Any]`)
# at every use below rather than factored into a named type alias - not a
# fully recursive JSON type either, which Python's type system handles
# awkwardly for little practical benefit here (nested values are still real
# JSON, just typed as Any at that depth). A named alias was tried and
# reverted: Pylance strict mode reported `reportUnknownVariableType` on the
# alias itself even with an explicit `TypeAlias` annotation (a known Pyright
# rough edge for this exact pattern), cascading into every signature that
# used it. Writing the union inline sidesteps the ambiguity entirely.


# the class definition for argonaut (aka colchis)
# see the README
class Argo:
    """a class to facilitate json object operations and reduce development effort"""

    # instantiate
    def __init__(self, json_path: Path) -> None:
        if not isinstance(json_path, Path):
            raise TypeError(
                f"The json_path parameter must be a Path object, not {type(json_path)}"
            )

        print(f"\nInstantiating '{json_path}' as an Argo object.")

        # create global objects
        self.file_path: Path = json_path

        # load the json file
        self.json_obj: dict[str, Any] | list[Any] | None = self.__read_json_data(
            self.file_path
        )

        # this is a 'global' for depict_struct
        self.line_count: int = 0

    # write a json data file
    def write_json_data(
        self,
        file_path: Path | None = None,
        wdata: dict[str, Any] | list[Any] | None = None,
        mode: Literal["w", "a"] = "w",
    ) -> bool:
        """Takes a file path, data, write mode and writes data to the file"""

        # insert the default params
        if file_path is None:
            file_path = self.file_path

        if wdata is None:
            wdata = self.json_obj

        if mode is None:
            mode = "w"

        try:
            with open(file_path, mode, encoding="utf-8") as outfile:
                json.dump(wdata, outfile, indent=4, ensure_ascii=False)
            return True  # The file is automatically closed when the 'with' block ends
        except TypeError as e:
            print(f"{e}: data is not valid JSON")
            return False
        except OSError as error:
            print(f"{error}: file {file_path} cannot be saved")
            return False

    # validate an external json object
    # node that self.json_obj is pre-validated
    def validate_json_data(
        self, j_obj: dict[str, Any] | list[Any] | None = None
    ) -> bool:
        """developer productivity feature: check the validity of a json object"""

        # this gives the option of sending a random dict
        # no param means use the instantiated object
        if j_obj is None:
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
        except (json.decoder.JSONDecodeError, TypeError) as e:
            print(f"Invalid JSON syntax: {e}")
            return False

    # print out the file to the terminal with indentation
    def print_json(self, j_obj: dict[str, Any] | list[Any] | None = None) -> bool:
        """developer feature to show the object contents"""

        # this gives the option of sending a random dict
        # no param means use the instantiated object
        if j_obj is None:
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
    def depict_struct(
        self,
        j_obj: dict[str, Any] | list[Any] | None = None,
        lines: int = 10,
        level: int = 0,
    ) -> bool:
        """developer productivity feature to show a json object structure
        recursive function...
        params:
            j_obj: valid json string
            lines: the required number of lines for output
            level: the current indentation level - used by recursive calls
        """

        # this gives the option of sending a random dict
        # no param means use the instantiated object
        if j_obj is None:
            j_obj = self.json_obj
            # reset the line_count to zero at the first invocation
            self.line_count = 0
            print(f"Structure diagram for {self.file_path}:")

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

    def is_symmetrical(self, j_obj: Any | None = None) -> bool:
        """
        Checks if the given JSON object has a symmetrical structure recursively.

        Args:
        j_obj: The JSON object to check. This can be an external jSON but
        the default is the instantiated object.

        Returns:
        True if the structure is symmetrical, False otherwise.
        """

        # substitute default param - explicit `is None` (not truthiness) so
        # a falsy-but-real external value (0, "", [], {}) isn't mistaken for
        # "no param given". The recursive traversal itself never re-applies
        # this substitution (see __is_symmetrical_recursive), so a scalar
        # leaf value encountered during recursion (including a falsy one)
        # is handled by the base case below rather than looping back here.
        if j_obj is None:
            j_obj = self.json_obj

        return self.__is_symmetrical_recursive(j_obj)

    # PRIVATE - the actual recursive traversal behind is_symmetrical
    def __is_symmetrical_recursive(self, j_obj: Any) -> bool:
        # ignore the redundant "remove unnecessary elif" hint
        if isinstance(j_obj, list):
            # Check if all elements in the list have the same type
            if not j_obj:  # Empty list is considered symmetrical
                return True
            first_item_type = type(j_obj[0])
            return all(isinstance(item, first_item_type) for item in j_obj) and all(
                self.__is_symmetrical_recursive(item) for item in j_obj
            )

        elif isinstance(j_obj, dict):
            # Check if all values in the dictionary have the same type
            if not j_obj:  # Empty dictionary is considered symmetrical
                return True
            first_key = next(iter(j_obj))
            first_value_type = type(j_obj[first_key])
            return all(
                isinstance(value, first_value_type) for value in j_obj.values()
            ) and all(
                self.__is_symmetrical_recursive(value) for value in j_obj.values()
            )

        else:
            # Base case: simple types (including a falsy one, or a JSON
            # `null` recursed into as Python None) are considered symmetrical
            return True

    # returns the number of keys in a dict and the value types
    def analyze_object(self, j_obj: dict[str, Any]) -> tuple[int, list[type[Any]]]:
        """analyze a dict in a json object"""

        num_keys = len(j_obj)
        val_list: list[type[Any]] = []

        for val in j_obj.values():
            val_list.append(type(val))

        return (num_keys, val_list)

    # returns the number of elements in a list and the value types
    def analyze_array(self, this_list: list[Any]) -> tuple[int, list[type[Any]]]:
        """analyze a list in a json object"""

        num_vals = len(this_list)
        val_list: list[type[Any]] = []

        for val in this_list:
            val_list.append(type(val))

        return (num_vals, val_list)

    # #################### private methods ############################

    # PRIVATE - read a json data file
    # called only by __init__ (maybe others later??)
    # but should this method be public, so that any json file can be read?
    # the purpose of argonaut is to improve the productivity of json wrangling.
    def __read_json_data(self, file_path: Path) -> dict[str, Any] | list[Any] | None:
        """Takes a file path and returns a file or an error"""

        try:
            with open(file_path, encoding="utf-8") as json_file:
                return json.load(json_file)
            # The file is automatically closed when the 'with' block ends
        except json.decoder.JSONDecodeError as e:
            print(f"{e}: file {file_path} is not valid JSON")
            return None
        except OSError as error:
            print(f"{error}: File {file_path} cannot be read")
            return None

    # PRIVATE - manage the line count for depict_struct
    # this doesn't work perfectly, but it works well enough for now
    def __line_counter(self, lines: int) -> None:
        """manage the line-count and implement pause as required"""

        # increment line count since we have just printed a line
        self.line_count += 1

        # have we breached the line limit?
        if self.line_count >= lines:

            # break for reading
            while True:
                input("Press 'Enter' to continue, or 'CTRL-C' to stop...")
                break

            # reset line count
            self.line_count = 0
