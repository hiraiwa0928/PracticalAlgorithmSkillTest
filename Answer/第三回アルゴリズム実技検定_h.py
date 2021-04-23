N, L = map(int, input().split())
X = list(map(int, input().split()))
T1, T2, T3 = map(int, input().split())

# ハードルがある座標においてTrueとなるような配列
H = [False]*(L+1)
for i in X:
    H[i] = True

# cost[i]:座標iで行動を終了するまでの最小所要時間
# 非常に大きな値で初期化しておき、minを用いて更新する
cost = [1001001001] * (L+1)

cost[0] = 0

# 順番に求めていく
for i in range(1, L+1):
    # 行動1
    cost[i] = min(cost[i], cost[i-1] + T1)
    # 行動2
    if i >= 2:
        cost[i] = min(cost[i], cost[i-2] + T1 + T2)
    # 行動3
    if i >= 4:
        cost[i] = min(cost[i], cost[i-4] + T1 + 3*T2)
    # もしハードルがあれば加算
    if H[i]:
        cost[i] += T3
    
# 答えは座標Lにぴったり止まるか、座標(L-3)~(L-1)からジャンプ中にゴールしたもの
ans = cost[L]

if L-1 >= 0:
    # L-1の地点で行動2をした場合
    ans = min(ans, cost[L-1] + T1//2 + T2//2)
if L-2 >= 0:
    # L-2の地点で行動3をした場合
    ans = min(ans, cost[L-2] + T1//2 + int(1.5*T2))
if L-3 >= 0:
    # L-3の地点で行動3をした場合
    ans = min(ans, cost[L-3] + T1//2 + int(2.5*T2))

print(ans)