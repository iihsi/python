"""
ファイル名の00000000を学籍番号に置き換えて提出すること

演習:論理演算
"""

"""
問1: NAND回路と同じような演算を行うために、以下の?を適切な論理演算子に書き換えよ
input1, input2が入力であり、outputが出力になるものとする
(ヒント: NAND回路では論理積の否定を行う)
"""
input1 = True
input2 = True
output = not (input1 and input2)
print(output)


"""
問2: NOR回路と同じような演算を行うために、以下の?を適切な論理演算子に書き換えよ
input1, input2が入力であり、outputが出力になるものとする
(ヒント: NOR回路では論理和の否定を行う)
"""
input1 = False
input2 = False
output = not (input1 or input2)
print(output)
