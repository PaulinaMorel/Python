r = int(input("Podaj r: "))
g = int(input("Podaj g: "))
b = int(input("Podaj b: "))

R, G, B = r/255, g/255, b/255

Cmax = max(R, G, B)
Cmin = min(R, G, B)
df = Cmax - Cmin

if Cmax == Cmin:
    h = 0
elif Cmax == R:
    h = (60 * ((G - B)/df) + 360) % 360
elif Cmax == G:
    h = (60 * ((B - R)/df) + 120) % 360
elif Cmax == B:
    h = (60 * ((R - G)/df) + 240) % 360

if Cmax == 0:
    s = 0
else:
    s = (df/Cmax) * 100

v = Cmax * 100

print("h",h,"% ","s",s,"% ","v",v,"%")