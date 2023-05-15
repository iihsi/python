"""
発展1: コンソール入力によるLEDの明滅

演習1を参考にして、実行したらコンソール入力を待ち、0が入力されたらLEDを消灯させ、1が入力されたらLEDを点灯させ、それ以外の場合は何もしない処理を3回行ったら終了するプログラムを作成せよ
実行終了後のLEDの状態は気にしなくて良い
回路は演習1と同じものを使うとして、ピンの番号の選択には気をつけること
"""

import RPi.GPIO  # GPIOを扱うためのライブラリを読み込み
import time

RPi.GPIO.setmode(RPi.GPIO.BOARD)
RPi.GPIO.setup(10, RPi.GPIO.OUT)

for i in range(3):
    x = input()
    if x == "0":
        RPi.GPIO.output(10, RPi.GPIO.LOW)
    elif x == "1":
        RPi.GPIO.output(10, RPi.GPIO.HIGH)

RPi.GPIO.cleanup()
