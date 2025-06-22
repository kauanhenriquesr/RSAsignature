import pytest
from src.rsa import criptografa_rsa, descriptografa_rsa, gera_chave

def test_criptografa_e_descriptografa():
    n, e, d = gera_chave()
    criptografado = criptografa_rsa(1234567890, n, e)
    assert descriptografa_rsa(criptografado, n, d) == 1234567890

def test_criptografa_e_descriptografa2():
    n, e, d = gera_chave()
    mensagem = "Hello, World!"
    for char in mensagem:
        criptografado = criptografa_rsa(ord(char), n, e)
        assert descriptografa_rsa(criptografado, n, d) == ord(char)

def test_criptografa_e_descriptografa3():
    n, e, d = gera_chave()
    mensagem = "Hello, World!"
    criptografado = criptografa_rsa(int.from_bytes(mensagem.encode(), 'big'), n, e)
    assert descriptografa_rsa(criptografado, n, d) == int.from_bytes(mensagem.encode(), 'big')