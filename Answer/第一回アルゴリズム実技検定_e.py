N, Q = map(int, input().split())

# FalseのNxNの2次元配列を作る
graph = []
for i in range(N):

    # 長さNのFlaseの1次元配列を作る
    row = []
    for j in range(N):
        row.append(False)
    
    # 長さNのFalseの1次元配列をgraphに追加する
    graph.append(row)

# Q個の操作を受け取る
for i in range(Q):
    query = list(map(int, input().split()))

    # 頂点番号は-1する
    a = query[1] - 1

    # 「フォロー」の操作の場合
    if query[0] == 1:

        # 頂点番号は-1する
        b = query[2] - 1

        # aからbへと辺を張る
        graph[a][b] = True
    
    # 「フォロー全返し」の宗さん場合
    if query[0] == 2:

        # 全ての頂点を番号に見る。見ている頂点をvとする
        for v in range(N):

            # 頂点vから頂点aへと辺があるとき
            if graph[v][a]:

                # 頂点aから頂点vへと辺を張る
                graph[a][v] = True
    
    # 「フォローフォロー」の操作の場合
    if query[0] == 3:

        # 頂点aから辺を張る予定の頂点のリスト
        to_follow = []

        # 全ての頂点を順番に見る。見ている頂点をvとする
        for v in range(N):

            # 頂点aから頂点vへと辺があるとき
            if graph[a][v]:

                # さらに全ての頂点を順番に見る。見ている頂点をwとする
                for w in range(N):

                    # 頂点vから頂点wへと辺があり、かつwがaではないとき
                    if graph[v][w] and w != a:

                        # あとで頂点aから辺を張るために記録しておく
                        to_follow.append(w)
        
        # 頂点aから辺を張る
        for w in to_follow:
            graph[a][w] = True

# 隣接行列を全て出力する
for i in range(N):
    for j in range(N):

        # iからjへと辺がある場合はYを、辺がない場合はNを出力する。改行はしない
        if graph[i][j]:
            print('Y', end = '')
        else:
            print('N', end = '')
    
    # N文字出力するごとに改行
    print()