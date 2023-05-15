"""
演習1: 線を引く

画像の一番上の行と下の行に赤い線を引く関数draw_red_line()を完成させよ
完成後、以下のように実行して得られるresult1.pngの一番上に赤い線が引かれていることを確認せよ
$ python3 raspi-ex2-1-00000000.py

ヒント:
- numpyの配列を仮にndarrayとすると、画像の横幅はlen(ndarray[0]), 縦幅はlen(ndarray)で取得できる(ものとして良い)
- ある(x,y)の位置の画像について、ndarray[y][x][0]はRを、ndarray[y][x][1]はGを、ndarray[y][x][2]はBを示す
    - numpyの配列に限って言うとnumpy[y, x, 0]などと書いても良い
- 愚直にやるのであればx, yに関する二重forループを使うと良い
    - numpyの配列独特の記法に慣れていればその記法で記述したほうが簡潔で高速ではある
"""

import time
import picamera
import numpy
from PIL import Image


def draw_red_line(ndarray):
    """画像が格納されたnumpyの配列を加工し、赤い線を一番上と一番下の行に引いた状態で返り値として返す

    ここで一番上の行とはndarray[0], 一番下の行とはndarray[len(ndarray) - 1]の中にあるピクセルたちのことを指し、
    赤とはRGB=(255, 0, 0)の状態を指すものとする

    Args:
        ndarray (numpy.ndarray): 画像を格納したnumpy.ndarray型の3次元配列

    Returns:
        numpy.ndarray: 赤い線が一番上の行に引かれた状態の画像が格納されたnumpyの配列

    """
    for x in range(len(ndarray[0])):
        for y in range(len(ndarray)):
            if y == 0 or y == len(ndarray)-1:
                ndarray[y][x][0] = 255
                ndarray[y][x][1] = 0
                ndarray[y][x][2] = 0
    return numpy.ndarray
    


if __name__ == '__main__':
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)  # 撮影する画像の縦横ピクセル
        camera.framerate = 24  # フレームレート
        time.sleep(2)  # カメラのセットアップが終わるのを待つ
        image = numpy.zeros((240, 320, 3), dtype=numpy.uint8)  # numpy.ndarrayという特殊な型(リストに近い)で3次元配列を定義
        camera.capture(image, 'rgb')  # RGB画像で撮影
        draw_red_line(image)
        im = Image.fromarray(image)
        im.save('result1.png')
