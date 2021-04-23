import sys
sys.setrecursionlimit(1001001001)

N = int(input())
h = list(map(int, input().split()))

done = [False] * N
cost = [0] * N

def dfs(i):
    if done[i]:
        return cost[i]
    if i == 0:
        cost[i] = 0
    elif i == 1:
        cost[i] = dfs(0) + abs(h[1] - h[0])
    else:
        cost[i] = min(dfs(i-1) + abs(h[i] - h[i-1]), dfs(i-2) + abs(h[i] - h[i-2]))
    done[i] = True
    return cost[i]

print(dfs(N-1))