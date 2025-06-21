import base64
from src.verificaassina import assinatura, verifica
from src.rsa import gera_chave

if __name__ == '__main__':
    n, e, d = gera_chave()
    assinatura = assinatura("assets/teste.txt", n, e, d)
    print(assinatura)
    teste = b'0'+base64.b64encode(d.to_bytes(256, 'big'))
    print(teste)
    try:
        print(verifica("assets/teste.txt", teste, n, e, d))
    except AssertionError as e:
        print(e)