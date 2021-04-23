# TLE
from collections import deque

N, M = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(M)]

figure = [[] for _ in range(N)]

for i in range(M):
    figure[xy[i][0]-1].append(xy[i][1]-1)

def search():
    cnt = 0
    while len(Q) > 0:
        i, num = Q.popleft()
        for i2 in figure[i]:
            Q.append([i2, num+1])
            cnt = num+1
    return cnt

ans = -float('INF')
Q = deque()

for i in range(N):
    Q.append([i, 0])
    num = search()
    if num > ans:
        ans = num
    Q.clear()
    cnt = 0

print(ans)