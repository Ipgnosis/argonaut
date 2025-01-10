# Colchis

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

## Approach

An arbitrary JSON file is:

* Has a read path (and potentially a write path)

* Either valid or invalid

* Is either an object or a list

* Is updated after instantiation or not

* Has either a uniform or non-uniform structure

**All** other considerations are file structure dependent.  Therefore, methods that are dependent on structure and contents should be implemented within *child* classes, e.g.:

* fetch higher level data objects

* add / update / delete data

## Imports

* import os

* from pathlib import Path

* import config

## Instantiation

x = Argo(file_path)

Where file_path is the valid path to a valid JSON file; 'x' is the class object of the json file

## Methods Implemented

__init__: sets:
    file_path
    json_obj
    obj_struct
    line_count

write_json_data

validate_json_data

print_json

depict_struct

is_symmetrical

analyze_object

analyze_array

__read_json_data

__good_params

__line_counter

## Methods awaiting implementation

__show_non_uniformity

## Background
**Jason** was a character in Greek mythology.  He set off on a quest in a ship (the **Argo**), with a crew (the **Argonauts**) to a foreign land (**Colchis**, present day Georgia) to recover a legendary **Golden Fleece** in order to regain his rightful throne.  To gain the Golden Fleece, he was assigned several arduous tasks, which he *completed* though divine intervention.  Despite his triumph, Jason continued to encounter serious problems in life and ultimately died a poor man while asleep under the rotting Argo, which fell and killed him.  Hopefully, history doesn't repeat itself.
