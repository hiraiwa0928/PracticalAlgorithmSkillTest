from collections import deque

N, M = map(int, input().split())

# グラフは隣接リストとして保持する
G = [[] for _ in range(N)]

# グラフの辺を受け取る
for _ in range(M):
    ai, bi = map(lambda x: int(x) - 1, input().split())
    G[ai].append(bi)
    G[bi].append(ai)

# 頂点0から各頂点への最短距離を保持する配列
# N個の-1で満たしておく(-1の場合は未訪問であることを表す)
dist = [-1] * N

# 幅優先対策で使うキュー
Q = deque()

# 始点となる頂点0をキューに追加しておく
Q.append(0)

# 始点となる頂点0への最短距離は0とする
dist[0] = 0

# 幅優先探索で各頂点への最短距離を求める
while len(Q) > 0:

    # キューの先頭の頂点を取り出してiとする
    i = Q.popleft()

    # 頂点iに隣接する頂点を順番に見る
    # 見ている頂点をjとする
    for j in G[i]:
        # jが未訪問だったとき、jへの最短距離を更新して、キューの末尾に追加する
        if dist[j] == -1:
            dist[j] = dist[i] + 1
            Q.append(j)

if dist[N-1] == 2:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')