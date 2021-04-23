A = [list(map(int, input().split())) for i in range(3)]
M = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(False)
    M.append(row)

N = int(input())
for _ in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                M[i][j] = True

bingo = False

for i in range(3):
    # i行目の3津に印がついているか調べる
    # 印がついていたらビンゴ達成となる
    if M[i][0] and M[i][1] and M[i][2]:
        bingo = True

for i in range(3):
    # i列目の3つに印が付いているか調べる
    # 印がついていたらビンゴ達成となる
    if M[0][i] and M[1][i] and M[2][i]:
        bingo = True

# 左上から右下にかけて、斜めに3つ印がついているか調べる
if M[0][0] and M[1][1] and M[2][2]:
    bingo = True

# 右上から左下にかけて、斜めに3つ印がついているか調べる
if M[0][2] and M[1][1] and M[2][0]:
    bingo = True

if bingo:
    print('Yes')
else:
    print('No')