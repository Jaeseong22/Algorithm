import sys
input = sys.stdin.readline

n = int(input())
books = {}

for i in range(n):
    a = input().strip()
    if a in books:
        books[a] += 1
    else:
        books[a] = 1
        
max_value = max(books.values())
best = []

for key, value in books.items():
        if value == max_value:
            best.append(key)

best = sorted(best)
print(best[0])