"""
ファイル名の00000000を学籍番号に置き換えて提出すること

本プログラムはPEP8に従い、インデント1回=スペース4つとする
https://www.python.org/dev/peps/pep-0008/#indentation
"""

"""
演習1-1: コンソールから受け取った文字列をint型に変換し、
age, money_in_pocketに代入するように?を適切を埋めよ
"""
age = int(input())
money_in_pocket = int(input())


"""
演習1-2: # 年齢ageがlegal_drink_age以上かつ
所持金money_in_pocketがdrink_cost以上の場合に"飲み会に参加可能である。"と表示され、
年齢ageがlegal_drink_age未満なら "お酒は{legal_drink_age}歳から。"と表示され、
そうでなければ "お金が足りない。"と表示されるよう、?を適切に埋めよ
"""
legal_drink_age = 20
drink_cost = 3000

if age >= legal_drink_age and money_in_pocket >= drink_cost :
    print("飲み会に参加可能である。")
elif age < legal_drink_age :
    print("お酒は", legal_drink_age, "歳から。")
else :
    print("お金が足りない。")
