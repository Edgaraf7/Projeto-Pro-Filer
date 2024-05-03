from pro_filer.actions.main_actions import show_details
import os
from datetime import date


def test_show_details(tmp_path, capsys):
    file_path = tmp_path / "file.txt"
    with open(file_path, "w") as file:
        file.write("GABIGOL VAI CRAVAR HOJE")
    context = {"base_path": str(file_path)}
    show_details(context)
    captured = capsys.readouterr()
    expected_output = (
        f"File name: file.txt\n"
        f"File size in bytes: 23\n"
        f"File type: file\n"
        f"File extension: .txt\n"
        f"""Last modified date: {
            date.fromtimestamp(os.path.getmtime(str(file_path)))
            }\n"""
    )
    assert captured.out.strip() == expected_output.strip()


def test_show_details_without_extension(tmp_path, capsys):
    file_path = tmp_path / "without_extension"
    with open(file_path, "w") as file:
        file.write("GABIGOL SE LESIONOU")
    context = {"base_path": str(file_path)}
    show_details(context)
    captured = capsys.readouterr()
    expected_output = (
        f"File name: without_extension\n"
        f"File size in bytes: 19\n"
        f"File type: file\n"
        f"File extension: [no extension]\n"
        f"""Last modified date: {
            date.fromtimestamp(os.path.getmtime(str(file_path)))
            }\n"""
    )
    assert captured.out.strip() == expected_output.strip()


def test_show_details_file_not_found(capsys):
    context = {"base_path": "/path/to/none/file_not_found"}
    show_details(context)
    captured = capsys.readouterr()
    expected_output = "File 'file_not_found' does not exist\n"
    assert captured.out.strip() == expected_output.strip()
