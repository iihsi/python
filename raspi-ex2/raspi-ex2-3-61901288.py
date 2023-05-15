"""
演習3: グレースケール変換する

画像をグレースケールに変換する関数convert_grayscale()を完成させよ
完成した場合、以下のように実行すればグレースケールに変換されたresult3.pngが保存されるはずである
$ python3 raspi-ex2-3-00000000.py
"""

import time
import picamera
import numpy
from PIL import Image


def convert_grayscale(ndarray):
    """画像をグレースケールに変換する関数

    引数に画像が格納されたnumpy配列をとり、これをグレースケール変換したnumpy配列を返す
    グレースケール変換もいつくか手法があるが、今回はR,G,Bの平均をとる方法で行うものとする
    例: [[[1, 2, 3], [3, 5, 4]], [[5, 6, 7], [7, 9, 8]]]というnumpy配列が引数に与えられた場合、返り値は[[[2, 2, 2], [4, 4, 4]], [[6, 6, 6], [8, 8, 8]]]となる
    また平均をとる際は小数点は切り捨てて良い (int()でint型に変換してしまって良い) とする

    Args:
        ndarray (numpy.ndarray): 画像が格納されたnumpy配列

    Returns:
        numpy.ndarray: グレースケール変換された画像が格納されたnumpy配列

    """
    gs = numpy.zeros((len(ndarray), len(ndarray[0]), 3), dtype=numpy.uint8)
    for y in range(len(ndarray)):
        for x in range(len(ndarray[0])):
            ave = int((ndarray[y][x][0] + ndarray[y][x][1] + ndarray[y][x][2]) / 3)
            gs[y][x][0] = ave
            gs[y][x][1] = ave
            gs[y][x][2] = ave
    return gs


if __name__ == '__main__':
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)  # 撮影する画像の縦横ピクセル
        camera.framerate = 24  # フレームレート
        time.sleep(2)  # カメラのセットアップが終わるのを待つ
        image = numpy.zeros((240, 320, 3), dtype=numpy.uint8)  # numpy.ndarrayという特殊な型(リストに近い)で3次元配列を定義
        camera.capture(image, 'rgb')  # RGB画像で撮影
        image = convert_grayscale(image)
        im = Image.fromarray(image)
        im.save('result3.png')
