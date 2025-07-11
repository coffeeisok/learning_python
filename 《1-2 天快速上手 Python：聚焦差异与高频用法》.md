# 《1-2 天快速上手 Python：聚焦差异与高频用法》

结合你的 C、Java 基础（已掌握编程核心逻辑），1-2 天内快速上手 Python 完全可行。核心策略是：**聚焦 “Python 与 C/Java 的差异”+ 工作场景高频用法**，跳过冗余理论，直接通过实战巩固。以下是分时段学习计划和核心内容：


### **第一天：掌握 Python 核心语法（与 C/Java 的差异是重点）**

#### **1. 环境准备（30 分钟）**



*   安装 Python：官网下载 3.x 版本（推荐 3.8+），勾选 “Add Python to PATH”（避免手动配置环境变量）。


*   编辑器：用 VS Code（轻量，安装 Python 插件），或 PyCharm（新手友好，社区版免费）。


*   运行方式：



    *   交互式：终端输入`python`进入解释器（类似 Java 的 JShell，适合临时测试代码）。


    *   脚本式：写`.py`文件，终端用`python 文件名.py`运行（和 Java 的`java 类名`类似）。


#### **2. 核心语法（6-8 小时，对比 C/Java 快速迁移）**

##### **（1）变量与数据类型（1 小时）**



*   **最大差异**：Python 无需声明类型（动态类型），直接赋值。




```
\# 对比Java：int a = 1; String b = "hi";


a = 1  # 整数（类似int，但Python自动支持长整数）


b = "hi"  # 字符串（单双引号通用，多行用三引号）


c = 3.14  # 浮点数


d = True  # 布尔值（首字母大写，区别于Java的boolean）
```



*   **常用数据结构（重点，工作高频）**：



    *   **列表（list）**：类似 Java 的 ArrayList，支持动态扩容、增删改查。




```
arr = \[1, 2, "a"]  # 元素可混类型（区别于C的数组）


arr.append(3)  # 新增元素


arr\[0] = 0  # 修改元素（和C/Java的数组索引用法一致）
```



*   **字典（dict）**：类似 Java 的 HashMap（键值对），工作中处理 JSON / 配置文件必备。




```
person = {"name": "张三", "age": 20}  # 键用字符串/数字，值任意类型


print(person\["name"])  # 取value（类似map.get("name")）


person\["gender"] = "男"  # 新增键值对
```



*   其他：元组（tuple，不可修改的列表，用`()`）、集合（set，去重，类似 Java 的 Set）。


<!---->

*   **字符串操作（高频）**：




```
s = "hello"


print(s\[0])  # 取单个字符（和C的char\[]类似）


print(s + " world")  # 拼接（比Java的+更简洁）


print(s.upper())  # 内置方法（Python字符串有大量实用方法，查文档即用）
```

##### **（2）控制流（1.5 小时）**



*   **分支（if-elif-else）**：无大括号，用**缩进**（4 个空格）区分代码块（核心差异！）。




```
\# 对比Java：if (a > 0) { ... } else if (a < 0) { ... } else { ... }


a = 5


if a > 0:


&#x20;   print("正数")  # 缩进=代码块，必须一致（否则报错）


elif a < 0:


&#x20;   print("负数")


else:


&#x20;   print("零")
```



*   **循环（for/while）**：



    *   for 循环：更灵活，直接遍历 “可迭代对象”（列表、字符串、字典等，无需下标）。




```
\# 对比Java：for (int i=0; i\<list.size(); i++) { ... }


arr = \[1, 2, 3]


for num in arr:  # 直接取元素，无需下标


&#x20;   print(num)


\# 如需下标，用enumerate（类似Java的for循环+index）


for index, num in enumerate(arr):


&#x20;   print(f"下标{index}：{num}")  # f-string：格式化字符串（比Java的+拼接高效）
```



*   while 循环：语法和 C/Java 几乎一致（注意缩进）。


##### **（3）函数（1.5 小时）**



*   **定义**：用`def`，无需声明返回值类型（返回值可动态变化）。




```
\# 对比Java：public int add(int a, int b) { return a + b; }


def add(a, b):  # 参数无需类型


&#x20;   return a + b  # 自动返回结果类型（int/float等）


print(add(2, 3))  # 调用：直接函数名(参数)，无需new
```



*   **参数特性**（Python 特色，工作常用）：



    *   关键字参数：调用时指定参数名，顺序可乱（适合多参数场景）。




```
def info(name, age):


&#x20;   print(f"姓名：{name}，年龄：{age}")


info(age=20, name="张三")  # 关键字参数，顺序无关
```



*   默认参数：定义时给参数设默认值（类似 Java 的方法重载简化版）。




```
def info(name, age=18):  # age默认18


&#x20;   print(f"姓名：{name}，年龄：{age}")


info("张三")  # 只传name，age用默认值
```

##### **（4）面向对象（1 小时，简化版，够用即可）**



*   类与对象：语法比 Java 简洁，无需`public`等修饰符，继承用`()`。




```
\# 对比Java：class Person { String name; public Person(String n) { name = n; } }


class Person:


&#x20;   def \_\_init\_\_(self, name):  # 构造方法（类似Java的构造函数）


&#x20;       self.name = name  # 成员变量（必须用self.xxx）


&#x20;  &#x20;


&#x20;   def say\_hi(self):  # 成员方法，第一个参数必须是self（类似Java的this）


&#x20;       print(f"你好，我是{self.name}")


p = Person("张三")  # 创建对象（无需new）


p.say\_hi()  # 调用方法
```

##### **（5）模块与库（1 小时，工作必备）**



*   导入模块：类似 Java 的`import`，但更灵活。




```
import json  # 导入整个模块（类似Java import java.util.\*）


from json import loads  # 只导入需要的函数（类似Java static import）


\# 第三方库：用pip安装（类似Java的Maven）


\# 终端执行：pip install 库名（比如之前的geopandas）
```

##### **（6）文件操作（1 小时，处理 JSON / 文本必备）**



*   读写文件：用`with`语句（自动关闭文件，比 C 的`fclose`安全）。




```
\# 写文件


with open("test.txt", "w", encoding="utf-8") as f:  # "w"=覆盖写，"a"=追加


&#x20;   f.write("hello world")  # 写入内容


\# 读文件


with open("test.txt", "r", encoding="utf-8") as f:


&#x20;   content = f.read()  # 读取全部内容


&#x20;   print(content)
```

#### **3. 实战练习（2 小时）**

用上述语法写一个小脚本：




*   需求：读一个文本文件，统计每个单词出现的次数，结果写入新文件。


*   提示：用`split()`分割单词，用字典`{单词: 次数}`存结果。


### **第二天：聚焦工作场景（以你的 “JSON/GeoJSON 处理” 为例）**

#### **1. 处理 JSON 数据（2-3 小时，结合你的业务）**



*   用`json`库（Python 内置，无需安装）：




```
import json


\# 1. 解析JSON字符串（类似Java的JSONObject）


json\_str = '{"name": "张三", "age": 20}'


data = json.loads(json\_str)  # 转成Python字典


print(data\["name"])  # 取字段


\# 2. 解析JSON文件


with open("input.json", "r", encoding="utf-8") as f:


&#x20;   data = json.load(f)  # 直接从文件加载


\# 3. 生成JSON（写入文件）


new\_data = {"name": "李四", "age": 22}


with open("output.json", "w", encoding="utf-8") as f:


&#x20;   json.dump(new\_data, f, ensure\_ascii=False, indent=2)  # indent=2：格式化显示
```

#### **2. 地理数据处理（结合你的 geopandas 需求，2-3 小时）**



*   安装库：终端执行`pip install geopandas`（可能需要额外安装依赖，按提示操作）。


*   核心操作（复用之前的业务场景）：




```
import geopandas as gpd


import json


\# 读GeoJSON


gdf = gpd.read\_file("input.geojson")  # 加载为GeoDataFrame（类似表格）


\# 提取指定字段（比如“地名”“区划码”）


select\_fields = \["地名", "区划码"]


new\_features = \[]


for \_, row in gdf.iterrows():  # 遍历每一行


&#x20;   properties = {field: row\[field] for field in select\_fields}  # 提取属性


&#x20;   geometry = json.loads(row\["geometry"].to\_json())  # 提取几何信息


&#x20;   new\_features.append({"type": "Feature", "properties": properties, "geometry": geometry})


\# 写入新的GeoJSON


with open("output.geojson", "w", encoding="utf-8") as f:


&#x20;   json.dump({"type": "FeatureCollection", "features": new\_features}, f, ensure\_ascii=False, indent=2)
```

#### **3. 工作中高频问题（1-2 小时）**



*   查文档：用`print(函数名.__doc__)`看说明，或直接搜 “Python 函数名 用法”（比如 “Python json.dump 参数”）。


*   调试：用`print`打印变量，或 VS Code/PyCharm 的断点调试（和 Java 类似）。


*   第三方库安装失败：换国内源（比如`pip install -i ``https://pypi.tuna.tsinghua.edu.cn/simple`` 库名`）。


### **快速上手技巧：用 “类比法” 迁移知识**



| 场景&#xA;      | C/Java&#xA;                        | Python&#xA;                      |
| ------------ | ---------------------------------- | -------------------------------- |
| 注释&#xA;      | `// 单行` `/* 多行 */`                 | `# 单行` `""" 多行 """`              |
| 数组 / 列表&#xA; | `int[] a = {1,2};`                 | `a = [1,2]`                      |
| 键值对&#xA;     | `HashMap<String, Integer> m = ...` | `m = {"k": 1}`                   |
| 循环遍历数组&#xA;  | `for (int i=0; i<a.length; i++)`   | `for num in a:`                  |
| 字符串拼接&#xA;   | `a + b`（效率低）&#xA;                  | `f"{a}{b}"`（f-string 高效）&#xA;    |
| 异常处理&#xA;    | `try-catch-finally`                | `try-except-finally`（关键词不同）&#xA; |

### **最后：用你的工作任务驱动学习**

直接拿实际工作中的需求练手（比如修改之前的`extract_from_geojson`函数，添加新字段提取逻辑）。遇到不懂的语法，针对性搜 “Python 如何实现 XX 功能”（比如 “Python 字典遍历”），1-2 天内足够上手基础工作。


Python 的核心优势是 “简洁 + 库丰富”，不用追求完美，先能用起来，后续再慢慢优化细节～


> （注：文档部分内容可能由 AI 生成）
>