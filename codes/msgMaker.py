import re


def formatMessage(msg):
    msg=msg.lower()
    return re.sub("[^a-z]", "",msg)

def encode(msg):
    msg=formatMessage(msg)
    output=[]
    for msgChar in msg:
        #ord converts to ascii. Subtract 96 to get a set at 1
        number=ord(msgChar)-96
        output.append(number)
    
    return output
        
    

print(encode("abcdefghijklmnopqrstuvwxyz"))
