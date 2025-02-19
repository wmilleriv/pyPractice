def fact(n):
    x=1
    for i in range(2,n+1):
        x=x*i
    return x

print("Enter a number")
x=input()
print(fact(int(x)))
assert(fact(5)==120)
