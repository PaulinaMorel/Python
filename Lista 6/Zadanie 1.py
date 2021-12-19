import trojkat

a = int(input("Podaj długość pierwszego boku: "))
b = int(input("Podaj długość drugiego boku: "))
c = int(input("Podaj długość trzeciego boku: "))


def check(a,b,c):
    if a<b+c and b<a+c and c<b+a:
        print("Parametry trójkąta są poprawne")
        print("Obwod trojkata to:", trojkat.obwod(a, b, c))
        print("Pole trojkata to:", trojkat.pole(a, b, c))
        print("Jest to ", trojkat.boczny(a, b, c), "oraz", trojkat.katny(a, b, c))
    else:
        print("Podaj prawidlowe wartosci. ")

print(check(a,b,c))



