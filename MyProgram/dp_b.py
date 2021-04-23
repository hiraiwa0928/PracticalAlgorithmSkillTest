n, k = map(int, input().split())
h = list(map(int, input().split()))

cost = [1001001001] * n

cost[0] = 0
cost[1] = abs(h[1] - h[0])

for i in range(2, n):
    for j in range(1, k+1):
        if i < j:
            break
        cost[i] = min(cost[i-j] + abs(h[i] - h[i-j]), cost[i])

print(cost[n-1])