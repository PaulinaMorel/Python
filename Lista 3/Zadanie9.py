m = int(input("Ilość wierszy: "))
n = int(input("Ilość kolumn: "))
x = [[i*j for i in range(1,n + 1)] for j in range (1,m + 1)] # wartosci

for j in range(0,n):
   print('\n')
   for i in range(0,m):
      print(" ",x[i][j], end="  ")
