# WA and TLE
from collections import deque

N, M = map(int, input().split())
si = sj = gi = gj = None
A = []
judge = [False] * 9
for i in range(N):
    a = list(map(str, input()))
    if 'S' in a:
        si = i
        sj = a.index('S')
    if 'G' in a:
        gi = i
        gj = a.index('G')
    A.append(a)
    for j in range(len(a)):
        if not (a[j] == 'S' or a[j] == 'G'):
            judge[int(a[j])-1] = True

if False in judge:
    print(-1)
    exit()

Q = deque()
Q.append([si, sj])

cnt = 0

target = '1'

nowi, nowj = si, sj

while len(Q) > 0:

    i, j = Q.popleft()

    discover = False

    for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        if not (0<=i2<N and 0<=j2<M):
            continue
        else:
            Q.append([i2, j2])
        if A[i2][j2] == target:
            ti, tj = i2, j2
            discover = True
    
    if discover:
        cnt += abs(nowi-ti) + abs(nowj-tj)
        if target == '9':
            target = 'G'
        elif target == 'G':
            break
        else:
            target = int(target)
            target += 1
            target = str(target)
        Q.clear()
        nowi, nowj = ti, tj
        Q.append([ti, tj])

print(cnt)