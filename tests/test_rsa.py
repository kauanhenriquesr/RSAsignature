import pytest
from src import criptografa, descriptografa, criptografa_mensagem, descriptografa_mensagem, gera_chave

def test_criptografa_e_descriptografa():
    n, e, d = gera_chave()
    criptografado = criptografa(1234567890, n, e)
    assert descriptografa(criptografado, n, d) == 1234567890

def test_criptografa_mensagem_e_descriptografa_mensagem():
    n, e, d = gera_chave()
    mensagem = "Hello, World!"
    criptografado = criptografa_mensagem(mensagem, n, e)
    assert descriptografa_mensagem(criptografado, n, d) == mensagem
