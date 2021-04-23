from collections import deque

k = int(input())

Q = deque()
[Q.append(i) for i in range(1, 10)]

ans = []
for _ in range(k):
    num = Q.popleft()
    ans.append(num)

    for i in range(-1, 2):
        add = num%10 + i
        if 0<=add<=9:
            Q.append(10*num+add)

print(ans[k-1])