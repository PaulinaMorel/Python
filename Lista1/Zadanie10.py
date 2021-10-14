import math
import cmath
a=0
b=1

z=complex(a,b)

print("Czesc rzeczywista: ")
print("sin:", cmath.sin(z).real)
print("cos:", cmath.cos(z).real)
print("Czesc urojona: ")
print("sin:", cmath.sin(z).imag)
print("cos:", cmath.cos(z).imag)

a=cmath.sin(z)**2+cmath.cos(z)**2
print(a)
#nie jest spełnione sin(z)+cos(z)=1
#zawsze wychodzi 1.00...002