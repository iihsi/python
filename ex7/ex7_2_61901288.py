"""
ファイル名の00000000を学籍番号に置き換えて提出すること

演習2:
英文の文字列scriptに含まれる単語数、及び単語"ship", "she"の数をカウントし、出力するプログラムを作成したい
以下のプログラムの修正箇所1~3を埋める形で完成させよ
"""

# 長文script
script = "A shipowner was about to send to sea an emigrant-ship. He knew that she was old, and not overwell built at the first; that she had seen many seas and climes, and often had needed repairs. Doubts had been suggested to him that possibly she was not seaworthy. These doubts preyed upon his mind, and made him unhappy; he thought that perhaps he ought to have her thoroughly overhauled and refitted, even though this should put him at great expense. Before the ship sailed, however, he succeeded in overcoming these melancholy reflections. He said to himself that she had gone safely through so many voyages and weathered so many storms that it was idle to suppose she would not come safely home from this trip also. He would put his trust in Providence, which could hardly fail to protect all these unhappy families that were leaving their fatherland to seek for better times elsewhere. He would dismiss from his mind all ungenerous suspicions about the honesty of builders and contractors. In such ways he acquired a sincere and comfortable conviction that his vessel was thoroughly safe and seaworthy; he watched her departure with a light heart, and benevolent wishes for the success of the exiles in their strange new home that was to be; and he got his insurance-money when she went down in mid-ocean and told no tales. What shall we say of him? Surely this, that he was verily guilty of the death of those men. It is admitted that he did sincerely believe in the soundness of his ship; but the sincerity of his conviction can in no wise help him, because he had no right to believe on such evidence as was before him. He had acquired his belief not by honestly earning it in patient investigation, but by stifling his doubts. And although in the end he may have felt so sure about it that he could not think otherwise, yet inasmuch as he had knowingly and willingly worked himself into that frame of mind, he must be held responsible for it."

# 空白記号 " " を除いた区切り文字群
delimiters = ".?!,;"

# 空白記号 " "
space = " "

# 総単語数
num_words = 0

# 文字列"she", "ship", 及びそれらをカウントするための変数
str_she = "she"
str_ship = "ship"
num_shes = 0
num_ships = 0

"""
修正箇所1:
ここで、文字列scriptについて、空白記号 " " を除く区切り文字群delimitersに含まれる文字を
空白記号 " " に変換せよ

(備考): 文字列を置換する関数 replace
・"文字列1".replace(文字列2, 文字列3)
 ・文字列1内の文字列2を文字列3に変換し、変換後の文字列を返す
(使用例):
text = "I like apple."
print(text.replace("apple", "orange")) # -> I like orange.
text2 = "ABCDCBA"
print(text2.replace("A", "X")) # -> XBCDCBX
"""
for d in delimiters:
    script = script.replace(d, space)

"""
修正箇所2:
ここで文字列scriptを空白記号で区切り、リスト変数 words に単語を格納せよ
(文字列を空白記号で分割し、リストwordsに保存)
"""
words = script.split()

"""
修正箇所3:
ここでリスト words 内に存在する総単語数, "ship"の数、"she"の数をカウントせよ
(num_words, num_ships, num_shesに, words内の総単語数, "ship"の数, "she"の数を
それぞれ代入すれば良い)


(備考): リスト内の要素の数を数える関数 count
・リスト.count(要素)
 ・リスト内に含まれる要素の数を返す
(使用例):
chars = ["A", "B", "C", "D", "C", "B", "A"]
print(chars.count("A")) # -> 2
print(chars.count("D")) # -> 1
print(chars.count("X")) # -> 0
"""
num_words = len(words)
num_ships = words.count(str_ship)
num_shes = words.count(str_she)
# カウントした総単語数, "ship"の数、"she"の数を表示
print("単語数:", num_words, "shipの数:", num_ships, "sheの数:", num_shes)