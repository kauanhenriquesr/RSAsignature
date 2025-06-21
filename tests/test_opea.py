import pytest
from src import codifica_oaep, decodifica_oaep, criptografa_rsa_oaep, descriptografa_rsa_oaep, gera_chave

def test_codifica_e_decodifica():
    mensagem = b"Hello, World!"
    codificado = codifica_oaep(mensagem)
    assert decodifica_oaep(codificado) == mensagem

def test_codifica_e_decodifica2():
    mensagem = b"Testando a funcao codifica_oaep"
    codificado = codifica_oaep(mensagem)
    assert decodifica_oaep(codificado) == mensagem

def test_codifica_e_decodifica3():
    mensagem = b"Testando novamente a funcao codifica_oaep"
    codificado = codifica_oaep(mensagem)
    assert decodifica_oaep(codificado) == mensagem

def test_sad_path_codifica_e_decodifica4():
    mensagem = b"Testando a funcao codifica_oaep"
    codificado = codifica_oaep(mensagem)
    codificado = codificado[:-1] + bytes([codificado[-1] ^ 0xff])
    with pytest.raises(AssertionError):
        decodifica_oaep(codificado)

def test_criptografa_rsa_oaep():
    n, e, d = gera_chave()
    mensagem = b"Testando a funcao criptografa_rsa_oaep"
    criptografado = criptografa_rsa_oaep(mensagem, n, e)
    assert descriptografa_rsa_oaep(criptografado, n, d) == mensagem

def test_criptografa_rsa_oaep2():
    n, e, d = gera_chave()
    mensagem = b"Testando novamente a funcao criptografa_rsa_oaep"
    criptografado = criptografa_rsa_oaep(mensagem, n, e)
    assert descriptografa_rsa_oaep(criptografado, n, d) == mensagem