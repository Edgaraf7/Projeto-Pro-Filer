from pro_filer.actions.main_actions import show_details
import os
from datetime import date


def test_show_details(dir, capsys):
    context = {"base_path": dir}
    show_details(context)
    captured = capsys.readouterr()
    expected_output = (
        f"File name: file.txt\n"
        f"File size in bytes: 23\n"
        f"File type: file\n"
        f"File extension: .txt\n"
        f"Last modified date: {date.fromtimestamp(os.path.getmtime(dir))}\n"
    )
    assert captured.out.strip() == expected_output.strip()


def test_show_details_without_extension(tmp_path, capsys):
    file = tmp_path / "without_extension"
    file.write_text("GABIGOL SE LESIONOU")
    context = {"base_path": str(file)}
    show_details(context)
    captured = capsys.readouterr()
    expected_output = (
        f"File name: without_extension\n"
        f"File size in bytes: 19\n"
        f"File type: file\n"
        f"File extension: [no extension]\n"
        f"""Last modified date: {
            date.fromtimestamp(os.path.getmtime(str(file)))
            }\n"""
    )
    assert captured.out.strip() == expected_output.strip()


def test_show_details_file_not_found(capsys):
    context = {"base_path": "/path/to/none/file_not_found"}
    show_details(context)
    captured = capsys.readouterr()
    expected_output = "File 'file_not_found' does not exist\n"
    assert captured.out.strip() == expected_output.strip()
