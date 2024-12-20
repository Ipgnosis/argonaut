# Argonaut

A work in progress...

A package, implemented as a Class, to generalize JSON traversal and processing.

See IETF RFC8259: The Javascript Object Notation (JSON) Data Interchange Format https://datatracker.ietf.org/doc/html/rfc8259

## Purpose

I seem to spend a lot of time writing code to perform operations on a JSON structure. I wonder if I can automate this?

### The minimum goal is a package that does the 'heavy lifting':

- Reduce duplication of effort
- Maximize compute performance
- Minimize coding errors
- Minimize coding effort

## Imports
import os

from pathlib import Path

import config

from colchis.classes.argo import Argo

## Instantiation

x = Argo(file_path)

Where file_path is the valid path to a valid JSON file; 'x' is the class object of the json file

## Methods Implemented

write_json_data

validate_json_data

depict_json

depict_struct

__read_json_data

__good_params

## Methods awaiting implementation

create_key_list

create_value_list

add_key_value

delete_key_value

update_key

update_value

find_key

find_value

find_except

find_element

delete_element

update_element

append_element

insert_element

## Background
**Jason** was a character in Greek mythology.  He set off on a quest in a ship (the **Argo**), with a crew (the **Argonauts**) to a foreign land (**Colchis**, present day Georgia) to recover a legendary **Golden Fleece** in order to regain his rightful throne.  To gain the Golden Fleece, he was assigned arduous tasks, which he *completed* though divine intervention.  Despite his triumph, Jason continued to encounter serious problems in life and ultimately died a poor man while asleep under the rotting Argo, which fell and killed him.
