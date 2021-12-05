def liczbyDzies(n):
    rzym = {"I": 1, "IV": 4, "V": 5, "IX":9, "X": 10, "XL":40, "L": 50, "C": 100, "CD":400 , "D": 500, "CM":900, "M": 1000}
    rzym_int = 0
    for i in range(len(n)):
        if i > 0 and rzym[n[i]] > rzym[n[i - 1]]: #zeby ta pierwsza byla wieksza typu VII
            rzym_int += rzym[n[i]]  - 2 * rzym[n[i - 1]] #no to sumuje  ze np VII to 5 - 
            
        else:
            rzym_int += rzym[n[i]] #jesli sie ma nie dodawac to bierze ze slownika odpowiednia wartosc
    return rzym_int

n=str(input("Podaj liczbe rzymska: "))
print(liczbyDzies(n))