"""
発展2: タクトスイッチの入力待ち

演習2を参考にして、ループしつづけてタクトスイッチを押される度にコンソールに”Down”とprintし、3回スイッチが押されたら終了するプログラムを完成させよ
回路は演習2と同じものを使うとして、ピンの番号の選択には気をつけること

必要な追加の関数:
RPi.GPIO.add_event_detect():
- 第1引数にピン番号、第2引数にエッジ識別子(立ち上がり: RPi.GPIO.RISING、立ち下がり: RPi.GPIO.FALLING、両方: RPi.GPIO.BOTH)、
- 第3引数にコールバック関数、第4引数に次のイベントを呼び出さない時間間隔をms単位で指定する
- 使用例: RPi.GPIO.add_event_detect(1, RPi.GPIO.RISING, callback=my_func, bouncetime=200)
    - 番号1のピンに、ピンの状態が立ち上がったときに予め定義したmy_func()を呼び出すようにし、200msの間は次のイベントを呼ばないようにする
    - my_func()は呼ばれる際、ピンの番号を第1引数に取らねばならない


ヒント: 押された回数のカウントはglobal変数を使ってしまって、それをwhile文などでチェックすれば良い
global変数の使用例:

x = 10
def func():
    global x
    x +=1
    print(x)
"""

import RPi.GPIO  # GPIOを扱うためのライブラリを読み込み

x = 0
def my_func(i):
    print("Down")
    global x
    x += 1

RPi.GPIO.setmode(RPi.GPIO.BOARD)
RPi.GPIO.setup(12, RPi.GPIO.IN)
RPi.GPIO.add_event_detect(12, RPi.GPIO.FALLING, callback=my_func, bouncetime=200)
while x < 3:
    continue
RPi.GPIO.cleanup()