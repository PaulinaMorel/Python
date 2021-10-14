import math
import cmath
a=float(input("podaj czesc rzeczywista"))
b=float(input("podaj czesc urojona"))
z=complex(a,b) #zmienia na zespolona
print("Modul z z to: ", math.sqrt(a**2+b**2)) #po prostu wzor
print("Argument z z to: ",math.cos(a/abs(z))) #abs to wartosc bezwzgledna
print(complex.conjugate(z))#to pokazuje np 1-2j to to sprzezenie liczby zespolonej