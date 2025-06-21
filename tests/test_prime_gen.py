from src import miller_rabin, gera_impar, gera_primo
import pytest

def test_gera_impar():
    assert gera_impar() % 2 == 1
    assert gera_impar() % 2 != 0

def test_miller_rabin():
    assert miller_rabin(89, 40) == True
    assert miller_rabin(97, 40) == True

def test_gera_primo():
    assert miller_rabin(gera_primo(), 40) == True
    assert miller_rabin(gera_primo(), 40) == True
    assert miller_rabin(gera_primo(), 40) == True
