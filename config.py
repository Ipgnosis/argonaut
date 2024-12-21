""" declare the colchis project global variables """

import os
import sys

# create a project root for colchis
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
COLCHIS_PACKAGE = PROJECT_ROOT  # argonaut is the distributable package

if COLCHIS_PACKAGE not in sys.path:  # Avoid adding multiple times
    sys.path.insert(0, COLCHIS_PACKAGE)  # Add to Python path

# Add DATA_DIR to sys.path for file access
DATA_DIR = os.path.join(COLCHIS_PACKAGE, "data")
