print("list（列表）")
classmates = []

classmates.append('Adam')
classmates.append("村长")
print(classmates)

classmates.insert(1,'Jack')
classmates.insert(0,"沸羊羊")
print(classmates)

classmates[3] = "灰太狼"
print(classmates)

classmates.pop(2)
print(classmates)

print("----------------我--是--分--割--线-------------------")
print("tuple（元组）：")

t_1 = (1,2)
t_2 = ()    #定义空元组
t_3 = (1)
t_4 = (1,)  #一个元素的tuple在后面要跟一个逗号
print(t_1)
print(t_2)
print(t_3)
print(t_4)

# “可变”元组    实际上可变的是其内部的列表
t = ('a','b','c',['01','ABC'])
print(t)
t[3][0] = "X"
t[3][1] = "Y"
print(t)

print("练习")
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Bob:
print(L[2][2])
