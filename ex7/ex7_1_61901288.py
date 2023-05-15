"""
ファイル名の00000000を学籍番号に置き換えて提出すること

演習1:
引数であるリストに含まれる要素のうち、
「空でないタプルの数」を返す関数 get_num_nonempty_tuples を作成

実行例:
test_list = [(), ("",), (2), (2, 3), ("Hello", "Good bye"), (True,)]
test_list = [(), ("",), (2,), (2, 3), ("Hello", "Good bye"), (True,)]
print(get_num_nonempty_tuples(test_list))

結果:
4
"""

def get_num_nonempty_tuples(tuples_list):
    result = 0
    for t in tuples_list:
        if type(t) == tuple and len(t)== 1 and t[0] == "":
            continue
        if type(t) != tuple and t != "":
            result += 1
            continue
        if type(t) == tuple and len(t) > 0:
            result += 1
    return result    