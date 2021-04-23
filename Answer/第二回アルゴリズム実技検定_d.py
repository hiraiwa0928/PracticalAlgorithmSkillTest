# 文字列Tが文字列Sにマッチするかどうかを判定する関数
# マッチするときはTrueを、マッチしないときはFalseを返す
def is_match(T, S):
    
    # Sのi文字目から始まる部分がTとマッチするかどうか調べる
    for i in range(len(S) - len(T) + 1):

        # Sのi文字目から始まる部分が
        # Tとマッチしているかどうかを保持する変数
        ok = True

        # Tのj文字目と、Sのi+j文字目を見比べる
        for j in range(len(T)):

            # Tのj文字目がSのi+j文字目と異なっていて、
            # かつ、Tのj文字目が'.'でもない場合、
            # Sのi文字目から始まる部分はTとマッチしない
            if S[i+j] != T[j] and T[j] != '.':
                ok = False
        
        # Sのi文字目から始まる部分がTマッチしている場合
        if ok:
            return True

    # Sの全ての部分についてTとマッチしなかった場合、Falseを返す
    return False

S = input()

# 使える文字の一覧
C = 'abcdefghijklmnopqrstuvwxyz.'

# 文字列Sとマッチする文字列を保持する配列
M = []

# 長さ1の文字列を全て調べ、SとマッチするものをMに入れる
for T in C:
    if is_match(T, S):
        M.append(T)

# 長さ2の文字列を全て調べ、SとマッチするものをMに入れる
for c1 in C:
    for c2 in C:
        T = c1 + c2
        if is_match(T, S):
            M.append(T)

# 長さ3の文字列を全て調べ、SとマッチするものをMに入れる
for c1 in C:
    for c2 in C:
        for c3 in C:
            T = c1 + c2 + c3
            if is_match(T, S):
                M.append(T)

print(len(M))