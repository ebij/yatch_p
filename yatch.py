# yatch.py
# ヨットの出る確率をモンテカルロ法で計算するプログラム
# 
import collections
import random

def diceCount(dice):
    # dice:現在のサイコロの状態
    # 返り値：[1の出目の個数, 2の出目の個数, 3の出目の個数, 4の出目の個数 ...]
    counter = collections.Counter(dice)
    # print(counter)
    dictlist = list()
    for i in range(1,7):
        dictlist.append(counter[i])
    # print(dictlist)
    return dictlist

def separateDices(dice):
    # キープするサイコロと振り直すサイコロを分ける
    # dice: 手持ちのサイコロの配列
    # keepdices: キープするサイコロの配列 
    
    #keepdices = dice
    counter = diceCount(dice)
    maxnum = max(counter)
    maxindex = counter.index(maxnum)+1
    keepdices = [maxindex for i in range(maxnum)]
    # print(f"maxnum:{maxnum}, maxindex:{maxindex}, keepdices:{keepdices}")
    return keepdices, 5-len(keepdices)

def rollDices(n):
    # n:サイコロの個数
    # 返り値：サイコロ出目の配列
    rolledDices = [random.randrange(1,6+1) for i in range(n)]
    return rolledDices

def main():

    loopN = 10
    k=0
    for i in range(loopN):
        # initialization
        dice = list()
        keepdices = list()
        # サイコロを振る
        newdice = rollDices(5)
        dice = keepdices + newdice
        print("1回目：",dice,end="  ")

        # カウントして残すサイコロを決定
        keepdices, n = separateDices(dice)

        # 2回目サイコロを振る
        newdice = rollDices(n)
        dice = keepdices + newdice
        print("2回目：",dice,end="  ")
        
        # カウントして残すサイコロを決定
        keepdices, n = separateDices(dice)
        
        # 3回目サイコロを振る
        newdice = rollDices(n)
        dice = keepdices + newdice
        print("3回目：",dice,end="  ")
        
        # カウントして判定
        _, n = separateDices(dice)

        if n == 0:
            k = k + 1
            print("○")
        else:
            print(f"{5-n}")

        # if i%1000 == 1 :
        #     print(i//1000, k/i)

    print(f"最終結果: {(k/loopN)*100}% (k={k},N={loopN})")


if __name__ == '__main__':
    main()
