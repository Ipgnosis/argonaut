""" declare the colchis project global variables """

import os
import sys

print("This is the config.py from colchis")

# create a project root for colchis
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
COLCHIS_PACKAGE = PROJECT_ROOT  # colchis is the distributable package

if COLCHIS_PACKAGE not in sys.path:  # Avoid adding multiple times
    sys.path.insert(0, COLCHIS_PACKAGE)  # Add to Python path
