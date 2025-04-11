f=open("SecretMessageThree.txt")
out=""
firstPass=[]
data=f.read().split()
charCount=0
for char in data:
    charCount+=1
    char=int(char)
    offset=20
    while(char%128!=0):
        char-=20
        offset+=1
    firstPass.append(char)
    print(firstPass)
    out+=chr(char)
print(charCount)
