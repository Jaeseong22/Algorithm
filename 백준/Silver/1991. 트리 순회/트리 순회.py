import sys
input = sys.stdin.readline

N = int(input())
graph = {}

for _ in range(N):
    a, b, c = input().strip().split()
    graph[a] = [b, c]

def preorder(a):
    if a != '.':
        print(a, end='')
        preorder(graph[a][0])
        preorder(graph[a][1])

def inorder(a):
    if a != '.':
        inorder(graph[a][0])
        print(a, end='')
        inorder(graph[a][1])

def postorder(a):
    if a != '.':
        postorder(graph[a][0])
        postorder(graph[a][1])
        print(a, end='')
        
preorder('A')
print()
inorder('A')
print()
postorder('A')