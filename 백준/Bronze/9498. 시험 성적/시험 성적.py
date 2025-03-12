def solution():
    n = int(input())
    if(n > 89):
        print("A")
    elif(n>79 and n<90):
        print("B")
    elif(n>69 and n<80):
        print("C")
    elif(n>59 and n<70):
        print("D")
    else:
        print("F")
  
solution()