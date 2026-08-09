"""Tests for colchis.argo.Argo."""

import json

import pytest

from colchis.argo import Argo


def write_json(path, data):
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


@pytest.fixture
def uniform_dict_path(tmp_path):
    return write_json(tmp_path / "uniform_dict.json", {"a": 1, "b": 2, "c": 3})


@pytest.fixture
def non_uniform_dict_path(tmp_path):
    return write_json(tmp_path / "non_uniform_dict.json", {"a": 1, "b": "two", "c": [3]})


@pytest.fixture
def uniform_list_path(tmp_path):
    return write_json(tmp_path / "uniform_list.json", [1, 2, 3])


def test_init_requires_a_path_object(tmp_path):
    with pytest.raises(TypeError):
        Argo(str(tmp_path / "uniform_dict.json"))


def test_init_loads_the_file(uniform_dict_path):
    obj = Argo(uniform_dict_path)
    assert obj.json_obj == {"a": 1, "b": 2, "c": 3}
    assert obj.file_path == uniform_dict_path


def test_init_returns_none_for_missing_file(tmp_path):
    obj = Argo(tmp_path / "does-not-exist.json")
    assert obj.json_obj is None


def test_write_json_data_round_trips(uniform_dict_path, tmp_path):
    obj = Argo(uniform_dict_path)
    out_path = tmp_path / "written.json"
    assert obj.write_json_data(file_path=out_path, wdata={"x": 1}) is True
    assert json.loads(out_path.read_text(encoding="utf-8")) == {"x": 1}


def test_write_json_data_uses_instance_defaults(uniform_dict_path):
    obj = Argo(uniform_dict_path)
    obj.json_obj = {"changed": True}
    assert obj.write_json_data() is True
    assert json.loads(uniform_dict_path.read_text(encoding="utf-8")) == {"changed": True}


def test_validate_json_data_on_instance_object(uniform_dict_path):
    obj = Argo(uniform_dict_path)
    assert obj.validate_json_data() is True


def test_validate_json_data_rejects_non_list_dict(uniform_dict_path):
    obj = Argo(uniform_dict_path)
    assert obj.validate_json_data("not a list or dict") is False


def test_print_json_returns_true_for_valid_object(uniform_dict_path, capsys):
    obj = Argo(uniform_dict_path)
    assert obj.print_json() is True
    assert "\"a\": 1" in capsys.readouterr().out


def test_print_json_returns_false_for_invalid_object(uniform_dict_path):
    obj = Argo(uniform_dict_path)
    assert obj.print_json("not a list or dict") is False


def test_depict_struct_does_not_block_on_small_structures(uniform_dict_path):
    # keep well under the default `lines=10` pagination threshold so the
    # blocking input() prompt in Argo.__line_counter never triggers.
    obj = Argo(uniform_dict_path)
    assert obj.depict_struct() is True


def test_is_symmetrical_true_for_uniform_dict(uniform_dict_path):
    obj = Argo(uniform_dict_path)
    assert obj.is_symmetrical() is True


def test_is_symmetrical_false_for_non_uniform_dict(non_uniform_dict_path):
    obj = Argo(non_uniform_dict_path)
    assert obj.is_symmetrical() is False


def test_is_symmetrical_true_for_uniform_list(uniform_list_path):
    obj = Argo(uniform_list_path)
    assert obj.is_symmetrical() is True


def test_is_symmetrical_handles_empty_containers(uniform_dict_path):
    obj = Argo(uniform_dict_path)
    assert obj.is_symmetrical({}) is True
    assert obj.is_symmetrical([]) is True


def test_analyze_object(uniform_dict_path):
    obj = Argo(uniform_dict_path)
    num_keys, val_types = obj.analyze_object({"a": 1, "b": "two"})
    assert num_keys == 2
    assert val_types == [int, str]


def test_analyze_array(uniform_dict_path):
    obj = Argo(uniform_dict_path)
    num_vals, val_types = obj.analyze_array([1, "two", 3.0])
    assert num_vals == 3
    assert val_types == [int, str, float]
