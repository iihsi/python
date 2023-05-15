# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:05:51 2019

@author: ryuta
"""
#############################################################
# ex1_1_turtle1_00000000.py
#
# 例題1: "length = 100", "degree = 120", "num_iter = 3"の各行の値を変更し、
# 長さ200の正方形を描画するプログラムを作成
# (ヒント: 長さ200の正方形の外角は90[度], 頂点の数は4)
#############################################################

# キャンバス上で「亀」を動かすためのライブラリturtleをインポート
import turtle

# 亀「alice」の定義
alice = turtle.Turtle()

# 距離length, 角度degree, 繰り返し回数num_iterの定義
length = 200
degree = 90
num_iter = 4

# 「aliceの座標表示」、「aliceが線を描きながら移動」をnum_iter回繰り返す
for i in range(num_iter):
    # aliceの座標表示
    p = alice.pos() # aliceの現在地の座標を取得
    alice.write(str(p)) # 座標をキャンバス上に表示
    
    # aliceが線を描きながら移動
    alice.forward(length) # 距離length分、aliceが前進
    alice.left(degree) # degree[度]左に旋回
    
# 以下は終了のためのコマンド
turtle.done()
turtle.bye()

# 毎回キャンバスのウィンドウを閉じること…
