from pro_filer.actions.main_actions import find_duplicate_files
import pytest

@pytest.fixture
def create_temp_files(tmp_path):
    file1_content = b"Content of file 1"
    file2_content = b"Content of file 2"

    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"

    with open(file1, "wb") as f1, open(file2, "wb") as f2:
        f1.write(file1_content)
        f2.write(file2_content)

    return str(file1), str(file2)

def test_find_duplicate_files_different_content(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"

    with open(file1, "w") as f1, open(file2, "w") as f2:
        f1.write("Content of file 1")
        f2.write("Different content for file 2")

    context = {"all_files": [str(file1), str(file2)]}

    assert find_duplicate_files(context) == []

def test_find_duplicate_files_same_content(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"

    content = "Same content for both files"

    with open(file1, "w") as f1, open(file2, "w") as f2:
        f1.write(content)
        f2.write(content)

    context = {"all_files": [str(file1), str(file2)]}

    assert find_duplicate_files(context) == [(str(file1), str(file2))]

def test_find_duplicate_files_missing_file(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"

    with open(file1, "w") as f1:
        f1.write("Content of file 1")

    context = {"all_files": [str(file1), str(file2)]}

    with pytest.raises(ValueError):
        find_duplicate_files(context)
