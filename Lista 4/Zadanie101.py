a = int(input("Pierwsza liczba: "))
b = int(input("Druga liczba: "))

i = 1
while(i <= a and i <= b): #dla a i b <=0
    if(a % i == 0 and b % i == 0): #zeby reszta z dzielenia przez i oby bula 0
        nwd = i #to wtedy to ich nwd
    else:
        print("Nie maja nwd")   
print("nwd z {0} i {1} = {2}".format(a, b, nwd))