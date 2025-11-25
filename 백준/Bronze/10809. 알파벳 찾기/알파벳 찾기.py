import sys
input = sys.stdin.readline

s = list(input().strip())
alp = 'qwertyuiopasdfghjklzxcvbnm'
alphabet = sorted(alp)
res = [-1] * 26
dic = dict(zip(alphabet, res))

for i in range(len(s)):
    if dic[s[i]] == -1:
        dic[s[i]] = i
rel = []        
for i in dic:
    rel.append((dic[i]))
    
print(*rel)