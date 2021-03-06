# 再帰上限を増やす
import sys
sys.setrecursionlimit(1001001)

N = int(input())
# child[i]:頂点iの子(部下)となる頂点たち
child = [[] for _ in range(N)]
for i in range(1, N):
    b = int(input())
    child[b-1].append(i)

# 再帰関数を定義
# dfs(i):頂点iのこの給料を全て求め、自身の給料を計算する
def dfs(i):
    # 子がいなければ1
    if len(child[i]) == 0:
        return 1
    else:
        values = []
        for j in child[i]:
            values.append(dfs(j))
        return max(values) + min(values) + 1

# 答えは頂点0の給料
print(dfs(0))