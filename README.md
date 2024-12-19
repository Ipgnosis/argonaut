# Argonaut

A work in progress...

A package to generalize JSON traversal and processing.

See IETF RFC8259: The Javascript Object Notation (JSON) Data Interchange Format https://datatracker.ietf.org/doc/html/rfc8259

## Purpose

I seem to spend a lot of time writing code to perform operations on a JSON structure. I wonder if I can automate this?

### The minimum goal is a package that does the 'heavy lifting':

- Reduce duplication of effort
- Maximize performance
- Minimize coding errors
- Minimize coding effort

## Import:
import os
from pathlib import Path
import config
from colchis.classes.argo import Argo


## Instantiate:

x = Argo(file_path)
where file_path is the valid path to a valid JSON file
