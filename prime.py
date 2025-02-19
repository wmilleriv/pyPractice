import sys
import math

for i in range(pow(sys.maxsize, 2), 2):
    for j in range(sys.maxsize):
        if i%j==0:
            print(i)

        
    
