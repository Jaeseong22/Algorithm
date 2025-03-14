def solution():
    a = input()
    b = input()
    c = input()

    x = []
    x.append(a)
    x.append(b)
    x.append(c)
    num = 0
    
    for j in x:
        num += 1
        if(j.isdigit()):
            if num == 3:
                result = int(j)+1
                if(result % 3 == 0 and result % 5 == 0):
                    print("FizzBuzz")
                    break
                elif(result %3 == 0):
                    print("Fizz")
                    break
                elif(result %5 == 0):
                    print("Buzz")
                    break
                else:
                    print(result)
                    break
            elif num == 1:
                result = int(j)+3
                if(result % 3 == 0 and result % 5 == 0):
                    print("FizzBuzz")
                    break
                elif(result %3 == 0):
                    print("Fizz")
                    break
                elif(result %5 == 0):
                    print("Buzz")
                    break
                else:
                    print(result)
                    break
            elif num == 2:
                result = int(j)+2
                if(result % 3 == 0 and result % 5 == 0):
                    print("FizzBuzz")
                    break
                elif(result %3 == 0):
                    print("Fizz")
                    break
                elif(result %5 == 0):
                    print("Buzz")
                    break
                else:
                    print(result)
                    break

solution()