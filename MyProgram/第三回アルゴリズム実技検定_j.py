N, M = map(int, input().split())
A = list(map(int, input().split()))

childEat = [0] * N

for i in range(M):

    ok = N
    ng = -1

    while ok-ng > 1:
        judge = int((ok+ng)/2)
        if A[i] > childEat[judge]:
            ok = judge
        else:
            ng = judge
    
    if ng == N-1:
        print('-1')
    else:
        childEat[ok] = A[i]
        print(ok+1)