"""
演習4: ビットマップ画像を自分で作る

画像が格納されたnumpy配列からビットマップ画像を生成する関数generate_bmp()を、以下のgenerate_sample_bmp()を参考にして完成させよ

write_binary_file(): 引数で与えられたバイナリーデータをresult4.bmpとして保存する関数
generate_sample_bmp(): 2x2の赤と緑のチェッカー画像のバイナリーデータを返す関数
使用例:
b = generate_sample_bmp()
write_binary_file(b)

generate_bmp()完成までのヒント:
ヒント1:
- ほぼgenerate_sample_bmp()と同じ
- 違いは画像の縦横ピクセル数と画像データをnumpy配列から動的に生成する必要があるということ

ヒント2:
- 格納するデータはすべてリトルエンディアン型のバイト列にする必要がある
- int型の数字ならto_bytes()関数で変換できる
使用例:
a = 7
a.to_bytes(4, 'little') # aをリトルエンディアンの4バイトのバイト配列に変換
# => b'\x07\x00\x00\x00'

ヒント3:
- 画像データの生成は画像をx,yで二重ループさせ、R, G, Bそれぞれの値を1バイトずつ格納していくと簡単
- numpyの配列を仮にndarrayとすると、画像の横幅はlen(ndarray[0]), 縦幅はlen(ndarray)で取得できる(ものとして良い)
- ビットマップ形式ではRGBの順ではなくてBGRの逆順であり、さらに1ピクセルごとにBGRの末尾に0x00を追加しなければならない点には注意
- numpy配列のデータのバイト化は、tobytes()をつかうと良い
使用例:
image = numpy.zeros((240, 320, 3), dtype=numpy.uint8)
image[0][0][0].tobytes() # 一番左上の1ピクセルのRの値を1バイトのバイト列に変換

ちなみに
image[0][0].tobytes()
とすると一番左上の1ピクセルのRGBをまとめてバイト列に変換できるが、順番がRGBなのでなんとかしてBGRにする必要があるので注意
"""

import time
import picamera
import numpy


def write_binary_file(binary):
    """引数で与えられたバイナリーデータをresult4.bmpとして保存する

    Args:
        binary (bytearray): 画像のバイナリーデータ

    Returns:
        None

    """
    with open('result4.bmp', 'wb') as f:
        f.write(binary)


def generate_sample_bmp():
    """2x2の赤と緑のチェッカー画像のバイナリーデータを返す

    今回はいくつかあるビットマップ形式のうち、初期からあった簡単な形式を使う

    Returns:
        bytearray: 画像のバイナリーデータ

    """
    ba = bytearray()  # バイト単位でデータを保存できる型

    # BITMAPFILEHEADER (14Byte)
    ba.extend([0x42, 0x4d])  # ファイルタイプ
    ba.extend([0x00, 0x00, 0x00, 0x00])  # ファイルサイズ。(厳密なデコーダでないなら0でも良い)
    ba.extend([0x00, 0x00])  # 予約領域1
    ba.extend([0x00, 0x00])  # 予約領域2
    ba.extend([0x36, 0x00, 0x00, 0x00])  # ファイル先頭から画像データまでのバイト数

    # BITMAPINFOHEADER (40Byte)
    ba.extend([0x28, 0x00, 0x00, 0x00])  # BITMAPINFOHEADERのサイズ
    ba.extend([0x02, 0x00, 0x00, 0x00])  # 画像の横ピクセル数
    ba.extend([0x02, 0x00, 0x00, 0x00])  # 画像の縦ピクセル数
    ba.extend([0x01, 0x00])  # プレーン数。今は使われおらず、1で良い
    ba.extend([0x20, 0x00])  # 1ピクセルあたりのビット数
    ba.extend([0x00, 0x00, 0x00, 0x00])  # 圧縮方式。圧縮しない場合は0
    ba.extend([0x00, 0x00, 0x00, 0x00])  # 画像のサイズ。圧縮しない場合は0のままで良い
    ba.extend([0x00, 0x00, 0x00, 0x00])  # 横方向の解像度 (ピクセル/m)。設定しなくても良い
    ba.extend([0x00, 0x00, 0x00, 0x00])  # 縦方向の解像度 (ピクセル/m)。設定しなくても良い
    ba.extend([0x00, 0x00, 0x00, 0x00])  # カラーパレット色数。使用しない
    ba.extend([0x00, 0x00, 0x00, 0x00])  # 重要なカラーパレット数。使用しない

    # 画像データ
    # 1ピクセルあたりのビット数を32bitとしており、
    # Blue(8bit), Green(8bit), R(8bit), Reserved(8bit) の順で記述する。
    # - RGBではなくBGRの順なので注意
    # - Reservedは0で単に埋める
    # - 例: [0xff, 0x00, 0x00, 0x00] は青
    # 行の終わりなどを特別示す必要はなく、画像の縦横ピクセル数を元に勝手に解釈される
    # - 順番は画像の「下の行から上に」、「左から右」に向かわないといけないので注意
    ba.extend([0x00, 0xff, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00])
    ba.extend([0xff, 0x00, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00])

    return ba


def generate_bmp(ndarray):
    """画像が格納されたnumpyの配列から、ビットマップ形式のバイナリーデータを生成し返り値として返す

    Args:
        ndarray (numpy.ndarray):

    Returns:

    """
    ba = bytearray()  # バイト単位でデータを保存できる型
    
    

    # BITMAPFILEHEADER (14Byte)
    ba.extend([0x42, 0x4d])  # ファイルタイプ
    ba.extend([0x00, 0x00, 0x00, 0x00])  # ファイルサイズ。(厳密なデコーダでないなら0でも良い)
    ba.extend([0x00, 0x00])  # 予約領域1
    ba.extend([0x00, 0x00])  # 予約領域2
    ba.extend([0x36, 0x00, 0x00, 0x00])  # ファイル先頭から画像データまでのバイト数

    # BITMAPINFOHEADER (40Byte)
    ba.extend([0x28, 0x00, 0x00, 0x00])  # BITMAPINFOHEADERのサイズ
    ba.extend(len(ndarray[0]).to_bytes(4, "little"))# 画像の横ピクセル数
    ba.extend(len(ndarray).to_bytes(4, "little"))# 画像の縦ピクセル数
    ba.extend([0x01, 0x00])  # プレーン数。今は使われおらず、1で良い
    ba.extend([0x20, 0x00])  # 1ピクセルあたりのビット数
    ba.extend([0x00, 0x00, 0x00, 0x00])  # 圧縮方式。圧縮しない場合は0
    ba.extend([0x00, 0x00, 0x00, 0x00])  # 画像のサイズ。圧縮しない場合は0のままで良い
    ba.extend([0x00, 0x00, 0x00, 0x00])  # 横方向の解像度 (ピクセル/m)。設定しなくても良い
    ba.extend([0x00, 0x00, 0x00, 0x00])  # 縦方向の解像度 (ピクセル/m)。設定しなくても良い
    ba.extend([0x00, 0x00, 0x00, 0x00])  # カラーパレット色数。使用しない
    ba.extend([0x00, 0x00, 0x00, 0x00])  # 重要なカラーパレット数。使用しない

    # 画像データ
    # 1ピクセルあたりのビット数を32bitとしており、
    # Blue(8bit), Green(8bit), R(8bit), Reserved(8bit) の順で記述する。
    # - RGBではなくBGRの順なので注意
    # - Reservedは0で単に埋める
    # - 例: [0xff, 0x00, 0x00, 0x00] は青
    # 行の終わりなどを特別示す必要はなく、画像の縦横ピクセル数を元に勝手に解釈される
    # - 順番は画像の「下の行から上に」、「左から右」に向かわないといけないので注意
    for y in reversed(range(len(ndarray))):
        for x in range(len(ndarray[0])):
            ba.extend(ndarray[y][x][2].tobytes())
            ba.extend(ndarray[y][x][1].tobytes())
            ba.extend(ndarray[y][x][0].tobytes())
            ba.extend([0x00])            
    return ba


if __name__ == '__main__':
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)  # 撮影する画像の縦横ピクセル
        camera.framerate = 24  # フレームレート
        time.sleep(2)  # カメラのセットアップが終わるのを待つ
        image = numpy.zeros((240, 320, 3), dtype=numpy.uint8)  # numpy.ndarrayという特殊な型(リストに近い)で3次元配列を定義
        camera.capture(image, 'rgb')  # RGB画像で撮影
        image = generate_bmp(image)
        write_binary_file(image)
