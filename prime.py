import sys
import math

def isPrime(n):
    if n<1:
        return False;
    if n<=3:
        return True;
    for j in range(2,int(pow(n,(1/2))+1)):
        if(n%j==0):
            return False;
    return True;




#f=open("./primes.txt", "a+")
#primes=[]
#for line in f:
 #   primes+=f.readline
for i in range(100):
    if(isPrime(i)):
        print(i)
      # f.write(str(i))
#f.close()
    
