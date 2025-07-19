import re

def demo_basic_patterns():
    print("\n=== 基本模式匹配 ===")

    # 1. 匹配多种可能 []
    print("\n1. 匹配多种可能 []")
    res = re.search(r'r[au]n','dog runs to cat')
    print("search(r'r[au]n','dog runs to cat'):", res)

    res = re.search(r'r[au]n','dog rans to cat')
    print("search(r'r[au]n','dog rans to cat'):", res)
    
    # 2. 匹配数字 \d and \D
    print("\n2. 匹配数字 \\d and \\D")
    res = re.search(r'r\dn','run r9n')
    print("search(r'r\\dn','run r9n'):", res)
    res = re.search(r'r\Dn','run r9n')
    print("search(r'r\\Dn','run r9n'):", res)
    
    # 3. 匹配空白 \s and \S
    print("\n3. 匹配空白 \\s and \\S")
    res = re.search(r'r\sn','r\nn r9n')
    print("search(r'r\\sn','r\\nn r9n'):", res)
    res = re.search(r'r\Sn','r\nn r9n')
    print("search(r'r\\Sn','r\\nn r9n'):", res)
    
    # 4. 匹配字母数字和下划线 \w and \W
    print("\n4. 匹配字母数字和下划线 \\w and \\W")
    res = re.search(r'r\wn','r\nn r9n')
    print("search(r'r\\wn','r\\nn r9n'):", res)
    res = re.search(r'r\Wn','r\nn r9n')
    print("search(r'r\\Wn','r\\nn r9n'):", res)
    
    # 5. 匹配单词边界 \b and \B
    print("\n5. 匹配单词边界 \\b and \\B")
    res = re.search(r'\bruns\b','dog runs to cat')
    print("search(r'\\bruns\\b','dog runs to cat'):", res)
    res = re.search(r'\bruns\b','dogrunsto cat')
    print("search(r'\\bruns\\b','dogrunsto cat'):", res)
    res = re.search(r'\Bruns\B','dog runs to cat')
    print("search(r'\\Bruns\\B','dog runs to cat'):", res)
    res = re.search(r'\Bruns\B','dogrunsto cat')
    print("search(r'\\Bruns\\B','dogrunsto cat'):", res)

def demo_special_chars():
    print("\n=== 特殊字符匹配 ===")
    # 6. 匹配特殊字符 \ and .
    print("\n6. 匹配特殊字符 \\ and .")
    res = re.search(r'runs\\','dog runs\ to cat')
    print("search(r'runs\\\\','dog runs\\ to cat'):", res)
    res = re.search(r'r.ns','dog r;ns to cat')
    print("search(r'r.ns','dog r;ns to cat'):", res)
    res = re.search(r'r.ns','dog r\nns to cat')
    print("search(r'r.ns','dog r\\nns to cat'):", res)
    
    # 7. 匹配行首行尾 ^ and $
    print("\n7. 匹配行首行尾 ^ and $")
    res = re.search(r'^runs','dog runs to cat')
    print("search(r'^runs','dog runs to cat'):", res)
    res = re.search(r'^dog','dog runs to cat')
    print("search(r'^dog','dog runs to cat'):", res)
    res = re.search(r'runs$','dog runs to cat')
    print("search(r'runs$','dog runs to cat'):", res)
    res = re.search(r'cat$','dog runs to cat')
    print("search(r'cat$','dog runs to cat'):", res)
    
    # 8. 多行匹配 re.M
    print("\n8. 多行匹配 re.M")
    string = """123. dog runs to cat.
You run to dog."""
    res = re.search(r'^You',string)
    print("search(r'^You',string):", res)
    res = re.search(r'^You',string,re.M)
    print("search(r'^You',string,re.M):", res)

def demo_quantifiers():
    print("\n=== 量词匹配 ===")
    # 9. 可选匹配 ?
    print("\n9. 可选匹配 ?")
    res = re.search(r'r(u)?ns','dog runs to cat')
    print("search(r'r(u)?ns','dog runs to cat'):", res)
    res = re.search(r'r(u)?ns','dog rns to cat')
    print("search(r'r(u)?ns','dog rns to cat'):", res)
    
    # 10. 零次或多次 *
    print("\n10. 零次或多次 *")
    res = re.search(r'ab*','a')
    print("search(r'ab*','a'):", res)
    res = re.search(r'ab*','abbbbbbbbbb')
    print("search(r'ab*','abbbbbbbbbb'):", res)
    
    # 11. 一次或多次 +
    print("\n11. 一次或多次 +")
    res = re.search(r'ab+','a')
    print("search(r'ab+','a'):", res)
    res = re.search(r'ab+','abbbbbbbbbb')
    print("search(r'ab+','abbbbbbbbbb'):", res)
    
    # 12. 指定次数 {n,m}
    print("\n12. 指定次数 {n,m}")
    res = re.search(r'ab{1,10}','a')
    print("search(r'ab{1,10}','a'):", res)
    res = re.search(r'ab{1,10}','abbbbbbbbbb')
    print("search(r'ab{1,10}','abbbbbbbbbb'):", res)

def demo_groups():
    print("\n=== 分组匹配 ===")
    # 13. 分组匹配
    print("\n13. 分组匹配")
    res = re.search(r'ID: (\d+), Name: (.+)','ID: 123456789, Name: a/b*c;d')
    print("search(r'ID: (\\d+), Name: (.+)','ID: 123456789, Name: a/b*c;d'):")
    print("group():", res.group())
    print("group(1):", res.group(1))
    print("group(2):", res.group(2))
    
    # 14. 命名分组
    print("\n14. 命名分组")
    res = re.search(r'ID: (?P<id>\d+), Name: (?P<name>.+)','ID: 123456789, Name: a/b*c;d')
    print("search(r'ID: (?P<id>\\d+), Name: (?P<name>.+)','ID: 123456789, Name: a/b*c;d'):")
    print("group('id'):", res.group('id'))
    print("group('name'):", res.group('name'))

def demo_functions():
    print("\n=== 正则函数 ===")
    # 15. findall
    print("\n15. findall")
    res = re.findall(r'r[ua]n','run ran ren')
    print("findall(r'r[ua]n','run ran ren'):", res)
    res = re.findall(r'(run|ran)','run ran ren')
    print("findall(r'(run|ran)','run ran ren'):", res)
    
    # 16. sub
    print("\n16. sub")
    res = re.sub(r'runs','catches','dog runs to cat')
    print("sub(r'runs','catches','dog runs to cat'):", res)
    
    # 17. split
    print("\n17. split")
    res = re.split(r'[,;\.\\]', 'a,b;c.d\e')
    print("split(r'[,;\.\\\\]', 'a,b;c.d\\e'):", res)
    
    # 18. compile
    print("\n18. compile")
    compile_re = re.compile(r'r[ua]n')
    res = compile_re.findall('run ran ren')
    print("compile_re.findall('run ran ren'):", res)

def demo_common_patterns():
    print("\n=== 常用正则模式 ===")
    # 数字校验
    print("\n数字校验:")
    print("1. 数字：^[0-9]*$ -", bool(re.match(r'^[0-9]*$', '123')))
    print("2. n位数字：^\\d{n}$ -", bool(re.match(r'^\d{3}$', '123')))
    print("3. 至少n位数字：^\\d{n,}$ -", bool(re.match(r'^\d{3,}$', '1234')))
    print("4. m-n位数字：^\\d{m,n}$ -", bool(re.match(r'^\d{2,4}$', '123')))
    
    # 字符校验
    print("\n字符校验:")
    print("1. 汉字：^[\\u4e00-\\u9fa5]{0,}$ -", bool(re.match(r'^[\u4e00-\u9fa5]+$', '中文')))
    print("2. 英文和数字：^[A-Za-z0-9]+$ -", bool(re.match(r'^[A-Za-z0-9]+$', 'Abc123')))
    print("3. 长度为3-20的所有字符：^.{3,20}$ -", bool(re.match(r'^.{3,20}$', 'abc123')))
    
    # 特殊需求
    print("\n特殊需求:")
    print("1. Email地址：^\\w+([-+.]\\w+)*@\\w+([-.]\\w+)*\\.\\w+([-.]\\w+)*$ -", 
          bool(re.match(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', 'test@example.com')))
    print("2. 手机号码：^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\\d{8}$ -", 
          bool(re.match(r'^(13[0-9]|14[57]|15[0-35-9]|18[0-35-9])\d{8}$', '13800138000')))
    print("3. 身份证号：^\\d{15}|\\d{18}$ -", bool(re.match(r'^\d{15}|\d{18}$', '123456789012345678')))
    print("4. 腾讯QQ号：[1-9][0-9]{4,} -", bool(re.match(r'[1-9][0-9]{4,}', '10000')))
    print("5. 中国邮政编码：[1-9]\\d{5}(?!\\d) -", bool(re.match(r'[1-9]\d{5}(?!\d)', '100000')))

if __name__ == "__main__":
    print("=== Python正则表达式演示 ===")
    demo_basic_patterns()
    demo_special_chars()
    demo_quantifiers()
    demo_groups()
    demo_functions()
    demo_common_patterns()
    print("\n=== 演示结束 ===")