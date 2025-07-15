# markdown
fmd = 'assets/Test_ReadWrite.md'
with open(fmd, 'r') as f:
    s = f.read()
    print("markdown格式：",s)

# 文本
fpath = 'assets/Test_ReadWrite.txt'
with open(fpath, 'r') as f:
    s = f.read()
    print("文本：",s)

print("-------------我是分割线---------------")    

# 图片
fimage = 'assets/17522077182628.jpg'
with open(fimage, 'rb') as f:
    s = f.read()
    print("图片：",s)
    
print("-------------我是分割线---------------")    
