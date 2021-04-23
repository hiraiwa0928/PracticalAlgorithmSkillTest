def dfs(i, j):
    visited[i][j] = True
    # 4方向の隣マスを探索する。
    for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        # もし盤面の範囲内でなければ無視する
        if not (0<=i2<h and 0<=j2<w):
            continue
        if c[i2][j2] == '#':
            continue
        if not visited[i2][j2]:
            dfs(i2, j2)

# 再起上限を増やす
import sys
sys.setrecursionlimit(1001001)

h, w = map(int, input().split())

# 始点と終点の座標を探し、それぞれ(si, sj)と(gi, gj)とする
si = sj = gi = gj = None
c = []
for i in range(h):
    tmp = list(map(str, input()))
    if 's' in tmp:
        si = i
        sj = tmp.index('s')
    if 'g' in tmp:
        gi = i
        gj = tmp.index('g')
    c.append(tmp)

# 訪問済みかどうかを管理する2次元配列
visited = [[False]*w for i in range(h)]

# 始点から呼び出す
dfs(si, sj)

if visited[gi][gj]:
    print('Yes')
else:
    print('No')