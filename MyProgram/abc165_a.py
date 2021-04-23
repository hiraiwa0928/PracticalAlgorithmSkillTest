k = int(input())
a, b = map(int, input().split())

judge = False

for i in range(a, b+1):
    if i%k == 0:
        judge = True
        break

if judge:
    print('OK')
else:
    print('NG')