f=open("TestMessage1.txt")
out=""
firstPass=[]
data=f.read().split()
for char in data:
    char=int(char)
    offset=0
    while(char%128!=0):
        char-=1
    firstPass.append(char)
    print(offset)
    out+=chr(char)
print(out)
