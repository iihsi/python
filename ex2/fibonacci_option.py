"""
演習2 オプション
以下はフィボナッチ数列をturtleで描画するプログラムである
演習2と同じように?に適当な変数名を入れて完成させよう
(あくまで結果の確認用であり、採点には含みません)
"""

import turtle
t = turtle.Turtle()
 
a = 0
b = 1

for i in range(8):
    n = a + b
    a = b
    b = n
    for f in range(6):
        t.forward(5 * n)
        if f < 5:
            t.right(90)
turtle.bye()
