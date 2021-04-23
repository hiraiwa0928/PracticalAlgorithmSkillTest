n, m, q = map(int ,input().split())
u, v = [], []
for i in range(m):
    n1, n2 = map(int, input().split())
    u.append(n1)
    v.append(n2)
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(q)]

connect = [[] for i in range(n)]
for i in range(m):
    connect[u[i]-1].append(v[i])

for i in range(m):
    connect[v[i]-1].append(u[i])

for i in range(q):
    print(c[s[i][1] - 1])
    if s[i][0] == 1:
        for j in connect[s[i][1] - 1]:
            c[j-1] = c[s[i][1] - 1]
    else:
        c[s[i][1] - 1] = s[i][2]