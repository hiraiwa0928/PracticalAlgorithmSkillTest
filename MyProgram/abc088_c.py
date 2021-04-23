c = [list(map(int, input().split())) for i in range(3)]

a = [None] * 3
b = [None] * 3

for i in range(3):
    a[i] = min(c[i])

for i in range(3):
    b[i] = c[0][i] - a[0]

flag = True

for i in range(3):
    for j in range(3):
        if c[i][j] != a[i] + b[j]:
            flag = False

if flag:
    print('Yes')
else:
    print('No')