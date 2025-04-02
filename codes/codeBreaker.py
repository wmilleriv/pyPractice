f=open("TestMessage1.txt")
out=""

data=f.read().split()
for char in data:
    char=int(char)
    out+=chr(char)
print(out)
