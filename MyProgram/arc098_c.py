N = int(input())
S = list(map(str, input()))

W = [0]

for i in range(N):
    if S[i] == 'W':
        W.append(W[i] + 1)
    else:
        W.append(W[i])

E = [0]

for i in range(N):
    if S[N-i-1] == 'E':
        E.append(E[i] + 1)
    else:
        E.append(E[i])

ans = []

for i in range(1, N+1):
    ans.append(W[i-1] + E[N-i])

print(min(ans))