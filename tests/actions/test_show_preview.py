from pro_filer.actions.main_actions import show_preview


def test_show_preview_with_files_and_dirs(capsys):
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
            "src/utils/helpers.py",
            "src/utils/constants.py",
            "src/utils/config.py"
        ],
        "all_dirs": [
            "src",
            "src/utils"
        ]
    }

    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == (
        "Found 6 files and 2 directories\n"
        "First 5 files: ['src/__init__.py', 'src/app.py', "
        "'src/utils/__init__.py', 'src/utils/helpers.py', "
        "'src/utils/constants.py']\n"
        "First 5 directories: ['src', 'src/utils']\n"
    )


def test_show_preview_with_empty_files_and_dirs(capsys):
    context = {
        "all_files": [],
        "all_dirs": []
    }

    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == "Found 0 files and 0 directories\n"
