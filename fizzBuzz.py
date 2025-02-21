for i in range(10000):
    if i%3==0:
        print("fizz", end ="")
    if i%5==0:
        print("buzz", end ="")
    if i%7==0:
        print("pop", end="")
    if i%5!=0 and i%3!=0 and i%7!=0:
        print(i, end="")
    print()
    
