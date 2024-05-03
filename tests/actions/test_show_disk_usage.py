import os
import pytest
from pro_filer.actions.main_actions import show_disk_usage

@pytest.fixture
def tmp_files(tmp_path):
    # Criando arquivos temporários
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file3 = tmp_path / "file3.txt"

    # Escrevendo dados nos arquivos
    file1.write_text("Hello")
    file2.write_text("World")
    file3.write_text("!")

    return [str(file1), str(file2), str(file3)]

def test_show_disk_usage(tmp_files, capfd):
    context = {
        "all_files": tmp_files
    }
    show_disk_usage(context)
    out, _ = capfd.readouterr()
    lines = out.strip().split("\n")
    
    assert len(lines) == 4  # Verifica se há 4 linhas (uma para cada arquivo e uma para o total size)
    assert "Total size:" in lines[-1]  # Verifica se a última linha começa com "Total size:"
    
    # Verifica se cada linha (exceto a última) possui a formatação correta
    for line in lines[:-1]:
        assert line.endswith("%)")  # Verifica se a linha termina com a porcentagem
        assert "(100%)" in line or "(0%)" in line  # Verifica se há "(100%)" ou "(0%)"

if __name__ == "__main__":
    pytest.main()
