n=int(input("Podaj n wyrazow ciagu:"))

def lookAndSay(x):
    result=[] #pusta tablica
    i=0 
    while i < len(x):
        licznik=1
        while i + 1 <len(x) and x[i] ==x[i+1]:
            i+=1
            licznik+=1
        result.append(str(licznik)+x[i])
        i+=1
    return ''.join(result)

x="1"
for i in range(n):
    x=lookAndSay(x)
    print(x)
