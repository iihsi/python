"""
演習2: タクトスイッチの入力

以下で解説するライブラリRPi.GPIOを用いて、実行時にタクトスイッチの入力を取得してprintするプログラムを作成せよ
(状態がLOWであればLOWを、HIGHであればHIGHを出力する)

実行例1: スイッチを押さずに実行
$ python3 raspi-ex1-2-00000000.py
LOW

実行例2: スイッチを押しながら実行
$ python3 raspi-ex1-2-00000000.py
HIGH

ライブラリの解説:

RPi.GPIO.setmode()
- 第1引数にピンモードを指定し、GPIOのピンのモードを選択する。初期化処理として初めに呼び出すこと
- RPi.GPIO.setmode(RPi.GPIO.BOARD)とした場合は物理的なピン番号を、RPi.GPIO.setmode(RPi.GPIO.BCM)とした場合はGPIOの番号を今後指定する必要がある

RPi.GPIO.setup()
- 第1引数にピン番号を、第2引数に入力モードか出力モードかの指定を行う。RPi.GPIO.setmode()の後に呼ぶこと
- ピン番号の指定はRPi.GPIO.setmode()で決めた方式に従う
- 使用例: RPi.GPIO.setup(1, RPi.GPIO.IN) # 1番ピンを入力モードに設定

RPi.GPIO.input()
- 第1引数にピン番号を指定し、ピン番号の状態を返す。RPi.GPIO.setup()が終わってから呼ぶこと
- ピン番号の指定はRPi.GPIO.setmode()で決めた方式に従う
- 返り値はRPi.GPIO.HIGHかRPi.GPIO.LOWのどちらかを取る
- 使用例: i = RPi.GPIO.input(1) # 1番ピンの入力を取得してiに代入

RPi.GPIO.cleanup()
- 引数なしで呼び出し、ピン状態をきれいに掃除する
- プログラム終了時には必ず呼び出すこと
"""

import RPi.GPIO  # GPIOを扱うためのライブラリを読み込み

RPi.GPIO.setmode(RPi.GPIO.BOARD)
RPi.GPIO.setup(12, RPi.GPIO.IN)
if RPi.GPIO.input(12)==RPi.GPIO.LOW:
    print("LOW")
else:
    print("HIGH")
RPi.GPIO.cleanup()
