def checkPalllindrome(n):
    rev=0
    while n:
        rev= rev*10 + (n%10)
        n//=10
    return rev
n=int(input("Enter the nunmber"))
if(checkPalllindrome(n)==n):
    print("Pallindrome")
else:
    print('Not a pallindrom')