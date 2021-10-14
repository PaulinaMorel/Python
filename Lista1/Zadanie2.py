import math #potrzebuje tego bo sinus
a=3
b=4
alfa=47

c=math.radians(alfa) #to mi zamienić musi z kąta na radiany bo po prostu tak juz jest w pythonie
pole=(a*b*math.sin(c))/2 #tutaj juz wzór na pole
print(pole)