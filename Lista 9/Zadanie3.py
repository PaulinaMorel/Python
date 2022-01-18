import math
import matplotlib.pyplot as plt

v0 = float(input("v0[m/s]: "))
alfa = float(input("alfa[stopnie]: "))
#kat w stopniach
alfa_rad = math.radians(alfa)

g = 9.81
v0y = v0 * math.sin(alfa_rad)
v0x = v0 * math.cos(alfa_rad)
h_max = (v0y * v0y)/(2 * g)
zasieg = (v0 * v0 * math.sin(2 * alfa_rad))/g
t_max = (2 * v0y)/g

print(str(h_max) + " h_max[m]")
print(str(zasieg) + " zasieg[m]")
print(str(t_max) + " czas[s]")

#vx = v0 * math.cos(alfa_rad)
#vy = v0 * math.sin(alfa_rad) - g * t

t_int = int(t_max) + 1

vx = []
vy = []
y = []
x = []
t = []
for t_ in range(t_int):
    vx.append(v0 * math.cos(alfa_rad))
    vy.append(v0 * math.sin(alfa_rad) - g * t_)
    y.append((v0y * t_) - (g * t_ * t_)/2)
    x.append(v0x * t_)
    t.append(t_)

print(vx)
print(vy)
print(t)
plt.subplot(221, title = "predkosc", xlabel = "[s]", ylabel = "[m/s]")
plt.plot(t, vy, t, vx)

plt.subplot(222, title = "polozenie w czasie", xlabel = "[s]", ylabel = "[m]")
plt.plot(t, y)

plt.subplot(223, title = "tor lotu", xlabel = "[m]", ylabel = "[m]")
plt.plot(x, y)

plt.show()