def isPrime(n):
    flag = 1
    if n==2:
        return True
    for i in range(2, n//2 +1):
        if n%i ==0:
            flag =0
            return False
    if flag == 1:
        return True
           

def perfectFact(n):
    s=0
    for i in range(1,n):
        if(n%i == 0):
            s=s+i
            print(i, end=" ")
