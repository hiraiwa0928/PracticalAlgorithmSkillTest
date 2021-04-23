import math

N = int(input())

# N番目のゾロ目数の桁数
x = math.ceil(N/9)

# N番目のゾロ目数の数
y = N%9

if y == 0:
    y = 9

ans = ''

for i in range(x):
    ans += str(y)

print(ans)