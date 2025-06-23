import pytest
from src.sha import calcular_sha3_512

def test_calcular_sha3_512():
    hash = calcular_sha3_512('tests/exemplo/exemplo1.txt')
    assert hash.hex() == 'a30f5466d26f804349076f453eafe5a74249626572a496caf60da4e9d782eae75eb9107ca6f5d9cfaf6c4805446ebd62aaa5d30ec29fb962310c391df076aba1'