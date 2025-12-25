# 선물할 같은 크기의 박스 n개
# 모든 박스는 정육면체, 크기는 A x A x A
# 이 박스를 L x W x H 인 직육면체 박스에 모두 넣으려고 한다.
# A**3 * n <= L * W * H
import sys
input = sys.stdin.readline

n, l, w, h = map(int, input().split())
left, right = 0.0, min(l,w,h)

for _ in range(100):
    mid = (left + right) / 2
    
    if mid == 0:
        left = mid
        continue
    
    cnt = int(l//mid) * int(w//mid) * int(h//mid)
    
    if cnt >= n:
        left = mid
    else:
        right = mid

print(left)