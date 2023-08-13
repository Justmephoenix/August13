def lcm(n1,n2):
    temp1=n1
    temp2=n2
    while(n1>n2):
        if n1> n2:
            n1=n1-n2
        else:
            n2-=n1
    return (temp1*temp2)//n1

n1=int(input('Enter the first Number '))
n2=int(input('Enter the second Number '))
print("GCD of ",n1  ,"and", n2 ,"is ",lcm(n1,n2))