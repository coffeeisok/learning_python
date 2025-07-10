print("字符串输出")
print(r'''hello,\n
      world''')
print(r'''hello,\nworld''')
print('''line1,line2,line3''')
print('''line1
      line2
      line3''')
print('''line1,
      line2,
      line3''')

print('''line1
line2
line3''')
print("----------------我--是--分--割--线-------------------")

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Bob!'''

print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)

print("-----------------我--是--分--割--线-------------------")
print("编码格式")
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))

print("-----------------我--是--分--割--线-------------------")

str = 'Runoob'  # 定义一个字符串变量  
print(str)           # 打印整个字符串
print(str[0:-1])     # 打印字符串第一个到倒数第二个字符（不包含倒数第一个字符）
print(str[0])        # 打印字符串的第一个字符
print(str[2:5])      # 打印字符串第三到第五个字符（不包含索引为 5 的字符）
print(str[2:])       # 打印字符串从第三个字符开始到末尾
print(str * 2)       # 打印字符串两次
print(str + "TEST")  # 打印字符串和"TEST"拼接在一起

print("-----------------我--是--分--割--线-------------------")
print("类型转换")
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# print('中文'.encode('ascii'))      # 会报错

print("-----------------我--是--分--割--线-------------------")
print("字符串格式化：")
print('hello,%s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

r = 2.5
s = 3.14 * r **2
print(f'圆的半径是{r}，面积是{s}')

print("----------------我--是--分--割--线-------------------")
s1 = 72
s2 = 85
r = (s2 - s1)/72
print(r)
print(f"小明的成绩提升了{r:.1}%")