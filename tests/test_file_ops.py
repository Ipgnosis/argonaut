"""Tests for colchis.file_ops."""

from colchis import file_ops


def test_delete_file(tmp_path):
    target = tmp_path / "a.txt"
    target.write_text("x", encoding="utf-8")
    assert file_ops.delete_file(target) is True
    assert not target.exists()


def test_delete_file_missing_returns_false(tmp_path):
    assert file_ops.delete_file(tmp_path / "missing.txt") is False


def test_rename_file(tmp_path):
    src = tmp_path / "a.txt"
    dst = tmp_path / "b.txt"
    src.write_text("x", encoding="utf-8")
    assert file_ops.rename_file(src, dst) is True
    assert not src.exists()
    assert dst.exists()


def test_move_files(tmp_path):
    src_dir = tmp_path / "src"
    dst_dir = tmp_path / "dst"
    src_dir.mkdir()
    (src_dir / "a.txt").write_text("x", encoding="utf-8")

    assert file_ops.move_files(src_dir, dst_dir) is True
    assert (dst_dir / "a.txt").exists()
    assert not (src_dir / "a.txt").exists()


def test_move_files_missing_source_returns_false(tmp_path):
    assert file_ops.move_files(tmp_path / "missing", tmp_path / "dst") is False


def test_copy_all_files(tmp_path):
    src_dir = tmp_path / "src"
    dst_dir = tmp_path / "dst"
    src_dir.mkdir()
    (src_dir / "a.txt").write_text("x", encoding="utf-8")

    assert file_ops.copy_all_files(src_dir, dst_dir) is True
    assert (src_dir / "a.txt").exists()  # copy, not move
    assert (dst_dir / "a.txt").exists()


def test_copy_all_files_missing_source_returns_false(tmp_path):
    assert file_ops.copy_all_files(tmp_path / "missing", tmp_path / "dst") is False


def test_delete_all_files(tmp_path):
    # regression test: delete_all_files used to pass bare filenames to
    # delete_file instead of joining them with `this_path`, so it silently
    # deleted nothing unless the caller's CWD happened to match this_path.
    (tmp_path / "a.txt").write_text("x", encoding="utf-8")
    (tmp_path / "b.txt").write_text("y", encoding="utf-8")

    assert file_ops.delete_all_files(tmp_path) is True
    assert list(tmp_path.iterdir()) == []


def test_delete_all_files_missing_dir_returns_false(tmp_path):
    assert file_ops.delete_all_files(tmp_path / "missing") is False
