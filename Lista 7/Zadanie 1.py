import time
def fibonacci_loop(n):
    a = 0
    b = 1
    for i in range(0, n + 1):
        print(a)
        c = b
        b += a
        a = c

def fibonacci_recursion(n):
    if n <= 1:
        return n
    else:
        return(fibonacci_recursion(n-1) + fibonacci_recursion(n-2)) 

def fibonacci_printer(n):
    for i in range(n):
        print(fibonacci_recursion(i))

def main():
    n = int(input("podaj n: "))
    case = int(input("1 albo 2 "))
    if case == 1:
        start = time.perf_counter()
        fibonacci_loop(n)
        end =  time.perf_counter()
        print(f"{end-start:0.4f}")
    if case == 2:
        start = time.perf_counter()
        fibonacci_printer(n)
        end = time.perf_counter()
        print(f"{end-start:0.4f}")
    
main()