""" declare the project global variables """

import os
import sys

# the project root string
PROJECT_ROOT = r"C:\Users\russe\Documents\Repos\GitHub\argonaut"

# the top level locations of the project
ARGO_DIR = os.path.abspath(PROJECT_ROOT)
sys.path.append(ARGO_DIR)

# project paths
ARGO_PACKAGE = os.path.join(ARGO_DIR, 'colchis')
sys.path.append(ARGO_PACKAGE)

# data folders paths
DATA_DIR = os.path.join(ARGO_DIR, "data")
sys.path.append(DATA_DIR)

# conda env paths
CONDA_PATH = r"C:\Users\russe\anaconda3\envs\bb-env"
sys.path.append(CONDA_PATH)
