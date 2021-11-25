from itertools import permutations

n = (input("ilosc elementow "))
lista = {}
for i in range(n):
    lista[i] = int(input())

for x in permutations(lista):
    print (x)