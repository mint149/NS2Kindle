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

