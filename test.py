
def output1():
  for i in range(10):
    for j in range(i + 1):
      print(j, end=" ")
    print()

output1()


def descending_pattern():
    for i in range(10, -1, -1):
        for j in range(i):
            print(j, end=" ")
        print()

descending_pattern()



def reverse_ascending_pattern():
    for i in range(10):
        for j in range(i, -1, -1):
            print(j, end=" ")
        print()

reverse_ascending_pattern()

