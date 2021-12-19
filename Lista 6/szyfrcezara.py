def szyfr(word,key):
    szyfr=""
    for i in range (len(word)):
        if not ord(word[i]) >= 97 and ord(word[i]) <=122:
            szyfr += chr(ord(word[i]))
        elif  ord(word[i]) >=97 and  ord(word[i]) <=122:
            if ord(word[i]) + key > 122:
                szyfr +=chr(ord(word[i]) + key - 26)
            else:
                szyfr+= chr(ord(word[i])+key)
    return szyfr



def odszyfr(word,key):
    deszyfr =""
    for i in range(len(word)):
        if not ord(word[i]) >= 97 and ord(word[i]) <=122:
            deszyfr += chr(ord(word[i]))
        elif ord(word[i]) >= 97 and ord(word[i]) <= 122:
            if ord(word[i]) - key < 97:
                deszyfr += chr(ord(word[i]) - key + 26)
            else:
                deszyfr += chr(ord(word[i]) - key)
    return deszyfr

word=input("Podaj slowo: ")
key=int(input("Podaj klucz: "))

x=szyfr(word,key)
print(x)

y=odszyfr(x,key)
print(y)
