import hashlib

def calcular_sha3_512(file_path):
    sha3_hasher = hashlib.sha3_512()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha3_hasher.update(chunk)
    return sha3_hasher.digest()