N = int(input())

cnt = 0

for A in range(1, N+1):
    for B in range(A, N+1):
        C = N - A * B
        if C > 0:
            if A != B:
                cnt += 2
            else:
                cnt += 1
        else:
            break

print(cnt)