import szyfrcezara

word=input("Podaj slowo: ")
key=int(input("Podaj klucz: "))

x=szyfrcezara.szyfr(word,key)
print(x)

y=szyfrcezara.odszyfr(x,key)
print(y)
