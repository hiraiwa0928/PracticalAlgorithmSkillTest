from collections import deque

N = int(input())
pre = -1

p = [[] for _ in range(N)]
for i in range(N): 
    t = int(input())
    if t == -1:
        pre = i
        continue
    p[t-1].append(i)

Q = deque()
Q.append(pre)

db = [[] for _ in range(N)]

while len(Q) > 0:
    i = Q.popleft()

    for j in p[i]:
        db[j].extend(db[i] + [i])
        Q.append(j)

query = int(input())

for _ in range(query):
    a, b = map(lambda x: int(x)-1, input().split())
    if b in db[a]:
        print('Yes')
    else:
        print('No')