N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort()

now = 1
nowIndex = 0

ans = 0

while True:

    minTime = float('INF')
    selectIndex = -1

    for i in range(nowIndex, len(AB)):
        if minTime > AB[i][1] - now:
            minTime = AB[i][1] - now
            selectIndex = i
    
    if minTime == float('INF'):
        break
    else:
        ans += 1
    
    now = AB[selectIndex][1] + 1

    tmpNowIndex = nowIndex

    for i in range(tmpNowIndex, len(AB)):
        if AB[i][0] >= now:
            nowIndex = i
            break
    
    if nowIndex == tmpNowIndex:
        break

print(ans)