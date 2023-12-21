# HTMLを読み込む
with open('/var/www/html/index.html', 'r') as file:
    html = file.read()

# 文字列操作を使用して情報を書き換える
old_text = 'This is the default welcom page'
new_text = 'yokuwakarimasen'
new_html = html.replace(old_text, new_text)

# 書き換えたHTMLを保存する
with open('/var/www/html/index.html', 'w') as file:
    file.write(new_html)
