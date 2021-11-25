import math
n = int(input("podaj numer elementu: "))
a1 = int(input("podaj 1 element ciagu: "))
q = int(input("podaj q: "))

def element():
    an = a1 * q ** (n-1)
    return an
print(element())
