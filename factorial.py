def factorial(n):
    f=1
    while(n):
        f*=n
        n-=1
    return f
n=int(input("Enter a number"))
f=factorial(n)
print(f'factorial of {n} is {f}')