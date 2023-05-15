"""
演習1: LEDの点滅

以下で解説するライブラリRPi.GPIOを用いて、LEDを1秒間隔でHIGH->LOW->HIGH->LOWと変化させ、2度点滅させるプログラムを作成せよ
スライドに記載した回路図通りでプログラムが動くよう、ピンの番号の選択には気をつけること

採点は
$ python3 raspi-ex1-1-00000000.py
と実行したときにRPi.GPIO.setmode(), RPi.GPIO.setup(), RPi.GPIO.output(), RPi.GPIO.cleanup()が正しい引数で正しい回数呼ばれているかどうかを確認して行う
ピン番号についてはBOARD, BCMのどちらのモードでも構わないが、スライド通りの回路で動くピン番号にしておくこと

ライブラリの解説:
すでにRPi.GPIOとtimeはimportされているので、以下の関数はそのまま実行できる

RPi.GPIO.setmode()
- 第1引数にピンモードを指定し、GPIOのピンのモードを選択する。初期化処理として初めに呼び出すこと
- RPi.GPIO.setmode(RPi.GPIO.BOARD)とした場合は物理的なピン番号を、RPi.GPIO.setmode(RPi.GPIO.BCM)とした場合はGPIOの番号を今後指定する必要がある

RPi.GPIO.setup()
- 第1引数にピン番号を、第2引数に入力モードか出力モードかの指定を行う。RPi.GPIO.setmode()の後に呼ぶこと
- ピン番号の指定はRPi.GPIO.setmode()で決めた方式に従う
- 使用例: RPi.GPIO.setup(1, RPi.GPIO.OUT) # 1番ピンを出力モードに設定

RPi.GPIO.output()
- 第1引数にピン番号を、第2引数に出力の状態を指定し、ピンの状態を変更する。RPi.GPIO.setup()が終わってから呼ぶこと
- ピン番号の指定はRPi.GPIO.setmode()で決めた方式に従う
- 出力の状態はRPi.GPIO.HIGHかRPi.GPIO.LOWで指定する
- 使用例: RPi.GPIO.output(1, RPi.GPIO.HIGH) # 1番ピンの出力をHIGHに変更

RPi.GPIO.cleanup()
- 引数なしで呼び出し、ピン状態をきれいに掃除する
- プログラム終了時には必ず呼ぶこと

time.sleep()
- 第1引数に秒数を指定し、その間スリープする
- LEDの明滅感覚の調整に使用
"""

import RPi.GPIO  # GPIOを扱うためのライブラリを読み込み
import time  # timeはGPIO制御に必須ではないが、点滅間隔を調整する際に使用する

RPi.GPIO.setmode(RPi.GPIO.BOARD)
RPi.GPIO.setup(10, RPi.GPIO.OUT)
RPi.GPIO.output(10, RPi.GPIO.HIGH)
time.sleep(1)
RPi.GPIO.output(10, RPi.GPIO.LOW)
time.sleep(1)
RPi.GPIO.output(10,  RPi.GPIO.HIGH)
time.sleep(1)
RPi.GPIO.output(10, RPi.GPIO.LOW)
RPi.GPIO.cleanup()


