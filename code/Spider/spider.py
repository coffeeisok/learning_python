from bs4 import BeautifulSoup
import requests

# 使用requests获取网页内容
url = 'https://cn.bing.com/'
response = requests.get(url)
# 中文乱码问题
response.encoding = 'utf-8'
# 使用BeautifulSoup解析网页
soup = BeautifulSoup(response.text,'lxml') # 使用lxml解析器

body_tag = soup.find('body')
print(body_tag.get_text())