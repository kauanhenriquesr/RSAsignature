import hashlib
from src.rsa import criptografa_rsa, descriptografa_rsa
import random

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def mgf1(seed_mgf, mascara_len):
    h_len = hashlib.sha3_512().digest_size
    
    if mascara_len > 2**32 * h_len:
        raise ValueError("Máscara longa demais")

    T = b""
    num_blocks = mascara_len // h_len if mascara_len % h_len == 0 else mascara_len // h_len + 1
    for i in range(num_blocks):
        C = i.to_bytes(4, 'big')
        T += hashlib.sha3_512(seed_mgf + C).digest()

    return T[:mascara_len]

def codifica_oaep(message, label = b""):
    h_len = hashlib.sha3_512().digest_size

    if len(message) > 256 - 2 * h_len - 2:
        raise ValueError("Mensagem longa demais para codificar com OAEP")

    label_hash = hashlib.sha3_512(label).digest()
    ps = b'\x00' * (256 - len(message) - 2 * h_len - 2)

    db = label_hash + ps + b'\x01' + message
    seed = random.randbytes(h_len)

    mascara_db = mgf1(seed, 256 - h_len - 1)

    db_mascarado = xor_bytes(db, mascara_db)

    mascara_seed = mgf1(db_mascarado, h_len)

    seed_mascarado = xor_bytes(seed, mascara_seed)

    mensagem_codificada = b'\x00' + seed_mascarado + db_mascarado

    return mensagem_codificada

def decodifica_oaep(em, label = b""):
    tamanho_em = len(em)
    h_len = hashlib.sha3_512().digest_size
    
    if tamanho_em != 256:
        raise ValueError("Erro de decifragem: comprimento da mensagem codificada inválido")

    y = em[0:1]
    seed_mascarado = em[1:h_len + 1]
    db_mascarado = em[h_len + 1:]
    
    mascara_seed = mgf1(db_mascarado, h_len)
    seed = xor_bytes(seed_mascarado, mascara_seed)

    mascara_db = mgf1(seed, 256 - h_len - 1)
    db = xor_bytes(db_mascarado, mascara_db)

    label_hash_esperado = hashlib.sha3_512(label).digest()
    
    label_hash_recuperado = db[:h_len]
    
    separator_index = -1
    for i in range(h_len, len(db)):
        if db[i] == 1:
            separator_index = i
            break
    
    assert y == b'\x00', "Erro de decifragem: primeiro byte inválido"
    assert label_hash_recuperado == label_hash_esperado, "Erro de decifragem: hash do label inválido"
    assert separator_index != -1, "Erro de decifragem: separador não encontrado"
    assert len(db[separator_index + 1:]) > 0, "Erro de decifragem: mensagem vazia"

    ps_recuperado = db[h_len:separator_index]
    for byte in ps_recuperado:
        assert byte == 0, "Erro de decifragem: padding inválido"
    
    return db[separator_index + 1:]

def criptografa_rsa_oaep(mensagem, n, chaveprivada):
    mensagem_codificada = codifica_oaep(mensagem)
    return criptografa_rsa(int.from_bytes(mensagem_codificada, 'big'), n, chaveprivada)

def descriptografa_rsa_oaep(mensagem, n, chavepublica):
    mensagem_descriptografada = descriptografa_rsa(mensagem, n, chavepublica)
    return decodifica_oaep(mensagem_descriptografada.to_bytes(256, 'big'))