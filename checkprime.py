def checkPrime(n):
    count=0
    for i in range(1,n+1):
        if(n%i)==0:
            count+=1
    return count==2

n=int(input('Enter the number'))
if(checkPrime(n)):
    print("Prime")
else:
    print("Not Prime")