""" test file for argonaut """

import os
from pathlib import Path
from colchis import Argo
import config
f


# TEST_NAME = "owid-covid-data.json"
# TEST_NAME = "city_list.json"
# TEST_NAME = "countries_with_priorities.json"

FILE_NAME = "countries_with_priorities.json"
# FILE_NAME = "belgium.json"

# WRITE_FILE = "delete-this.json"

file_path = Path(os.path.join(config.DATA_DIR, FILE_NAME))
# test_path = Path(os.path.join(config.DATA_DIR, TEST_NAME))
# write_path = Path(os.path.join(config.DATA_DIR, WRITE_FILE))

json_obj = Argo(file_path)
# json_obj = Argo(test_path)


# test_obj = read_json_data(test_path)
# json_obj.validate_json_data(test_obj)

# print(f"argo init: {json_obj.obj_struct}")
# print(json_obj.find_element("country", "Colombia", "time_zones"))

# json_obj.write_json_data(write_path, json_obj.json_obj, 'w')

# json_obj.print_json(test_obj)
# json_obj.print_json()

json_obj.depict_struct()
# json_obj.depict_struct(test_obj, 1)
# json_obj.print_json(test_obj)


# print(json_obj.file_path)
# print(json_obj.json_obj)
