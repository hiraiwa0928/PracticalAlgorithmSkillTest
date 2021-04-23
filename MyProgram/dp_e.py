N, W = map(int, input().split())
ws = [0]
vs = [0]
for i in range(N):
    w, v = map(int, input().split())
    ws.append(w)
    vs.append(v)

weight =[[float('inf')]*(10**5+1) for _ in range(N+1)]

weight[0][0] = 0

for i in range(1, N+1):
    for v in range(10**5+1):
        weight[i][v] = weight[i-1][v]
        if v-vs[i] >= 0:
            weight[i][v] = min(weight[i][v], weight[i-1][v-vs[i]] + ws[i])

ans = None
for v in range(10**5, -1, -1):
    if weight[N][v] <= W:
        ans = v
        break

print(ans)