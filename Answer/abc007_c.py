from collections import deque

r, c = map(int, input().split())
sy, sx = map(lambda x: int(x)-1, input().split())
gy, gx = map(lambda x: int(x)-1, input().split())
s = [list(map(str, input())) for i in range(r)]

# 始点からの最小移動回数を管理する2次元配列。-1であれば未訪問であることを表す
dist = [[-1]*c for i in range(r)]

# キューを用意して、始点を入れる
Q = deque()
Q.append([sy, sx])
dist[sy][sx] = 0

# キューから取り出しながら探索する
while len(Q) > 0:
    i, j = Q.popleft()
    # 4津の隣マスを確認する
    for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        # もし盤面の範囲内でなければ無視する
        if not (0<=i2<=r and 0<=j2<=c):
            continue
        # もし壁マスであれば無視する
        if s[i2][j2] == '#':
            continue
        # もし未訪問(dist[i2][j2]が-1)であれば、距離を更新してキューに入れる
        if dist[i2][j2] == -1:
            dist[i2][j2] = dist[i][j] + 1
            Q.append([i2, j2])

# 始点から終点までの最小移動回数を出力
print(dist[gy][gx])