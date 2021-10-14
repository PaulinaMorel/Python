import math #potrzebuje tego bo sinus
print("podaj dlugosc pierwszego boku: ")
a=int(input())
print("podaj dlugosc drugiego boku: ")
b=int(input())
print("podaj kat miedzy bokami: ")
alfa=int(input())
c=math.radians(alfa) #to mi zamienić musi z kąta na radiany bo po prostu tak juz jest w pythonie
pole=(a*b*math.sin(c))/2 #tutaj juz wzór na pole
print("pole wynosi: ")
print(pole)

