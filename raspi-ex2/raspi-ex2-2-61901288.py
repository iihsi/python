"""
演習2: 最も明るいピクセルを見つけ出す

最も明るいピクセルを探すsearch_brightest()を完成させよ
完成した場合、以下のように実行すればそのピクセルが赤く塗られたresult2.pngが保存されるはずである
$ python3 raspi-ex2-2-00000000.py

ヒント: 演習1を参考にしてみよう
"""

import time
import picamera
import numpy
from PIL import Image


def search_brightest(ndarray):
    """最も明るいピクセルを探しだし、その座標を赤く塗った画像を返す

    画像の左から右、上から下に向かって探索するものとし、
    明るさが同じピクセルがあれば、一番最初に見つかった座標を赤く塗るとする
    また「最も明るい」とはRGBの合計値が最も大きいものを指すものとする

    Args:
        ndarray (numpy.ndarray): 画像の格納されたnumpy配列

    Returns:
        numpy.ndarray: 最も明るいピクセルを1つだけ赤く塗った画像の格納されたnumpy配列

    """

    max_rgb = 0
    max_x = 0
    max_y = 0
    for y in range(len(ndarray)):
        for x in range(len(ndarray[0])):
            myrgb = int(ndarray[y][x][0]) + int(ndarray[y][x][1]) + int(ndarray[y][x][2])
            if max_rgb < myrgb:
                max_rgb = myrgb
                max_x = x
                max_y = y
    ndarray[max_y][max_x][0] = 255
    ndarray[max_y][max_x][1] = 0
    ndarray[max_y][max_x][2] = 0
    return ndarray


if __name__ == '__main__':
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)  # 撮影する画像の縦横ピクセル
        camera.framerate = 24  # フレームレート
        time.sleep(2)  # カメラのセットアップが終わるのを待つ
        image = numpy.zeros((240, 320, 3), dtype=numpy.uint8)  # numpy.ndarrayという特殊な型(リストに近い)で3次元配列を定義
        camera.capture(image, 'rgb')  # RGB画像で撮影
        image = search_brightest(image)
        im = Image.fromarray(image)
        im.save('result2.png')
