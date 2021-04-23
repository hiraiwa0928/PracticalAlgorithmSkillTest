n = int(input())
h = list(map(int, input().split()))

# cost[i]:足場iに辿り着く為の最小コスト。サイズNを確保する
cost = [0] * n

# 初期設定
cost[0] = 0
# 2つ目の足場はジャンプ元が1通り
cost[1] = abs(h[1] - h[0])
# それ以降の足場はジャンプ元が2通りあるため、コストが小さいほうを採用する
for i in range(2, n):
    cost[i] = min(cost[i-1] + abs(h[i]-h[i-1]), cost[i-2] + abs(h[i]-h[i-2]))

# 答えは最後の足場までの最小コスト
print(cost[n-1])