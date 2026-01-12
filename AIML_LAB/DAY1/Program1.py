import math

def isPrime(n):
    c =int(0);
    for i in range (2,int(math.sqrt(n))) :
        if(n%i==0):
            c=1
            break
    if(c==1):
        print(f"{n} is not prime")
    else:
        print(f"{n} is prime")
    return

def isPalindrome(n):
    s=str(n)
    if(s==s[::-1]):
        print(f"{n} is palindrome")
    else:
        print(f"{n} is not palindrome")

def isArmstrong(n):
    m,new_num=n,0
    c=len(str(m))

    while(n>0):
        d=n%10;
        new_num+=int(math.pow(d,c))
        n//=10
    if(new_num==m):
        print(f"{m} is an armstrong number")
    else:
        print(f"{m} is not an armstrong number")
n = int(input("Enter a number: "))

isPrime(n)
isPalindrome(n)
isArmstrong(n)
