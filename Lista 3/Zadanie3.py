print("PROGRAM LICZACY PIERWIASTKI Z ROWANANIA KWADRATOWEGO")
a= int(input(" Podaj a: "))
b= int(input(" Podaj b: "))
c= int(input(" Podaj c: "))
if a== 0:
    print("To nie jest równanie kwadratowe")
else:
    delta=(b*b)-(4*a*c)
    print("delta wynosi ", delta)
    if delta <0:
        print("Nie ma w zbiorze rzeczywistych")
    if delta ==0:
        x0=-b/(a*a)
        print("Pierwiastek równania wynosi ", x0)
    if delta >0:
        pdelta = pow(delta,1/2.0)
        x1=(-b-pdelta)/(a*a)
        x2=(-b+pdelta)/(a*a)
        print("Pierwszy pierwiastek równania wynosi ", x1)
        print("Drugi pierwiastek równania wynosi ", x2)