"""
ファイル名の00000000を学籍番号に置き換えて提出すること
"""

"""
例題1-1:
複数のタプル (key, value) を要素に持つリストを引数とし、
辞書型に変換して返す関数 gen_dict を作成
なお、要素となるタプルにkeyの重複はないものとする

実行例:
tuples =  [('a', 0), ('b', 1), ('c', 2), ('d', 3)]
print(gen_dict(tuples)) #  {'a': 0, 'b': 1, 'c': 2, 'd': 3}
"""


def gen_dict(tuples):
    return(dict(tuples))


"""
例題1-2:
keyを英字小文字の文字列, valueを整数とする要素を持つ辞書を引数とし、
各要素のkeyの文字列を大文字とし、valueの値の正負の符号を反転させた辞書を返す関数 convert_up_neg を作成

備考:
文字列を大文字に変換したものを返す関数 upper
使用例:
print("abc".upper()) # -> ABC

実行例:
dict1 =  {'a': 0, 'b': 1, 'c': 2, 'd': 3}
print(convert_up_neg(dict1)) #  {'A': 0, 'B': -1, 'C': -2, 'D': -3}
"""


def convert_up_neg(in_dict):
    result = dict()
    for k, v in in_dict.items():
        result[k.upper()] = -1 * v
    return result

