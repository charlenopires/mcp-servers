"""
Testes para o servidor mcpprompt_server.py
"""

import pytest
import sys
import os

# Adicionar o diretório pai ao path para importar os servidores
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def test_mcpprompt_server_exists():
    """Testa se o arquivo mcpprompt_server.py existe."""
    server_path = os.path.join(os.path.dirname(
        __file__), '..', 'servers', 'mcpprompt_server.py')
    assert os.path.exists(
        server_path), "Arquivo mcpprompt_server.py não encontrado"


def test_mcpprompt_server_is_readable():
    """Testa se o arquivo mcpprompt_server.py pode ser lido."""
    server_path = os.path.join(os.path.dirname(
        __file__), '..', 'servers', 'mcpprompt_server.py')
    with open(server_path, 'r', encoding='utf-8') as f:
        content = f.read()
    assert isinstance(
        content, str), "Não foi possível ler o conteúdo do arquivo"
    assert len(content) > 0, "Arquivo mcpprompt_server.py está vazio"


def test_mcpprompt_server_has_docstring():
    """Testa se o arquivo mcpprompt_server.py tem uma docstring."""
    server_path = os.path.join(os.path.dirname(
        __file__), '..', 'servers', 'mcpprompt_server.py')
    with open(server_path, 'r', encoding='utf-8') as f:
        content = f.read()
    assert '"""' in content, "Arquivo mcpprompt_server.py deve ter uma docstring"


if __name__ == "__main__":
    pytest.main([__file__])
