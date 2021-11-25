n = (input("n elementow: "))

a = 1
c = 0

for i in range(int(n) - 1):
    b = a/(i + 2)
    c += b
print(c + a)