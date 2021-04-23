A, R, N = map(int, input().split())

if R == 1:
    print(A)
    exit()

ans = A

for i in range(N-1):
    ans *= R
    if ans > 10**9:
        print('large')
        exit()

print(ans)