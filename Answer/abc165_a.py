## 解法1
# K = int(input())
# A, B = map(int, input().split())

# ok = False

# for x in range(A, B+1):
#     if x%K == 0:
#         ok = True

# if ok:
#     print('OK')
# else:
#     print('NG')


# # 解法2
# K = int(input())
# A, B = map(int, input().split())

# # Kの倍数がA以上B以下の範囲の中にあるかどうかを記録する変数
# ok = False

# # Kの倍数を小さいほうから順番に調べる。
# # iを整数として、i*KがA以上B以下の範囲に入っているかを調べる
# for i in range(1000000 + 1):
#     # 調べたいKの倍数がBより大きかったら、そこでループを終了する
#     if i*K > B:
#         break

#     # 調べているKの倍数i*KがA以上B以下の範囲に入っているかを調べる
#     if A <= i*K <=B:
#         ok = True

# if ok:
#     print('OK')
# else:
#     print('NG')

# 解法3

K = int(input())
A, B = map(int, input().split())

ok = False

x = A // K
u = B // K

# x<u ならばKの倍数がA以上B以下の範囲の中にある
if x < u:
    ok = True

if A % K == 0:
    ok = True

if ok:
    print('OK')
else:
    print('NG')