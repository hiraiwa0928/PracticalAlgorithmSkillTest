N, M = map(int, input().split())
A = []
for _ in range(M):
    a = int(input())
    A.append(a)

# N = 1のとき
if N == 1:
    print(1)
    exit()

mod = 10**9 + 7

stair = [0] * (N+1)

# 初期条件
if 1 in A and 2 in A:
    print(0)
    exit()
elif 1 in A:
    stair[1] = 0
    stair[2] = 1
elif 2 in A:
    stair[1] = 1
    stair[2] = 0
else:
    stair[1] = 1
    stair[2] = 2

NG = -1
NGIndex = -1

for i in range(M):
    if A[i] >= 3:
        NG = A[i]
        NGIndex = i
        break
    else:
        continue

for i in range(3, N+1):
    if i == NG:
        if M > NGIndex + 1:
            NGIndex += 1
            NG = A[NGIndex]
        continue
    stair[i] = (stair[i-1] + stair[i-2]) % mod

print(stair[N])