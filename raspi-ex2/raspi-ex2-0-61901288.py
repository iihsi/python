"""
カメラ撮影サンプルプログラム (提出する必要はありません)

以下は320x240の画像をカメラで撮影してresult.pngという名前で保存するプログラムである
以下のように実行してみて、動作を確認してみよう
$ python3 raspi-ex2-0-00000000.py

また、画素数を変えてみて遊んでみよう
"""

import time
import picamera
import numpy
from PIL import Image


def save_image(ndarray):


    """picameraによって画像を格納されたnumpyの配列を受け取り、PILライブラリを使ってファイルとして保存する

    Args:
        ndarray (numpy.ndarray): 画像を格納したnumpy.ndarray型の3次元配列。例えば横3px, 縦2pxで真っ赤の画像は以下のような形式とする
        [[[255, 0, 0], [255, 0, 0], [255, 0, 0]], [[255, 0, 0], [255, 0, 0], [255, 0, 0]]]

    Returns:
        None

    """
    im = Image.fromarray(ndarray)
    im.save('result.png')


if __name__ == '__main__':
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)  # 撮影する画像の縦横ピクセル
        camera.framerate = 24  # フレームレート
        time.sleep(2)  # カメラのセットアップが終わるのを待つ
        image = numpy.zeros((240, 320, 3), dtype=numpy.uint8)  # numpy.ndarrayという特殊な型(リストに近い)で3次元配列を定義
        camera.capture(image, 'rgb')  # RGB画像で撮影
        save_image(image)
