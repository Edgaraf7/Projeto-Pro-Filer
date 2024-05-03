from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


def test_find_duplicate_files(tmp_path):
    files = []
    file_1 = tmp_path / "file_test1.txt"
    with open(file_1, "w") as f:
        f.write("Edgar Web Developer")

    file_2 = tmp_path / "file_test2.txt"
    with open(file_2, "w") as f:
        f.write("Primeiro Sim")

    file_2_2 = tmp_path / "file_test2_2.txt"
    with open(file_2_2, "w") as f:
        f.write("Primeiro sim Internacional")

    files.append(str(file_1))
    files.append(str(file_2))
    files.append(str(file_2_2))
    to_check = find_duplicate_files({"all_files": files})
    assert len(to_check) == 1
    assert len(to_check[0]) == 2

    files.append("inexistent_file.txt")
    with pytest.raises(ValueError, match="All files must exist"):
        to_check = find_duplicate_files({"all_files": files})
