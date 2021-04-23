N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort()

disp = 0
ok = 0

for n in range(1, N+1):

    for i in range(ok, len(AB)):
        if n >= AB[i][0]:
            ok = i
        else:
            break
    
    pointMax = -float('INF')

    sel = -1
    
    for i in range(ok + 1):
        if AB[i][1] > pointMax:
            pointMax = AB[i][1]
            sel = i
    
    AB.pop(sel)
    disp += pointMax

    if ok != 0:
        ok -= 1

    print(disp)