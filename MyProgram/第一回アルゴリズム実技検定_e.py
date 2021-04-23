import copy

n, q = map(int, input().split())
judge = [['N'] * n for i in range(n)]

for i in range(q):

    s = list(map(int, input().split()))

    if s[0] == 1:

        s[1] -= 1
        s[2] -= 1

        judge[s[1]][s[2]] = 'Y'

    elif s[0] == 2:
        
        s[1] -= 1

        for i in range(n):
            if s[1] == i:
                continue
            if judge[i][s[1]] == 'Y':
                judge[s[1]][i] = 'Y'

    elif s[0] == 3:
        
        s[1] -= 1
        now_follow = copy.copy(judge[s[1]])

        for i in range(n):
            if now_follow[i] != 'Y' or i == s[1]:
                continue
            for j in range(n):
                if s[1] == j:
                    continue
                if judge[i][j] == 'Y':
                    judge[s[1]][j] = 'Y'
    
for ele in judge:
    print(*ele, sep = '')