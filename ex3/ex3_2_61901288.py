"""
ファイル名の00000000を学籍番号に置き換えて提出すること

演習: ユーザー入力と型変換
"""

"""
以下の仕様を満たすプログラムを作成せよ
1. 実行後、ユーザーの入力を待つ
2. ユーザーが自然数を入力後、リターンキーを入力したら、もう一度ユーザーの入力を待つ
3. 再度ユーザーが自然数を入力後、リターンキーを入力したら、「始めに入力された数字の2乗と後に入力された数字の2乗を足したもの」をprintし、プログラムを終了させる

注意: 採点はプログラムに任意の入力を与え、プログラムが最後にprintする出力を比べて行う。従って、余計なprintは行わないこと
"""
a = int(input())
b = int(input())
print(a**2 + b**2)

