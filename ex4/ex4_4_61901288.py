"""
ファイル名の00000000を学籍番号に置き換えて提出すること
"""

"""
演習4 発展課題
2~100の間の数で素数をすべて見つけ出し、printせよ
ヒント: 2重ループ

結果は

2
3
...

となっていれば良い
"""

for n in range(2,101):
    flag = True
    for m in range(2,n):
        if n % m == 0 :
            flag = False
            break
    if flag == True :
        print(n)
        