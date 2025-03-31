def solution():
    import sys
    input = sys.stdin.readline

    n = int(input().strip())
    word_ls = set()

    for _ in range(n):
        word_ls.add(input().strip())
    
    sorted_word = sorted(word_ls, key= lambda x:(len(x), x))

    for word in sorted_word:
        print(word)
        
solution()