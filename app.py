""" test file for argonaut """

import os
from pathlib import Path
import config
from colchis.classes.argo import Argo

FILE_NAME = "owid-covid-data.json"
WRITE_FILE = "erase-this.json"

file_path = Path(os.path.join(config.DATA_DIR, FILE_NAME))
write_path = Path(os.path.join(config.DATA_DIR, WRITE_FILE))


json_obj = Argo(file_path)
# json_obj = Argo(FILE_NAME)


json_obj.write_json_data(write_path, json_obj, 'w')

print(json_obj.file_path)
print(json_obj.json_obj)
