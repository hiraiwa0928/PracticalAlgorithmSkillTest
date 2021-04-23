N, M = map(int, input().split())
A, B, C = [0], [0], [0]
for i in range(M):
    a, b = map(int, input().split())
    c = list(map(lambda x: int(x)-1, input().split()))
    c_val = 0
    for j in c:
        c_val |= 1<<j
    A.append(a)
    B.append(b)
    C.append(c_val)

ALL = 1 << N

cost = [[float('INF')]*ALL for _ in range(M+1)]

cost[0][0] = 0

for n in range(1, M+1):
    for i in range(ALL):
        cost[n][i] = min(cost[n][i], cost[n-1][i])
        cost[n][i|C[n]] = min(cost[n][i|C[n]], cost[n-1][i] + A[n])

ans = cost[M][ALL-1]

if ans == float('INF'):
    ans = -1

print(ans)