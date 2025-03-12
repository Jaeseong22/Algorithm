def solution():
    h, m = map(int, input().split())
    if(m<45):
        if(h < 1):
            h = (h+24) - 1
            m = (m+60) - 45
            print(h,m)
        else:
            h -= 1
            m = (m+60) - 45
            print(h,m)
    else:
        print(h, m-45)
solution()