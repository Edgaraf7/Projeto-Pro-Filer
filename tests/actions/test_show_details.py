from pro_filer.actions.main_actions import show_details
from datetime import date
import os


def test_show_details_existing_file(capsys):
    file_path = "/home/trybe/Downloads/Trybe_logo.png"
    file_name = "Trybe_logo.png"
    file_size = os.path.getsize(file_path)
    file_extension = ".png"
    last_modified_date = date.fromtimestamp(
        os.path.getmtime(file_path)
    )

    context = {
        "base_path": file_path
    }

    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == (
        f"File name: {file_name}\n"
        f"File size in bytes: {file_size}\n"
        "File type: file\n"
        f"File extension: {file_extension}\n"
        "Last modified date: "
        f"{last_modified_date}\n"
    )


def test_show_details_non_existing_file(capsys):
    file_path = "/home/trybe/Downloads/Non_existing_file.txt"
    file_name = "Non_existing_file.txt"

    context = {
        "base_path": file_path
    }

    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == f"File '{file_name}' does not exist\n"


def test_show_details_directory(capsys):
    dir_path = "/home/trybe/Downloads"
    dir_name = "Downloads"

    context = {
        "base_path": dir_path
    }

    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == (
        f"File name: {dir_name}\n"
        "File size in bytes: 4096\n"
        "File type: directory\n"
        "[no extension]\n"
        "Last modified date: "
        f"{date.fromtimestamp(os.path.getmtime(dir_path))}\n"
    )
