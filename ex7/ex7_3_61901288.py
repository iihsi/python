"""
ファイル名の00000000を学籍番号に置き換えて提出すること

演習3: 数字ピラミッド
以下の仕様を満たすような数字のピラミッドをprintする関数pyramid_numを作成せよ
- ピラミッドのn段目の数字の個数はn個
- ピラミッドはn = 1から始まるとし、1段目1番目の数字は1とする
- n >= 2 段目以降において
  - n 段目のm番目の数字は、n-1段目のm-1番目の数字とm番目の数字を足したものとする
  - n-1段目のm-1番目やm番目の数字が存在しない場合は、そこは0として計算する

関数自体の仕様は以下の通りとする
- pyramid_num()の引数はint型1つとし、引数に渡した数nに応じたn段の数字のピラミッドを作成する
- ピラミッドをprintする際は、1段ごとに改行し、数字と数字は半角スペースで区切る
  - 各段の最後の数字の後ろには何もprintしてはいけないが、例外として半角スペースが1つあっても良いとする
- 引数がint型でない場合、もしくは0以下の場合は何もprintせずに終了する
- 返り値は特に気にしなくて良い

採点は関数をこちらで呼びだして行うので、関数名の間違いなどには十分注意すること

実行例:
pyramid_num(6)

結果:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
"""

def pyramid_num(n:int):
    if type(n) != int:
        return
    if n<= 0:
        return
    
    pyramids = []
    for i in range(n):
        if i == 0:
            pyramids.append([1])
            continue
        
        pyramids.append([])
        for j in range(i+1):
            tmp = 0
            if j-1 < 0:
                tmp = 0 + pyramids[i-1][j]
            elif j >= len(pyramids[i-1]):
                tmp = pyramids[i-1][j-1] + 0
            else:
                tmp = pyramids[i-1][j-1] + pyramids[i-1]
            pyramids[i].append(tmp)
            
    for i in range(n):
        for j in range(i+1):
            print(pyramids[i][j], end=" ")
        print("")
        