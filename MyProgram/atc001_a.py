import sys
sys.setrecursionlimit(1001001)

h, w = map(int, input().split())
si = sj = gi = gj = None
c = []
for i in range(h):
    c_tmp = list(map(str, input()))
    if 's' in c_tmp:
        si = i
        sj = c_tmp.index('s')
    if 'g' in c_tmp:
        gi = i
        gj = c_tmp.index('g')
    c.append(c_tmp)

visited = [[False]*w for i in range(h)]

def dfs(i, j):
    visited[i][j] = True
    for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        if not (0<=i2<h and 0<=j2<w):
            continue
        if c[i2][j2] == '#':
            continue
        if not visited[i2][j2]:
            dfs(i2, j2)

dfs(si, sj)

if visited[gi][gj]:
    print('Yes')
else:
    print('No')