import sys
import math
input = sys.stdin.readline

xa, ya, xb, yb, xc, yc = map(float, input().split())

if (xb - xa)*(yc - ya) == (yb - ya)*(xc - xa):
    print(float(-1))

else:
    AB = math.sqrt((xa-xb)**2 + (ya-yb)**2)
    AC = math.sqrt((xa-xc)**2 + (ya-yc)**2)
    BC = math.sqrt((xb-xc)**2 + (yb-yc)**2)

    pa = 2 * (AB + AC)
    pb = 2 * (AB + BC)
    pc = 2 * (AC + BC)

    print(max(pa, pb, pc)-min(pa, pb, pc))