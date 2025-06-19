from src.prime_gen import gera_primo

def gera_chave():
    p = gera_primo()
    q = gera_primo()
    while p == q:
        q = gera_primo()
    n = p*q
    z = (p - 1) * (q - 1)
    e = gera_primo()
    while z % e == 0:
        e = gera_primo()
    d = pow(e, -1, z)
    return n, e, d

def criptografa(mensagem, n, e):
    return pow(mensagem, e, n)

def descriptografa(criptograma, n, d):
    return pow(criptograma, d, n)

def criptografa_mensagem(mensagem, n, e):
    return [criptografa(ord(char), n, e) for char in mensagem]

def descriptografa_mensagem(criptograma, n, d):
    return ''.join([chr(descriptografa(char, n, d)) for char in criptograma])