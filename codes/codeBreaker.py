f=open("TestMessage1.txt")
out=""

data=f.read().split()
for char in data:
    char=int(char)
    offset=0
    while(char%128!=0):
        char-=1
    print(char)
    out+=chr(char)
print(out)
