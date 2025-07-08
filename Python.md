# Python
## 语法
* 转义字符：`\`
    - `\n`换行
    - `\000`空
    - `\r`百分比进度
* 变量用`=`赋值（可以一次性赋多值）
* 变量不需要定义类型，直接赋值即可
    - `a = b = c = 1`
    - `a, b, c = 1, 2, "areyouok"`
* 变量是对象的引用

    ```
    a = [1, 2, 3]
    b = a         # b 和 a 指向同一个列表对象
    b.append(4)
    print(a)      # 输出：[1, 2, 3, 4]（因为 a 和 b 指向同一个对象）
    ```
* `import`导入相应模块
* `from A import B`从模块A中导入函数B
### 切片`[:]`（前闭后开）
* 从序列（列表、字符串、元组）中提取子序列；支持反向索引、步长操作
`sequence[start:stop:step]`
* 

### 语句
* del
用于删除对象的引用或名称绑定
   - `del x`删除变量`x`
   - `del lst[2]`删除列表中索引为2的元素
   - `del person["age"]`删除字典`person`中键`"age"`及其对应的值


-------

## 函数
1. `print()`
    - 默认输出换行
    - 不需要换行：末尾加上`end=""`
2. `type()`
    - 查看变量的类型
    - 以字符串形式输出，输出的类型用单引号`''`引着
    - 示例`print(type(x))` -> `<class 'int'>`
    * `type()`：认为子类**不是**一种父类类型
3. `isinstance()`
    - 用于检查一个对象是否为某个特定类或类型的实例
    - 示例：检查`a`是否为`int`的实例。
    ```
    a = 111
    isinstance(a, int)
    
    ->True #a是int型
    ```
    * `isinstance()`：认为子类**是**一种父类类型

1. append()

## 关键字
1. `del`
    * 用于删除对象的引用或名称绑定
2. `raise`
    * 手动触发异常
3. `yield`
    - 用于创建生成器，定义生成器函数
## 数据类型
* 通用规则：
    - 索引：`0`从头起始，`-1`从末尾开始
    - 
### 1.数字
* int（长整型）、float、bool、complex（复数）
    - `bool`是`int`的子类
    - `true`,`false`可以和数字相加
    ```
    True + 1    ->2
    False + 1   ->1
    ```
* 数学运算符
    - 乘方：`a ** b`
    - 除法：`/`浮点数`//`整数
    - 其余跟java一致
    - 混合计算时，整型会转成浮点型

### 2.String（字符串）`""`
* 用`''`或`""`括起来
* `+`连接运算符，`*`重复操作（要乘的次数）
* 索引：`0`从头起始，`-1`从末尾开始（前闭后开）
* 截取字符串（前闭后开）
    - `str[头下标:尾下标]`
#### 字符串运算符
   - `+`拼接字符串
   - `*`重复输出
   - `in`字符串中包含给定的字符，返回True
   - `%`以String型格式化输出（C语言中printf）
* 用法：
```
str = 'Runoob'  # 定义一个字符串变量

print(str)           # 打印整个字符串
print(str[0:-1])     # 打印字符串第一个到倒数第二个字符（不包含倒数第一个字符）
print(str[0])        # 打印字符串的第一个字符
print(str[2:5])      # 打印字符串第三到第五个字符（不包含索引为 5 的字符）
print(str[2:])       # 打印字符串从第三个字符开始到末尾
print(str * 2)       # 打印字符串两次
print(str + "TEST")  # 打印字符串和"TEST"拼接在一起
```
->
```
Runoob
Runoo
R
noo
noob
RunoobRunoob
RunoobTEST
```

* 有序对象的集合
* 写在`[]`之间，元素用`,`隔开
* 列表中元素类型可以不同；列表之间可以嵌套
* `+`连接运算符，`*`重复操作（要乘的次数）
* 元素通过偏移存取
* 索引：`0`从头起始，`-1`从末尾开始（前闭后开）

### 4.Dictionary（字典）`{}`
* 无序的对象（键`key`:值`value`）集合
* 元素通过键存取
* 字典是一种映射类型，用`{}`标识
* 键`key`是唯一的
* 详细用法示例：
    - 1. 简单创建字典
    ```
    dict = {}
    dict['one'] = "1 - 菜鸟教程"
    dict[2]     = "2 - 菜鸟工具"
    
    tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
    
    print (dict['one'])       # 输出键为 'one' 的值
    print (dict[2])           # 输出键为 2 的值
    print (tinydict)          # 输出完整的字典
    print (tinydict.keys())   # 输出所有键
    print (tinydict.values()) # 输出所有值
    ```
    - 2. 构造函数dict()
    ```
    >>> dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
    {'Runoob': 1, 'Google': 2, 'Taobao': 3}
    
    >>> dict(Runoob=1, Google=2, Taobao=3)
    {'Runoob': 1, 'Google': 2, 'Taobao': 3}
    ```

### 5.元组`()`
* 写在`()`中，元素之间用`,`隔开
* 元素类型可以不同

#### 元组运算符
元组之间可以用`+`、`+=`和`*`号进行运算


### 6.Set（集合）
* 无序、可变，用于存储唯一的元素
* 用`{}`表示，元素间用`,`隔开
* 集合中元素不重复，可以进行交、并、差集等操作
* 可以使用`set()`函数创建集合
* 创建空集合必须用`set()`
* 


## 面向对象
### 类
#### 类定义
* 语法格式：
    ```
    class ClassName:
        <statement_1>
        .
        .
        .
        <statrmrnt_n>
    ```
* 类实例化后可以使用其属性；创建一个类后，可以通过类名访问其属性
#### 类对象




## 迭代器
* 访问集合元素的一种方式
* 可以记住遍历位置的对象
* 迭代器对象从集合的第一个元素开始访问，直到所有元素被访问完结束
* 迭代器只能向前不能后退
* 两个基本方法：`__iter__()`、`__next__()`
### 创建一个迭代器  
1. `__iter__()`
    - 在对象初始化时执行
    - 返回一个特殊的迭代器对象
2. `__next__()`
    - 返回下一个迭代器对象

### StopIteration异常
* 用于标识迭代的完成，防止出现无限循环的情况

## 生成器
* 使用了`yield`的函数被称为生成器
* 生成器函数：可以在迭代的过程中逐步产生值，而不是一次性返回所有结果
* 生成器函数中使用`yield`语句时，函数的执行将会暂停，并将`yield`后面的表达式作为当前迭代的值返回
* 调用一个生成器函数，返回一个迭代器对象
## 异常


## 爬虫
基本流程：
- **发送HTTP请求**：通过HTTP请求从目标网站获取HTML页面，常用`requests`库
- **解析HTML内容**：常用库BeautifulSoup、lxml、Scrapy等
- **提取数据**：定位HTML元素（标签、属性、类名）来提取所需数据
- **存储数据**：将提取数据存储到数据库、CSV文件、JSON文件等
### 解析器
把HTML字符串翻译成树状结构，才能查找标签、提取内容
* 常用解析器：`lxml`
    - 容错好，速度快
* `html.parser`：python内置，容错差
### BeautifulSoup
* 适用于解析HTML和XML文件，并提供了一些方法来导航、搜索和修改解析树
* 能通过提供简单API来提取和操作网页中的内容
1. 基本用法
    * 查找标签、获取标签属性、提取文本
    * 使用bts需要先导入bts，并将HTML页面加载到BeautifulSoup对象中
    * 通常，先用爬虫库获取网页内容
2. [获取网页标题](code/Spider/get_web_title.py)
3. [查找标签](code/Spider/find_tags.py)
    * `find()`
        - 返回第一个匹配的标签
    * `find_all()`
        - 返回所有匹配的标签
4. [获取标签的文本](code/Spider/get_tag_text.py)
    `get_text()`提取标签中的文本内容
5. [查找子标签和父标签](code/Spider/find_tags_parent_son.py)
    - 通过parent和children属性访问标签的父标签&子标签
    ```
    #获取当前标签的父标签
    parent_tag = first_link.parent
    #获取当前标签的所有子标签
    children = first_link.children
    ```
6. [查找具有特定属性的标签](code/Spider/find_specific_attributes_tags.py)
    - 通过传递属性来查找具有特定属性的标签
        ```
        # 查找所有 class="example-class"的<div>标签
        divs_with_class = soup.find_all('div',class_='example-class') 
        # 查找具有 id="unique-id" 的<p> 标签
        unique_paragraph = soup.find('p',id='unique-id')
        ```
7. CSS选择器
`select()`方法允许使用类似jQuery的选择器语法来查找标签
    ```
    # 使用CSS选择器查找所有class为 'example' 的<div>标签
    example_divs = soup.select('div.example')
    
    # 查找所有 <a> 标签中的 href 属性
    links = soup.select('a[href]')
    ```

### Scrapy库
* 专门用于抓去网页数据并提取信息。常被用于数据挖掘、信息处理、存储历史数据等应用
* 全功能的爬虫框架，高度的可扩展性、灵活性，使用复杂和大规模的网页抓取任务
* [Scrapy架构图](assets/Scrapy架构图.png)
* Scrapy 的工作基于以下几个核心组件：
    - **Spider**：爬虫类，用于定义如何从网页中提取数据以及如何跟踪网页的链接。
    - **Item**：用来定义和存储抓取的数据。相当于数据模型。
    - **Pipeline**：用于处理抓取到的数据，常用于清洗、存储数据等操作。
    - **Middleware**：用来处理请求和响应，可以用于设置代理、处理 cookies、用户代理等。
    - **Settings**：用来配置 Scrapy 项目的各项设置，如请求延迟、并发请求数等。
* Scrapy项目结构：
