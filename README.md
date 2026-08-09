# Argonaut

A small module, built around one class (`Argo`), for loading, validating, pretty-printing, and inspecting the structure of a JSON file — the boilerplate around `json.load`/`json.dumps`/`pprint` that ends up rewritten in every script that touches JSON.

Ships as two flat modules (`argo`, `file_ops`) — no package wrapper, no PyPI publishing — meant for pulling into other repos with a plain editable/git install and importing directly, e.g. `from argo import Argo`.

See IETF RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format — <https://datatracker.ietf.org/doc/html/rfc8259>

## What this is (and isn't)

`Argo` is intentionally thin: load a JSON file, check it's valid, print it, inspect its structure and type-uniformity. It is **not** a general JSON query/traversal/diffing engine — for querying, reach for [`jmespath`](https://jmespath.org/) or [`glom`](https://glom.readthedocs.io/); for schema validation, [`pydantic`](https://docs.pydantic.dev/) or [`jsonschema`](https://python-jsonschema.readthedocs.io/); for structural diffing, [`deepdiff`](https://zepworks.com/deepdiff/); for richer pretty-printing, [`rich`](https://rich.readthedocs.io/). See `docs/DECISIONS.md` (2026-08-09) for why this project stays scoped rather than growing into a reimplementation of any of those.

## Install

```bash
pip install -e .
```

(from the repo root, into whatever environment needs it — this repo's own default dev environment is the `bb-env` conda environment, see `CLAUDE.md`. From another repo: `pip install git+https://github.com/Ipgnosis/argonaut.git`, or a local editable install pointed at this repo's path.)

## Usage

```python
from pathlib import Path
from argo import Argo

obj = Argo(Path("data/example.json"))

obj.validate_json_data()          # -> bool
obj.print_json()                  # pretty-prints to stdout
obj.depict_struct()               # prints a type-annotated structure diagram
obj.is_symmetrical()              # -> bool: is every level of the structure type-uniform?
obj.analyze_object(obj.json_obj)  # -> (num_keys, [value types])
obj.write_json_data()             # writes self.json_obj back to self.file_path
```

Most methods accept an optional external JSON object (`j_obj`) instead of operating on the instantiated file, so the same logic works on ad hoc structures too.

## File-management helpers

`file_ops` has a few standalone functions (`delete_file`, `rename_file`, `move_files`, `delete_all_files`, `copy_all_files`) that aren't JSON-specific and don't belong on `Argo`.

## Development

```bash
pytest          # run the test suite
ruff check .    # lint
mypy src        # type-check
```

## Background

**Jason** (JSON... ) was a character in Greek mythology.  He set off on a quest in a ship (the **Argo**), with a crew (the **Argonauts**) to a foreign land (**Colchis**, present day Georgia) to recover a legendary **Golden Fleece** in order to assert his claim to his father's throne.  To gain the Golden Fleece, he was assigned several arduous tasks, which he completed though divine intervention.  Despite his triumph, Jason continued to encounter serious problems in life and ultimately died a poor man while asleep under the rotting Argo, which fell and killed him.  Hopefully, 'history' doesn't repeat itself.
