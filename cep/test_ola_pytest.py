from django.test import TestCase


# Create your tests here.

def soma(n, n2):
    return n + n2


def test_primeiro_test():
    resultado = soma(1, 2)
    resultado_esperado = 3
    assert resultado == resultado_esperado
