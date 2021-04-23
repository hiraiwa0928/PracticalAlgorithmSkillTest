# WA
def act1():
    global nowPlace, time
    if nowPlace in x or nowPlace+1 in x:
        time += t[0] + t[2]
    else:
        time += t[0]
    nowPlace += 1

def act2():
    global nowPlace, time
    if nowPlace+2 in x:
        time += t[0] + t[2]
    else:
        time += t[0]
    time += t[1]
    nowPlace += 2

def act3():
    global nowPlace, time
    if nowPlace+4 in x:
        time += t[0] + t[2]
    else:
        time += t[0]
    time += 3*t[2]
    nowPlace += 4

n, l = map(int, input().split())
x = list(map(int, input().split()))
t = list(map(int, input().split()))

nowPlace = 0
time = 0

run = False
jump = False

# 走るかジャンプをするかどちらが早いのか判定
if t[0] > t[1]:
    jump = True
else:
    run = True

while l > nowPlace:
    if run:
        if nowPlace+1 not in x:
            act1()
        else:
            act2()
    if jump:
        pass

print(time)