import math
n = int(input("Podaj dlugosc tablicy"))
tablica = []
for i in range(0,n):
    a = (input("Podaj jakie sa elementy:"))
    tablica.append(a)

tablica = list(dict.fromkeys(tablica))
print(tablica)

