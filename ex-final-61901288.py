# Q1-1:
# 引数として与えられた整数xが偶数であれば真, 奇数であれば偽を返す関数is_even()を完成させよ
# 引数xは0以上の整数であると仮定してよく、返り値の型はbool型とする
def is_even(x: int):
    if x%2 == 1:
        return False
    else:
        return True
        

if __name__ == "__main__":
    # デバッグ用のテストケースを自分で追加してよい。これ以降の問題でも同様
    print("Q1-1")
    print("is_even(4) => ", is_even(4)) # True
    print("is_even(7) => ", is_even(7)) # False
    print()

# Q1-2:
# 引数として与えられた整数のリストnum_listの中がすべて偶数であれば真を、そうでなければ偽を返す関数check_even_in_list()を完成させよ
# リストの整数はすべて0以上と仮定して良く、Q1-1で作ったis_even()を使用しても良い
# また返り値の型はbool型とする
def check_even_in_list(num_list: list):
    x = 0
    for i in num_list:
        if i%2 == 0:
            x += 0
        else:
            x += 1
    if x == 0:
        return True
    else:
        return False
    

if __name__ == "__main__":
    print("Q1-2")
    print("check_even_in_list([2, 4, 6]) => ", check_even_in_list([2, 4, 6])) # True
    print("check_even_in_list([2, 3, 4]) => ", check_even_in_list([2, 3, 4])) # False
    print()

# Q2:
# 引数に与えられた文字列に対して、"l"が見つかったら3文字繰り返すようにした文字列を返す関数repeat_str()を完成させよ
# 返り値の型はstr型とする
# 実行例: repeat_str("apple", "l") # 結果は appllle
def repeat_str(string: str):
    x = list(string)
    for i in range(len(x)):
        if x[i] == "l":
            x[i] = "lll"
    return "".join(x)

if __name__ == "__main__":
    print("Q2")
    print('repeat_str("apple") => ', repeat_str("apple")) # appllle
    print('repeat_str("orange") => ', repeat_str("orange")) # orange
    print()


# Q3:
# フィボナッチ数列 a(n) は、 a(0) = 0, a(1) = 1 から始まり、 n = 2 以上は a(n) = a(n - 1) + a (n - 2) で表される数列である
# 引数に与えられた整数nに対して、フィボナッチ数列のa(n)の値を返り値として返す関数fibonacci()を完成させよ
# nは0以上の整数と仮定して良く、返り値の型はint型とする
#
# 実行例:
# fibonacci(0) # 0
# fibonacci(1) # 1
# fibonacci(2) # 1
# fibonacci(3) # 2
# fibonacci(4) # 3
# fibonacci(5) # 5
# fibonacci(6) # 8
def fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    print("Q3")
    print('fibonacci(0) => ', fibonacci(0)) # 0
    print('fibonacci(1) => ', fibonacci(1)) # 1
    print('fibonacci(2) => ', fibonacci(2)) # 1
    print('fibonacci(3) => ', fibonacci(3)) # 2
    print('fibonacci(6) => ', fibonacci(6)) # 8
    print()

# Q4-1:
# 以下のような学生ごとのテストの点数を示すdict型があるとする
# score_dict_example = {"taro": 80, "hanako": 85, "ichiro": 73, "jiro": 90}
# これを80点以上の学生とそうでない学生の2つのdict型に分ける関数split_dict()を完成させよ
# 第1引数は分割したい元のdictがくるものとし、第2引数のdictには分割後の80点以上の学生を格納、第3引数のdictにはそうでない学生を格納せよ
#
# 実行例:
# in_dict = {"taro": 80, "hanako": 85, "ichiro": 73, "jiro": 90}
# out_dict1 = {}
# out_dict2 = {}
# split_dict(in_dict, out_dict1, out_dict2)
# print(out_dict1) # {'taro': 80, 'hanako': 85, 'jiro': 90}
# print(out_dict2) # {'ichiro': 73}
def split_dict(input_dict: dict, output_dict1: dict, output_dict2: dict):
    for x in in_dict:
        if in_dict[x] >= 80:
            output_dict1[x] = in_dict[x]
        else:
            del(in_dict[x])
            output_dict2[x] = in_dict[x]
    return (output_dict1, output_dict2)
            

if __name__ == "__main__":
    print("Q4-1")
    in_dict = {"taro": 80, "hanako": 85, "ichiro": 73, "jiro": 90}
    out_dict1 = {}
    out_dict2 = {}
    split_dict(in_dict, out_dict1, out_dict2)
    print("out_dict1 => ", out_dict1) # {'taro': 80, 'hanako': 85, 'jiro': 90}
    print("out_dict2 => ", out_dict2) # {'ichiro': 73}
    print()


# Q4-2:
# 以下のように学生ごとのテストの点数を示す2つのdictがあるとする
# score_dict1 = {"taro": 80, "hanako": 85, "ichiro": 70}
# score_dict2 = {"ichiro": 73, "jiro": 90, "hanako": 65}
#
# 第1引数と第2引数にこれらのdict型が与えられたとして、第1引数のdictに第2引数のdictの内容をマージする関数merge_dict()を完成させよ
# ただし同じ学生 (=同じKey)がいた場合は、点数 (Value) の高い方で上書きするものとする
# 実行例:
# merge_dict(score_dict1, score_dict2) # {"taro": 80, "hanako": 85, "ichiro": 73, "jiro": 90}
def merge_dict(dict1: dict, dict2: dict):
    pass

if __name__ == "__main__":
    print("Q4-2")
    score_dict1 = {"taro": 80, "hanako": 85, "ichiro": 70}
    score_dict2 = {"ichiro": 73, "jiro": 90, "hanako": 65}
    merge_dict(score_dict1, score_dict2)
    print("score_dict1 => ", score_dict1) # {"taro": 80, "hanako": 85, "ichiro": 73, "jiro": 90}
    print()
