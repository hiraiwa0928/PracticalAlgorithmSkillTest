from collections import deque

num = 200 + 1

n, x, y = map(int, input().split())
xy = [list(map(lambda x: int(x)+num, input().split())) for i in range(n)]

x += num
y += num

dist = [[-1]*(num*2+1) for i in range(num*2+1)]

Q = deque()
Q.append([num, num])
dist[num][num] = 0

while len(Q) > 0:

    i, j = Q.popleft()

    for i2, j2 in [[i+1, j+1], [i, j+1], [i-1, j+1], [i+1, j], [i-1, j], [i, j-1]]:
        if not (0<=i2<=num*2 and 0<=j2<=num*2):
            continue
        if [i2, j2] in xy:
            continue
        if dist[i2][j2] == -1:
            dist[i2][j2] = dist[i][j] + 1
            Q.append([i2, j2])

print(dist[x][y])