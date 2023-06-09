"""
ファイル名の00000000を学籍番号に置き換えて提出すること

演習3: 再帰呼び出し
1~nまでの数字の合計値を、for文を使わずに求める関数sum_ex()を完成させよ

ヒント: sum_ex()の中でsum_ex()を呼出すことが可能
"""


def sum_ex(n):
    """1~nまでの数字の合計値を、for文を使わずに求める関数

    Args:
        n (int): 合計したい数字の最大値

    Returns:
        int: 合計値

    """
    if n == 1:
        return n
    return n + sum_ex(n-1)