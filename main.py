import lxml.html
import requests

# HTML取得
target_url = 'http://togetter.com/li/702450'
requestHtml = requests.get(target_url)
root = lxml.html.fromstring(requestHtml.text)

# 解析
tweets = root.cssselect('.tweet')

# 表示
for tweet in tweets:
	print(tweet.text_content())

# ファイル生成
header = open('header.html', 'r')
footer = open('footer.html', 'r')
output = open('_output.html', 'w')

for tag in header.readlines():
	print(tag)
	output.write(tag)

title = '<h2>**TITLE**</h2><hr><br>'
title = title.replace('**TITLE**', 'バック・イン・ブラック')
output.write(title)

for tweet in tweets:
	tweetStr = '<p>' + tweet.text_content() + '</p><br>'

	print(tweetStr)
	output.write(tweetStr)

for tag in footer.readlines():
	print(tag)
	output.write(tag)
