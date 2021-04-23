# dequeを使えるようにする
from collections import deque

# 頂点数 N, 辺情報 E, 始点 sは定義済みとする
N, E, s = None, None, None

# N個のFalseで初期化した配列visitedを用意する
visited = []
for i in range(N):
    visited.append(False)

# キューを用意する
Q = deque()
Q.append(s)
visited[s] = True

# キューから取り出しながら探索する
while len(Q) > 0:
    i = Q.popleft()
    for j in E[i]:
        if not visited[j]:
            visited[j] = True
            Q.append(j)