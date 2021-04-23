# WA
n = int(input())
c = list(map(int, input().split()))
q = int(input())

cnt = 0
c_all = sorted(c)

c_odd = []
for i in range(0, n, 2):
    c_odd.append(c[i])

c_odd.sort()

for i in range(q):

    s = list(map(int, input().split()))

    if s[0] == 1:

        s[1] -= 1

        if c[s[1]] >= s[2]:
            c[s[1]] -= s[2]
            cnt += s[2]

    if s[0] == 2:
        
        ac = n + 1
        wa = -1

        while ac-wa > 1:
            if c_odd[int(ac+wa/2)] >= s[1]:
                ac = int(ac+wa/2)
            else:
                wa = int(ac+wa/2)
        
        if ac == len(c_odd):
            cnt += len(c_odd) * s[1]

    if s[0] == 3:

        ac = n + 1
        wa = -1

        while ac-wa > 1:
            if c_all[int(ac+wa/2)] >= s[1]:
                ac = int(ac+wa/2)
            else:
                wa = int(ac+wa/2)
        
        if ac == len(c_all):
            cnt += len(c_all) * s[1]

print(cnt)