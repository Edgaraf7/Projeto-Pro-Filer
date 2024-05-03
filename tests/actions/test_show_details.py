from datetime import date
import pytest
from pro_filer.actions.main_actions import show_details


def test_show_details_existing_file(capfd):
    context = {
        "base_path": "/home/trybe/Downloads/Trybe_logo.png"
    }
    show_details(context)
    out, _ = capfd.readouterr()
    assert "File name: Trybe_logo.png" in out
    assert "File size in bytes" in out
    assert "File type: file" in out
    assert "File extension: .png" in out
    assert "Last modified date:" in out


def test_show_details_nonexistent_file(capfd):
    context = {
        "base_path": "/home/trybe/????"
    }
    show_details(context)
    out, _ = capfd.readouterr()
    assert "File '????' does not exist" in out


def test_show_details_directory(capfd):
    context = {
        "base_path": "/home/trybe/Documents"
    }
    show_details(context)
    out, _ = capfd.readouterr()
    assert "File type: directory" in out


def test_show_details_no_extension(capfd):
    context = {
        "base_path": "/home/trybe/Downloads/README"
    }
    show_details(context)
    out, _ = capfd.readouterr()
    assert "File extension: [no extension]" in out


def test_show_details_date_format(capfd):
    context = {
        "base_path": "/home/trybe/Downloads/Trybe_logo.png"
    }
    show_details(context)
    out, _ = capfd.readouterr()
    date_str = out.split("Last modified date: ")[1].strip()
    try:
        date.fromisoformat(date_str)
        assert True
    except ValueError:
        assert False, "Date format is incorrect"


if __name__ == "__main__":
    pytest.main()
