# modify the globals

import config
import os, sys
from pathlib import Path

config.CURRENT_DIR_STR = os.path.abspath('')
config.DATA_FILE_STR = os.path.join(config.CURRENT_DIR_STR, 'data', data_file_name)
config.ARGO_PACKAGE_STR = os.path.join(config.CURRENT_DIR_STR, 'colchis')
config.DATA_FILE_PATH = Path(config.DATA_FILE_STR)
sys.path.append(config.DATA_FILE_PATH)
config.ARGO_PACKAGE_PATH = Path(config.ARGO_PACKAGE_STR)
sys.path.append(config.ARGO_PACKAGE_PATH)
