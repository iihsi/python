"""
ファイル名の00000000を学籍番号に置き換えて提出すること
"""

"""
演習2
フィボナッチ数列は、最初は0, 1から始まり、その後の項は前2項の和となっている数列である
以下はフィボナッチ数列の10番目までを表示しようとしているプログラムである
?に適当な変数名を入れてフィボナッチ数列を完成させよう
"""

a = 0
b = 1
print(a)
print(b)

# 以下の?に適当な変数名を入れてフィボナッチ数列を完成させよう
# for文は今は「同じことを繰り返すおまじない」と考えておいて良い
for i in range(8):
    n = a + b
    a = b
    b = n
    print(n)
