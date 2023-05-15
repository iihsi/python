"""
ファイル名の00000000を学籍番号に置き換えて提出すること

演習1: 以下の関数をDocstringに従って完成させよ
"""


def find_even(min_num, max_num):
    """min_num以上, max_num以下の整数の中から最小の偶数を返す関数

    min_num以上, max_num以下の整数の中から最小の偶数を1つ返す。もし範囲内に偶数がない場合はNoneを返す

    Args:
        min_num (int): 最小の偶数を探すときの範囲の最小値
        max_num (int): 最小の偶数を探すときの範囲の最大値

    Returns:
        int or None: 範囲内の最小の偶数。見つからないばあいはNone

    """
    for i in range(min_num, max_num + 1):
            if i%2 == 0:
                return i
    return None