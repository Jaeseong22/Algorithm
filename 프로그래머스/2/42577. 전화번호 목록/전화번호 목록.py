def solution(phone_book):
    answer = True
    hash = {}
    for i in phone_book:
        hash[i] = 1
    
    for num in phone_book:
        arr = ''
        for i in num:
            arr += i
            if arr in hash and arr != num:
                answer = False
    
    return answer