"""
ファイル名の00000000を学籍番号に置き換えて提出すること

演習:
与えられた文字列の最初の2文字と最後の2文字からなる文字列を出力するプログラムを作成せよ
以下の仕様を満たすこと
- 文字列はinput() の記述を用いて変数に代入
- 文字列の最初の2文字と最後の2文字からなる文字列を出力
- ただし、文字列の長さが2より小さい場合は、"Invalid string"と出力
 
(実行例1):
Input: aiueo
Output: aieo

(実行例2):
Input: 入力
Output: 入力入力

(実行例3):
Input: あ
Invalid string
"""

string = input("Input: ")
if len(string) >= 2 :
    print("Output", string[:2] + string[-2:] )
else :
    print("Invalid string")
        
    