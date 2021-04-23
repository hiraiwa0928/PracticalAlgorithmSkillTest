from collections import deque

H, W = map(int, input().split())
A = [list(map(str, input())) for _ in range(H)]

mod = 10**9 + 7

Q = deque()

Q.append((0, 0))

cnt = 0

while len(Q) > 0:

    i, j = Q.popleft()

    for i2, j2 in [[i+1, j], [i, j+1]]:
        if not (0<=i2<H and 0<=j2<W):
            continue
        if A[i2][j2] == '#':
            continue
        if i2 == H-1 and j2 == W-1:
            cnt  = (cnt + 1) % mod
        else:
            Q.append((i2, j2))

print(cnt)