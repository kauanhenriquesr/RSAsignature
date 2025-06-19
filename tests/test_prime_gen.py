from src import miller_rabin, gera_impar, gera_primo
import pytest

def test_gera_impar():
    assert gera_impar() % 2 == 1
    assert gera_impar() % 2 != 0

def test_miller_rabin():
    assert miller_rabin(29, 40) == True
    assert miller_rabin(31, 40) == True
    assert miller_rabin(37, 40) == True
    assert miller_rabin(41, 40) == True
    assert miller_rabin(43, 40) == True
    assert miller_rabin(47, 40) == True
    assert miller_rabin(53, 40) == True
    assert miller_rabin(59, 40) == True
    assert miller_rabin(61, 40) == True
    assert miller_rabin(67, 40) == True
    assert miller_rabin(71, 40) == True

def test_gera_primo():
    assert miller_rabin(gera_primo(40), 40) == True
