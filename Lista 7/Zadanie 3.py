import random
import time

def sort(tablica, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if tablica[j] > tablica[j+1]:
                bufor = tablica[j+1]
                tablica[j+1] = tablica[j]
                tablica[j] = bufor

n = int(input("podaj n: "))
tablica = []
for i in range(0,n):
    a = random.randint(0,20)
    tablica.append(a)
print(tablica)

start = time.perf_counter()
sort(tablica, n)
end = time.perf_counter()
print(f"{end-start:0.4f}")
print(tablica)