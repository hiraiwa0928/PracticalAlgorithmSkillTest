ABC = list(map(int, input().split()))
ABC.sort()

mod = 998244353

n1, n2, n3 = 0, 0, 0

for i in range(1, ABC[0]+1):
    n1 = (n1 + i) % mod

n2 = n1

for i in range(ABC[0]+1, ABC[1]+1):
    n2 = (n2 + i) % mod

n3 = n2

for i in range(ABC[1]+1, ABC[2]+1):
    n3 = (n3 + i) % mod

ans = (n1*n2*n3) % mod

print(ans)