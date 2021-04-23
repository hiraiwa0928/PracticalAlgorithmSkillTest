A, B, X = map(int, input().split())

ac = 0
wa = 10**9 + 1

while wa-ac > 1:
    checkNum = int((ac+wa)/2)
    if X >= A*checkNum + B*len(str(checkNum)):
        ac = checkNum
    else:
        wa = checkNum

print(ac)