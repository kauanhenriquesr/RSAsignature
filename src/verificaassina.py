import base64
from src.sha import calcular_sha3_512
from src.opea import criptografa_rsa_oaep, descriptografa_rsa_oaep

def assinatura(file_path, n, e, d):
    print(n, e, d)
    hash = calcular_sha3_512(file_path)
    print(hash)
    em = criptografa_rsa_oaep(hash, n, e)
    print(em)
    return base64.b64encode(em.to_bytes(256, 'big')).decode(encoding='utf-8')

def verifica(file_path, assinatura, n, e, d):
    em = base64.b64decode(assinatura)
    print(em)
    em = int.from_bytes(em, 'big')
    hash = descriptografa_rsa_oaep(em, n, d)
    hash_arquivo = calcular_sha3_512(file_path)
    return hash == hash_arquivo