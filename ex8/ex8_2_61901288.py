"""
ファイル名の00000000を学籍番号に置き換えて提出すること

"""

"""
演習2-1:
2つの辞書in_dict1, in_dict2を引数とし、
それぞれの辞書の要素 (keyは文字列, valueは整数)を統合し1つの辞書として返す関数 merge_dict を作成
ただし、in_dict1とin_dict2に同じkeyを持つ要素がある場合、
それらのvalueの値を加算したものを統合後の辞書のvalueとすること

実行例:
dict1 = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
dict2 = {'a': 4, 'b': 5, 'e': 6, 'f': 7}
print(merge_dict(dict1, dict2)) # {'a': 4, 'b': 6, 'c': 2, 'd': 3, 'e': 6, 'f': 7}
"""


def merge_dict(in_dict1, in_dict2):
    d1 = in_dict1.copy()
    for k, v in in_dict2.items():
        if k in d1:
            d1[k] += v
        else:
            d1[k] = v
    return d1


"""
演習2-2:
辞書in_dict (各要素のkeyは文字列, valueは整数), 整数 threshold を引数とし、
辞書内の要素の各keyについて昇順に以下の繰り返し処理を行う関数show_deleted_dict()を作成
(1) key, in_dictを表示する
(2) keyに対応する要素のvalueがthreshold未満の場合、in_dictからその要素を削除する

実行例:
in_dict = {'a': 4, 'b': 6, 'c': 2, 'd': 3, 'e': 6, 'f': 7}
threshold = 5
show_deleted_dict(in_dict, threshold)
# a {'a': 4, 'b': 6, 'c': 2, 'd': 3, 'e': 6, 'f': 7}
# b {'b': 6, 'c': 2, 'd': 3, 'e': 6, 'f': 7}
# c {'b': 6, 'c': 2, 'd': 3, 'e': 6, 'f': 7}
# d {'b': 6, 'd': 3, 'e': 6, 'f': 7}
# e {'b': 6, 'e': 6, 'f': 7}
# f {'b': 6, 'e': 6, 'f': 7}
"""


def show_deleted_dict(in_dict, threshold):
    for k, v in sorted(in_dict.items()):
        print(k, in_dict)
        if v < threshold:
            del in_dict[k]
        else:
            continue
