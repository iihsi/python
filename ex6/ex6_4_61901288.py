"""
ファイル名の00000000を学籍番号に置き換えて提出すること

発展: スコープ
以下は発展問題で、点数は+aの採点とします

以下のcreate_closure_example()は、呼出すたびに返り値が1増える関数、を戻り地として返す関数である

これを参考にして、呼び出すたびに与えられた引数の値を合計して戻り地として返し、
合計値が10以上のときは常に10を返すような関数を戻り値として返す関数、create_closure()を作成せよ

余裕がある人は、なぜ変数xは消えずに値を保持し続けるのか、調べてみよう。「クロージャ」などを検索してみると良い
"""

"""
def create_closure_example():
    x = 0

    def count():
        nonlocal x
        x += 1
        return x

    return count


f = create_closure_example()
print(f())  # 1
print(f())  # 2
print(f())  # 3
"""


def create_closure():
    """呼び出されるたびに与えられた引数の値を合算して戻り地として返す関数、を返す関数

    Returns:
        callable: 呼び出されるたびに与えられた引数の値を合算して戻り地として返す関数

    """
    def count(n):
        nonlocal x
        x += n
        if x >= 10:
            return 10
        else:
            return x
    
    return count