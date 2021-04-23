n = int(input())

cnt = 0
now = 0

while(cnt != n):
    now = int(now)
    now += 1
    now = str(now)
    num = list(map(int, now))
    if len(num) == 1:
        cnt += 1
    else:
        judge_num = num[0]
        judge = True
        for i in range(1, len(num)):
            if judge_num != num[i]:
                judge = False
                break
        if judge:
            cnt += 1

print(now)