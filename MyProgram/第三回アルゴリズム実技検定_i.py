# WA TLE
N = int(input())
Q = int(input())

H = []
W = []
for i in range(N):
    H.append(i)
    W.append(i)

Transpose = False

for _ in range(Q):

    query = list(map(int, input().split()))

    if query[0] == 1:
        a = query[1] - 1
        b = query[2] - 1
        if Transpose:
            W[a], W[b] = W[b], W[a]
        else:
            H[a], H[b] = H[b], H[a]
    elif query[0] == 2:
        a = query[1] - 1
        b = query[2] - 1
        if Transpose:
            H[a], H[b] = H[b], H[a]
        else:
            W[a], W[b] = W[b], W[a]
    elif query[0] == 3:
        if Transpose:
            Transpose = False
        else:
            Transpose = True
    else:
        a = query[1] - 1
        b = query[2] - 1
        if Transpose:
            ans = N * W[a] + H[b]
        else:
            ans = N * H[a] + W[b]
        print(ans)