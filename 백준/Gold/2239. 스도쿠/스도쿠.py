from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
board = [list(map(int, input().strip())) for _ in range(9)]

zeros = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zeros.append((i, j))

def row_check(r, c, num):
    for x in range(9):
        if c != x and num == board[r][x]:
            return False
    return True

def col_check(r, c, num):
    for x in range(9):
        if r != x and num == board[x][c]:
            return False
    return True

def triple_check(r, c, num):
    nc = (c // 3) * 3
    nr = (r // 3) * 3
    for x in range(3):
        for y in range(3):
            if (r != nr + x or c != nc + y) and board[nr+x][nc+y] == num:
                return False
    return True

def dfs(depth, r, c, num):
    if depth > 0:
        if not row_check(r, c, num):
            return
        if not col_check(r, c, num):
            return
        if not triple_check(r, c, num):
            return
    
    if depth >= len(zeros):
        for k in range(9):
            print(''.join(map(str, board[k])))
        exit()
    
    nr, nc = zeros[depth]
    for j in range(1, 9+1):
        board[nr][nc] = j
        dfs(depth+1, nr, nc, j)
        board[nr][nc] = 0

dfs(0, 0, 0, 0)