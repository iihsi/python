"""
ファイル名の00000000を学籍番号に置き換えて提出すること

演習: 二分探索

arrayは数字が小さい順にソート済みの配列である

コンソールから入力した数字を探し出し、その位置(=配列のインデックス)を
printし、見つからなければ「見つかりませんでした」とprintするよう、
?を適切に埋めよ

探索方法は、
- 探索範囲の中心と探したい数字を比較し、
- 配列の中心が探したい数字より大きければ中心より左側を、
- そうでなければ中心より右側を新たな探索範囲とする
- 新たな探索範囲に対して、同じ処理を繰り返す

ような形となる
"""

array = [1, 2, 4, 7, 10, 12, 15, 16, 20, 22, 25, 27, 30, 31]
target = int(input())


# 初期探索範囲は配列の左端から右端まで
left_index = 0
right_index = len(array) - 1

while True:
    # 探索範囲がなくなったとき、数字は見つからなかったものとする
    if (left_index > right_index):
        print('見つかりませんでした')
        break

    center_index = int((left_index + right_index) / 2)
    if target < array[center_index]:
        right_index = center_index - 1
    elif target > array[center_index]:
        left_index = center_index + 1
    else:
        # 探索終了
        print(center_index)
        break
