"""
ファイル名の00000000を学籍番号に置き換えて提出すること

例題:
引数として与えられた要素として整数を持つリストに対し、
先頭から要素を調べ、今まで調べた要素の中で最も小さい値の場合、
その値 (value) を"Find min: (value)"の形式で表示する関数 find_min を作成
ただし、引数の先頭の要素は必ず"Find min: (value)"の形式で表示すること

実行例:
test_ints = [3, 8, 2, 4, -1, -5, 3, -8]
find_min(test_ints)

結果:
Find min: 3
Find min: 2
Find min: -1
Find min: -5
Find min: -8
"""

def find_min(ints):
    def _print_min(elem):
        print("Find min:", elem)
        
    min_value = None
    for i in ints:
        if min_value is None or min_value > i:
            _print_min(i)
            min_value = i