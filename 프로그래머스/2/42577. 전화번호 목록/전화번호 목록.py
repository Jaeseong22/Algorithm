def solution(phone_book):
    answer = True
    phone_book = set(phone_book)
    
    for num in phone_book:
        p = ''
        for i in num:
            p += i
            if p != num and p in phone_book:
                answer = False
                
    return answer
