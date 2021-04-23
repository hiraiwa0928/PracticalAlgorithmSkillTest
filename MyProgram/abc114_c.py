# 入力された数字を三進法に変換する
# 各位の数字が0ならば3、1ならば5、2ならば7に変換する
def change(n):
    n_3 = []
    while n > 0:
        n_3.append(n%3)
        n = int(n/3)
    n_3.reverse()

    retNum = 0
    d = len(n_3)-1

    for i in range(len(n_3)):
        if n_3[i] == 0:
            n_3[i] = 3
        elif n_3[i] == 1:
            n_3[i] = 5
        else:
            n_3[i] = 7
        retNum += n_3[i] * 10**d
        d -= 1
    
    return str(retNum)

n = int(input())

digit = len(str(n))
ans = []

# 3,5,7の数字が存在する最小の桁数である3から
# 入力された数字の桁数までの解となる数字を探していく
for d in range(3, digit+1):
    for i in range(3**(d)-1, 3**(d+1)+1):
        judgeNum = change(i)
        judgeNum = judgeNum[-d:]
        if '3' in judgeNum and '5' in judgeNum and '7' in judgeNum:
            if n >= int(judgeNum):
                ans.append(int(judgeNum))

print(len(set(ans)))