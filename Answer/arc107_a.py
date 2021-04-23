A, B, C = map(int, input().split())

mod = 998244353

numA = (A*(1 + A)//2) % mod
numB = (B*(1 + B)//2) % mod
numC = (C*(1 + C)//2) % mod

ans = (numA * numB * numC) % mod

print(ans)