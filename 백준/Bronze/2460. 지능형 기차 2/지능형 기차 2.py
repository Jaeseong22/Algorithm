import sys
input = sys.stdin.readline

people = 0
peoples = []
for _ in range(10):
    a, b = map(int, input().split())
    people -= a
    people += b
    peoples.append(people)

print(max(peoples))