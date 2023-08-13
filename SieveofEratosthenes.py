#prime number less than or equal to n
def SieveOfEratosthene(n):
    for i in range(1,n+1):
        c=0
        for j in range(1,i+1):
            if (i%j==0) :
                c+=1
        if c==2:
            print(i)
            
n=int(input("Enter the limit"))
SieveOfEratosthene(n)