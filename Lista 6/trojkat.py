import math


def obwod(a, b, c):
    obw = a + b + c
    return obw


def pole(a, b, c):
    P = math.sqrt(((1 / 2) * (a + b + c)) * (((1 / 2) * (a + b + c)) - a) * (((1 / 2) * (a + b + c)) - b) * (
            ((1 / 2) * (a + b + c)) - c))
    return P


def boczny(a, b, c):
    if a == b and b == c:
        boczny = "trójkąt równoboczny"
    elif a == b or a == c or b == c:
        boczny = "trójkąt równoramienny"
    else:
        boczny = "trójkąt różnoboczny"
    return boczny


def katny(a, b, c):
    if a >= b and a >= c:
        if a ** 2 > b ** 2 + c ** 2:
            kat = "rozwartokątny"
        elif a ** 2 == b ** 2 + c ** 2:
            kat = "prostokątny"
        else:
            kat = "ostrokątny"
    elif b >= a and b >= c:
        if b ** 2 > a ** 2 + c ** 2:
            kat = "rozwartokątny"
        elif b ** 2 == a ** 2 + c ** 2:
            kat = "prostokątny"
        else:
            kat = "ostrokątny"
    elif c >= a and c >= b:
        if c ** 2 > a ** 2 + b ** 2:
            kat = "rozwartokątny"
        elif c ** 2 == a ** 2 + b ** 2:
            kat = "prostokątny"
        else:
            kat = "ostrokątny"
    return kat
