def gcd(n1,n2):
    while(n1>n2):
        if n1> n2:
            n1=n1-n2
        else:
            n2-=n1
    return n1
n1=int(input('Enter the first Number '))
n2=int(input('Enter the second Number '))
print("GCD of ",n1  ,"and", n2 ,"is ",gcd(n1,n2))