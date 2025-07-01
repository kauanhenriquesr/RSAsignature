import base64
from src.sha import calcular_sha3_512
from src.opea import criptografa_rsa_oaep, descriptografa_rsa_oaep

def assinatura(file_path, n, private_key):
    hash = calcular_sha3_512(file_path)
    print("-"*30)
    print("Hash do arquivo:", hash)
    em = criptografa_rsa_oaep(hash, n, private_key)
    print("-"*30)
    print("Mensagem criptografada:", em)
    print("-"*30)
    return base64.b64encode(em.to_bytes(256, 'big')).decode(encoding='utf-8')

def verifica(file_path, assinatura, n, public_key):
    try:
        em = base64.b64decode(assinatura)
        em = int.from_bytes(em, 'big')
        print("Mensagem criptografada:", em)
        hash = descriptografa_rsa_oaep(em, n, public_key)
        print("-"*30)
        print("Hash descriptografado:", hash)
        print("-"*30)
        hash_arquivo = calcular_sha3_512(file_path)
        print("Hash do arquivo:", hash_arquivo)
        print("-"*30)
        return hash == hash_arquivo
    except (ValueError, AssertionError):
        return False