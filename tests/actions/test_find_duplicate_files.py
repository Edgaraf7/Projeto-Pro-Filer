import pytest
import os
import tempfile
from pro_filer.actions.main_actions import find_duplicate_files


@pytest.fixture
def create_temp_files():
    temp_dir = tempfile.mkdtemp()
    files = [
        "file1.txt",
        "file2.txt",
        "file3.txt"
    ]
    for file in files:
        file_path = os.path.join(temp_dir, file)
        with open(file_path, "w") as f:
            f.write("Test content")
    return temp_dir


def test_no_duplicate_files(create_temp_files):
    files = [
        os.path.join(create_temp_files, "file1.txt"),
        os.path.join(create_temp_files, "file2.txt"),
        os.path.join(create_temp_files, "file3.txt")
    ]
    context = {"all_files": files}
    assert find_duplicate_files(context) == []


def test_all_duplicate_files(create_temp_files):
    files = [
        os.path.join(create_temp_files, "file1.txt"),
        os.path.join(create_temp_files, "file2.txt"),
        os.path.join(create_temp_files, "file3.txt")
    ]
    context = {"all_files": files * 2}  # Duplicate all files
    expected_result = [
        (files[0], files[3]),
        (files[1], files[4]),
        (files[2], files[5])
    ]
    assert find_duplicate_files(context) == expected_result


def test_some_duplicate_files(create_temp_files):
    files = [
        os.path.join(create_temp_files, "file1.txt"),
        os.path.join(create_temp_files, "file2.txt"),
        os.path.join(create_temp_files, "file3.txt")
    ]
    context = {"all_files": files[:2] + files[1:]}  # Duplicate file2
    expected_result = [
        (files[0], files[1]),
        (files[1], files[2])
    ]
    assert find_duplicate_files(context) == expected_result


def test_missing_files():
    files = [
        "nonexistent_file1.txt",
        "nonexistent_file2.txt"
    ]
    context = {"all_files": files}
    with pytest.raises(ValueError):
        find_duplicate_files(context)
