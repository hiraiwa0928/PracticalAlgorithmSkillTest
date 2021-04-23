N = int(input())
S = input()

# 向きを変える必要がある人数の最小値を保持する変数
# 答えになりえない大きい値で初期化しておく
min_turn = float('INF')

sum_W = [0]

for i in range(N):
    if S[i] == 'W':
        sum_W.append(sum_W[i] + 1)
    else:
        sum_W.append(sum_W[i])

for i in range(N):

    # リーダーiより西側にいて西を向いている人の数
    w = sum_W[i]

    # リーダーiより東側にいて東を向いている人の数
    e = (N - 1 - i) - (sum_W[N] - sum_W[i + 1])

    # 人iをリーダーとした時の
    # 向きを変える必要がある人数
    turn = w + e
    
    # リーダーiの場合について数え終わったら
    # 向きを変える必要がある人数の最小値を更新する
    min_turn = min(min_turn, turn)

print(min_turn)