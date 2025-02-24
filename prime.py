import sys
import math

def isPrime(n):
    for j in range(2,int(pow(n,(1/2)))):
        if(i%j==0):
            return False;
    print(i);
    return True;




#primes=[0,1,2]
f=open("primes.txt","a")
for i in range(100000000000):
    if(isPrime(i)):
       f.write(i + ", ")
   
f.close()
