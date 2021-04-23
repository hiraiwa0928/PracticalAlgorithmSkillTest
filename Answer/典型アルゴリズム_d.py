import heapq

N, M = map(int, input().split())

# 隣接リストとしてグラフを作る
G = [[] for _ in range(N)]

for _ in range(M):
    u, v, c = map(int, input().split())

    # uからvへと、重みcの辺が張られているため
    # 行き先のvだけでなく、重みのcも入れておく
    G[u].append((v, c))

# 頂点0から各頂点への最短距離を保持する配列
# N個の-1で満たしておく(-1の場合は未訪問であることを表す)
dist = [-1] * N

# ダイクストラ法で使うヒープ
Q = []

# 始点となる頂点0をヒープに追加しておく
# (距離, 頂点)として追加する
heapq.heappush(Q, (0, 0))

# 始点となる頂点0への最短距離は0とする
dist[0] = 0

# ヒープから取り出したことがあるかを保存する配列
# 最初はN個のFalseで埋めておく
done = [False] * N

# ダイクストラ法で各頂点への最短距離を求める
while len(Q) > 0:

    # ヒープの先頭の頂点を取り出してiとする
    d, i = heapq.heappop(Q)

    # もし前にヒープから取り出したことがあれば、
    # 隣接する頂点を調べるのをスキップする
    if done[i]:
        continue
    
    # ヒープから頂点iを取り出したことを記録しておく
    done[i] = True

    # 頂点iに隣接する頂点を順番に見る
    # 見ている頂点をjtosuru
    # また、iからjへ移動する時に使う辺の重みをcとする
    for (j, c) in G[i]:

        # jが未訪問だったとき、あるいはjへの最短距離が行進可能だったとき、
        # jへの最短距離を更新して、ヒープの末尾に追加する
        if dist[j] == -1 or dist[j] > dist[i] + c:
            dist[j] = dist[i] + c
            heapq.heappush(Q, (dist[j], j))

print(dist[N-1])