klucz={"a" : "y","e" : "i","i" : "o","o" : "a","y" : "e"}

z=input("Podaj słowo ")

def szyfr(z):
    for x in range(len(z)):
        for y in klucz: 
            if(z[x]==y): #dla kazdej litery zgadajacej sie z kluczem bedzie zamienial
                z=z[:x]+klucz[y]+z[x+1:] #tu zmienia z danego y z klucza
                break
    return z

def deSzyfr(z):
    for x in range(len(z)):
        for y in klucz:
            if (z[x] == klucz[y]): #a tu tylko jak z bedzie takie jak zgadzajace sie z kluczeem
                z = z[:x] + y + z[x + 1:] #to zamienia zmieniona na dobra
                break
    return z
print(szyfr(z))
print(deSzyfr(szyfr(z)))
