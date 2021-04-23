N, M = map(int, input().split())

# 全ての頂点の組についての最短距離を保存する2次元配列distを作る
dist = [[float('INF')]*N for _ in range(N)]

# グラフの辺を受け取り、distに直接書き込む
for _ in range(M):
    u, v, c = map(int, input().split())
    dist[u][v] = c

# iからiへの同じ頂点同士の距離は0としておく
for i in range(N):
    dist[i][i] = 0

# ワーシャル-フロイド法
for k in range(N):
    for x in range(N):
        for y in range(N):
            dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])

# 全ての頂点の組について最短距離を合計する
ans = 0
for i in range(N):
    for j in range(N):
        ans += dist[i][j]

print(ans)