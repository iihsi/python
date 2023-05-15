"""
ファイル名の00000000を学籍番号に置き換えて提出すること

例題:
配列を左から順に2つずつ比較し、小さい方が左になるように交換できるよう、
?を適切に埋めよ

(array[0]とarray[1]の比較&交換、array[1]とarray[2]の比較&交換...をする)
"""

array = [19, 5, 14, 18, 8, 3, 11, 1, 7]

for i in range(len(array) - 1):
    if (array[i] > array[i+1]):
        tmp = array[i]
        array[i] = array[i+1]
        array[i+1] = tmp

print(array)
