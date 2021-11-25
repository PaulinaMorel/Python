a = int(input("Pierwsza liczba: "))
b = int(input("Druga liczba: "))

i = 1
while(i <= a and i <= b): #dla a i b <=0
    if(a % i == 0 and b % i == 0): #zeby reszta z dzielenia przez i oby bula 0
        nwd = i #to wtedy to ich nwd
    i=i+1;   #i dopóki się nie drówna a do b
    
print("nwd z",a," i ",b," = ",nwd)