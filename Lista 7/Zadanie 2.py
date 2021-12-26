import random
import time
lista100 = []
lista200 = []
lista300 = []
def sort(lista,n):
    for x in range(n):
        element=lista[x] 
        y=x-1
        while y>=0 and element<lista[y]: 
            lista[y+1]=lista[y] 
            y-=1 
            lista[y+1] = element 
for i in range(100):
    lista100.append(random.randint(0,20))
for i in range(200):
    lista200.append(random.randint(0,20))
for i in range(300):
    lista300.append(random.randint(0,20))
czas1 = time.time_ns()
sort(lista100,100)
czas2 = time.time_ns()
print("Sortowanie 1 listy: ", (czas2-czas1)/(10**9)," sekund")
print(lista100)
czas1 = time.time_ns()
sort(lista200,200)
czas2 = time.time_ns()
print("Sortowanie 2 listy: ", (czas2-czas1)/(10**9)," sekund")
print(lista200)
czas1 = time.time_ns()
sort(lista300,300)
czas2 = time.time_ns()
print("Sortowanie 3 listy: ", (czas2-czas1)/(10**9)," sekund")
print(lista300)