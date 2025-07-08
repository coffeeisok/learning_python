from bs4 import BeautifulSoup
import requests

# 指定哟啊获取标题的网站
response = requests.get(url = 'https://www.baidu.com/')
response.encoding = 'utf-8' # 解决中文乱码问题

soup = BeautifulSoup(response.text,'lxml')
# 查找具有 id="su"的<input>标签
unique_input = soup.find('input',id = 'su')

input_value = unique_input['value'] #获取 input 输入框的值

print(input_value)