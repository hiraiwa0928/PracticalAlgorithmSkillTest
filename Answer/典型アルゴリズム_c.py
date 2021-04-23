N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

ALL = 1 << N
# cost[n][i]:訪れた都市の集合がnで、最後にいる年がiであるときのコスト最小値
cost = [[float('INF')]*N for _ in range(ALL)]

# 初期条件。最初にいるときの始点はnには含めない
cost[0][0] = 0

# nで表現される集合に要素iが含まれるかを判定してTrue/Falseを返す関数
def has_bit(n, i):
    return (n & 1<<i)

for n in range(ALL):
    for i in range(N):
        # iからjに移動する遷移を試す
        for j in range(N):
            # すでに訪問済みか、同じ都市は無視する
            if has_bit(n, j) or i == j:
                continue
            print(f'n:{n}, n|1<<j:{n|1<<j}, j:{j}')
            cost[n|1<<j][j] = min(cost[n|1<<j][j], cost[n][i] + A[i][j])

# 全都市を訪問して始点に戻ってくる最小コストが答え
print(cost[ALL-1][0])

# for i in range(ALL):
#     print(*cost[i])