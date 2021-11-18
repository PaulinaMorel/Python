n = int(input())
a = 1
b = 1
ciąg = [1, 1]

for x in range(2, n):
    nast = ciąg[x - 1] + ciąg[x - 2]
    ciąg.append(nast)
    
print(ciąg)

