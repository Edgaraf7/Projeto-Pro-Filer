from pro_filer.actions.main_actions import show_details
from datetime import date
import pytest


@pytest.mark.parametrize(
    "base_path, expected_output",
    [
        (
            "/home/trybe/Downloads/Trybe_logo.png",
            "File name: Trybe_logo.png\n"
            "File size in bytes: 22438\n"
            "File type: file\n"
            "File extension: .png\n"
            f"Last modified date: {date.fromisoformat('2023-06-13')}\n"
        ),
        (
            "/home/trybe/????",
            "File '????' does not exist\n"
        ),
        (
            "/home/trybe/Downloads",
            "File name: Downloads\n"
            "File size in bytes: 4096\n"
            "File type: directory\n"
            "[no extension]\n"
            f"Last modified date: {date.fromisoformat('2023-06-13')}\n"
        ),
    ]
)
def test_show_details(base_path, expected_output, capsys):
    context = {"base_path": base_path}
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == expected_output
