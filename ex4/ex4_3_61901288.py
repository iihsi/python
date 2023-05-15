"""
ファイル名の00000000を学籍番号に置き換えて提出すること

演習3: コンソールから整数を繰り返し受け取り、合計が10以上になったら合計値を表示して終了するプログラムを作成せよ

採点時は任意の入力を与えてprintされた合計値が正しいがどうかを確認するので、余計な文字列をprintしないように注意
"""

max_value = 10
sum_value = 0

while sum_value < max_value :
    sum_value += int(input())
print(sum_value)