import math
print("podaj liczbe elementow w tablicy")
n = int(input())
tablica = []
for i in range(0,n): # otwiera tablice co ma n elementow
    a = int(input()) #pyta o elementy tablicy
    tablica.append(a) #dodaje je 
print(tablica)

print("suma: ", sum(tablica))
print("iloczyn: ", math.prod(tablica))

