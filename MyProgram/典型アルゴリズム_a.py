N, K = map(int, input().split())
A = list(map(int, input().split()))

ac = N
wa = -1

while ac-wa > 1:
    x = int((ac+wa)/2)
    if A[x] >= K:
        ac = x
    else:
        wa = x

if ac == N:
    ac = -1

print(ac)