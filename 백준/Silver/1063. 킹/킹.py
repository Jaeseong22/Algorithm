import sys
input = sys.stdin.readline

move = {
    'L':  (-1, 0),
    'R':  (1, 0),
    'T':  (0, 1),
    'B':  (0, -1),
    'LT': (-1, 1),
    'RT': (1, 1),
    'LB': (-1, -1),
    'RB': (1, -1)
}

king, stone, n = input().split()

kx = ord(king[0]) - ord('A')
ky = int(king[1]) - 1

sx = ord(stone[0]) - ord('A')
sy = int(stone[1]) - 1

for _ in range(int(n)):
    cmd = input().strip()
    dx, dy = move[cmd]
    
    nkx, nky = kx + dx, ky + dy
    
    if not (0 <= nkx <8 and 0 <= nky <8):
        continue
    
    if nkx == sx and nky == sy:
        nsx, nsy = sx + dx, sy + dy
        if not (0 <= nsx < 8 and 0 <= nsy < 8):
            continue
        sx, sy = nsx, nsy
        
    kx, ky = nkx, nky
    
print(chr(kx + ord('A')) + str(ky + 1))
print(chr(sx + ord('A')) + str(sy + 1))