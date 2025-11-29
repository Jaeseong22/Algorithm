import sys
input = sys.stdin.readline

n, m = map(int, input().split())

res = 0
m_set = []
for _ in range(m):
    m_set.append(list(map(int, input().split())))

package = []
price = []

for i in m_set:
    package.append(i[0])
    price.append(i[1])
    
m_pa = min(package)
m_pr = min(price)
        
res = min(
    m_pa*(n//6 + 1),
    m_pa*(n//6) + m_pr*(n%6),
    m_pr * n
)
        
print(res)