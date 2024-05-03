from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from pro_filer.cli_helpers import _get_printable_file_path


def test_show_disk_usage(tmp_path, capsys):
    file_1 = tmp_path / "file_test1.txt"
    with open(file_1, "w") as f:
        f.write("GABIGOL VOLTOU")
    print_1 = f"'{_get_printable_file_path(str(file_1))}':".ljust(70)

    file_2 = tmp_path / "file_test2.txt"
    with open(file_2, "w") as f:
        f.write("MAS AINDA NÃO FEZ GOL")
    print_2 = f"'{_get_printable_file_path(str(file_2))}':".ljust(70)

    context = {"all_files": [str(file_1), str(file_2)]}
    show_disk_usage(context)
    captured = capsys.readouterr()
    expected_out = (
        f"{print_2} 22 (61%)\n{print_1} 14 (38%)\nTotal size: 36\n"
    )
    assert captured.out == expected_out

    context_2 = {"all_files": []}
    show_disk_usage(context_2)
    captured_2 = capsys.readouterr()
    assert captured_2.out == "Total size: 0\n"
