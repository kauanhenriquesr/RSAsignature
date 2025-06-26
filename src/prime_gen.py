import random

def miller_rabin(n, k):
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, n-1, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                continue
            if x == 1:
                return False
        return False
    return True

def gera_impar():
    num = random.randint(2**1023, 2**1024 - 1)
    
    if num % 2 == 0:
        num += 1
    return num

def gera_primo(iteracoes=40):    
    while True:
        candidato = gera_impar()
        if miller_rabin(candidato, iteracoes):
            return candidato
