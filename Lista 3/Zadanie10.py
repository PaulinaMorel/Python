lista=[]
for i in range(100,401):
    for j in str(i):
        if int(j) %2 != 0:
            break
    else:
        lista.append(i)
print(lista)
