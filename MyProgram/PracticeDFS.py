# 再起上限を増やす
import sys
sys.setrecursionlimit(1001001)

# 頂点数 N, 辺情報 E, 始点 s は定義済みとする

N, E, s = None

# N個のFalseで初期化した配列visitedを用意する
visited = []
for i in range(N):
    visited.append(False)

# 再起関数dfsを定義する
def dfs(i):
    visited[i] = True
    for j in E[i]:
        if not visited[j]:
            dfs(j)

# 始点から呼び出す
dfs(s)