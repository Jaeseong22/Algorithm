def solution():
    l = int(input())
    m = 1234567891
    r = 31
    st = input()
    result = 0
    num = 0
    alpha = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
    for i in st:
        for j in alpha:
            if(i == j):
                result += alpha[j]*r**num
                num += 1
                break

    print(result % m)
solution()