# app.py for argonaut

import config, modify

from colchis.classes.argo import Argo

file_obj = Argo(config.DATA_FILE_PATH)

print(file_obj.filePath)
print(file_obj.jFile)
