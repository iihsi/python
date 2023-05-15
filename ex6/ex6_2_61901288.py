"""
ファイル名の00000000を学籍番号に置き換えて提出すること

演習2: 以下のDocstringに従って関数を完成させよ
"""


def reverse_string(string):
    """文字列を逆にして返す関数

    引数に渡された文字列を逆にした文字列を戻り値として返す
    ただし、引数の型がstrでない場合はNoneを返すこと

    Args:
        string (str): 逆さまにしたい文字列

    Returns:
        str or None: 逆さまにされた文字列。引数の型がstr出ない場合はNone

    """
    if type(string) != str:
        return None
    
    result = ""
    for s in string:
        result = s + result
    return result