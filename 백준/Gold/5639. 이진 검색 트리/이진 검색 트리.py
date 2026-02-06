import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

tree = []
while True:
    try:
        node = int(input())
        tree.append(node)
    except:
        break
def treepost(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if tree[i] > tree[start]:
            mid = i
            break
    treepost(start + 1, mid - 1)  # 왼쪽 트리
    treepost(mid, end)  # 오른쪽 트리
    print(tree[start])  # 루트 노드


treepost(0, len(tree) - 1)