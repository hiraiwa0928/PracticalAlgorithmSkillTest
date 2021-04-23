import heapq

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v, c = map(int, input().split())
    G[u].append((c, v))
    G[v].append((c, u))

marked = [False] * N

marked_count = 0

Q = []

for c, j in G[0]:
    heapq.heappush(Q, (c, j))

marked[0] = True

marked_count += 1

sum = 0

while marked_count < N:
    
    c, i = heapq.heappop(Q)
    if marked[i]:
        continue

    marked[i] = True
    marked_count += 1

    sum += c

    for c, j in G[i]:

        if marked[j]:
            continue

        heapq.heappush(Q, (c, j))

print(sum)