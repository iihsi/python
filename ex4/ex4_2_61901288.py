"""
ファイル名の00000000を学籍番号に置き換えて提出すること

"""

"""
演習2-1:
コンソールから受け取った文字列をforループで1文字ずつ確認し、
'.'が何文字あるか数えられるよう、?を適切に埋めよ
"""

string = input()
searching_string = '.'

counter = 0
for s in string:
    if searching_string == s:
        counter += 1

print(counter)

"""
演習2-2: 変数stringの'.'が'?'に置き換わった文字列をprintせよ
例えば"foo.bar"という文字列を入力した場合は"foo?bar"とprintされれば良い

ヒント: 演習2-1と同じようなfor文が使える
"""

ans = ''
for s in string:
    if searching_string == s:
        ans += '?'
    else:
        ans += s 
print(ans)
        