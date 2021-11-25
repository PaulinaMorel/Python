n = int(input())
a = 1
if n < 0:
   print("silnia nie istnieje")
elif n == 0:
   print("silnia z 0 = 1")
else:
   for i in range(1,n + 1):
       a = a * i
   print("silnia =",a ) 