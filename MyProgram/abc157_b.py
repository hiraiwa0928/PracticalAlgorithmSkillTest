a = [list(map(int, input().split())) for i in range(3)]
n = int(input())
judge = [[0]*3 for i in range(3)]

for i in range(n):
    b = int(input())
    flag = False
    for x in range(3):
        for y in range(3):
            if a[x][y] == b:
                judge[x][y] = 1
                flag = True
                break
        if flag:
            break

ans = False

for i in range(3):
    if judge[i] == [1, 1, 1]:
        ans = True

for i in range(3):
    if judge[0][i] == 1 and judge[1][i] == 1 and judge[2][i] == 1:
        ans = True

if judge[0][0] == 1 and judge[1][1] == 1 and judge[2][2] == 1:
    ans = True

if judge[2][0] == 1 and judge[1][1] == 1 and judge[0][2] == 1:
    ans = True

if ans:
    print('Yes')
else:
    print('No')