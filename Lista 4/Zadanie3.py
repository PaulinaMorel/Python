import math
r2d = (input("Jesli chcesz z radianow na stopnie to wpisz r2d "))
x = float(input("Podaj wartosc jaka chesz zmienic "))

def convert(x,how="r2d"):
    if how =="r2d":
        return math.radians(x)
    else:
        return math.degrees(x)

print(convert(x,r2d))
