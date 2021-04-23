N = int(input())
ps = [0]
ps.extend(list(map(int, input().split())))

point = [[float('INF')]*(10**4+1) for i in range(N+1)]
point[0][0] = 0

for i in range(1, N+1):
    for p in range(10**4+1):
        point[i][p] = point[i-1][p]
        if p-ps[i] >= 0:
            point[i][p] = min(point[i][p], point[i-1][p-ps[i]] + ps[i])

ans = 0
for i in range(10**4+1):
    if point[N][i] != float('INF'):
        ans += 1

print(ans)