import math
import cmath
a=0
b=1

z=complex(a,b)

print("Czesc rzeczywista: ")
print("sin:", cmath.sin(z).real) #zeby liczylo czesc rzeczywista sinus
print("cos:", cmath.cos(z).real) #no i cos
print("Czesc urojona: ")
print("sin:", cmath.sin(z).imag) #a tu urojony sinus
print("cos:", cmath.cos(z).imag)

a=cmath.sin(z)**2+cmath.cos(z)**2
print(a)
#nie jest spełnione sin(z)+cos(z)=1
#zawsze wychodzi 1.00...002