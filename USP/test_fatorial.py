def fatorial(n):
    i = fatorial = 1
    while i <= n:
        fatorial = fatorial * i
        i = i+1
    return fatorial

def test_fatorial0():
    assert fatorial (0) == 1

def test_fatorial4():
    assert fatorial (4) == 24

def test_fatorial5():
    assert fatorial (5) == 120



