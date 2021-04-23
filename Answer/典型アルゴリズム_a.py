import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))

ok = bisect.bisect_left(A, K)

if ok == N:
    print(-1)
else:
    print(ok)