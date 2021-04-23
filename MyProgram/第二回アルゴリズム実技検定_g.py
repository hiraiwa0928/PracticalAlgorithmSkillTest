# WA

Q = int(input())

alpha = 'abcdefghijklmnopqrstuvwxyz'

have = {}
use = {}

for ele in alpha:
    have[ele] = 0

for ele in alpha:
    use[ele] = 0

s = []

for _ in range(Q):

    ans = 0

    query = list(map(str, input().split()))

    # 命令1のとき
    if query[0] == '1':
        if len(s) == 0:
            s.append(query[1])
        else:
            if not (s[-1] == query[1]):
                s.append(query[1])

        have[query[1]] += int(query[2])
    # 命令2のとき
    else:
        D = int(query[1])
        useStr = []
        # 先頭のD個の文字を取り終わるか、文字列sが空になったら終了
        while D > 0 and len(s) != 0:
            s_tmp = s[0]
            # 先頭からD個目の文字がすべて同じ場合
            if have[s_tmp] >= D:
                if have[s_tmp] == D:
                    s = s[1:]
                use[s_tmp] += D
                have[s_tmp] -= D
                useStr.append(s_tmp)
                break
            # 複数の文字を削除する場合
            else:
                D -= have[s_tmp]
                use[s_tmp] += have[s_tmp]
                have[s_tmp] = 0
                useStr.append(s_tmp)
                s = s[1:]
            
        useStr = set(useStr)
        for ele in useStr:
            ans += use[ele] ** 2
            use[ele] = 0
        print(ans)