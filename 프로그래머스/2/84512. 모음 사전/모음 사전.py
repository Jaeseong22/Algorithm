def solution(word):
    from itertools import product
    words = []
    alpha = ['A', 'E', 'I', 'O', 'U']
    
    for length in range(1, 6):
        for p in product(alpha, repeat=length):
            words.append(''.join(p))
    
    words.sort()
    
    return words.index(word) + 1