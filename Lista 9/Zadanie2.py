import sys, re
import numpy

def operacje(info):
    info = str(info)
    info = re.findall('\w+', info)      # findall w+ - zwraca alfnumeryczne znaki w postaci listy (bez spacji i przecinka)
    print(info)
    dane = [int(i) for i in info if type(i) == int or i.isdigit()]  # tylko gdy jest liczba lub mozna zamienic na liczbe
    wyniki = [numpy.mean(dane), numpy.std(dane), numpy.var(dane)]
    return wyniki

if len(sys.argv) == 1:
    x = sys.stdin.read()
else:
    x = sys.argv[1:]
print(x)
wyniki = operacje(x)
print("srednia: ", wyniki[0], "odchylenie standardowe: ", wyniki[1], "wariancja: ", wyniki[2])
