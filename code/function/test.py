print("----------------我--是--分--割--线-------------------")
print("关于 map() 函数的代码：")

def f(x):
    return x * x

r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))

print("----------------我--是--分--割--线-------------------")

print("列表生成式：")
print("if在后：")
print([x for x in range(1, 11) if x % 2 == 0])

print("if在前：")
print([x if x % 2 == 0 else -x for x in range(1, 11)])

print("----------------我--是--分--割--线-------------------")
print("生成器：")

print("list：")
L = [x * x for x in range(10)]
print("generator：")
g = (x * x for x in range(10))
print(L)
print(g)
print("用next()",next(g))

for i in g:
    print(i,end=",")

print("\n斐波那契数列：")
# 1,1,2,3,5,8,13,21,34,...
def fib(max):
    n,a,b = 0, 0, 1
    while n < max:
        #print(b,end=",")
        yield b
        b = a+b
        a = b
        n += 1
    return 'done'
    
print(fib(6))

print("----------------我--是--分--割--线-------------------")
print("杨辉三角：")

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
def triangles():
    row = [1]
    while True:
        yield row
        row = [1]+[row[i] + row[i+1] for i in range(len(row)-1)] + [1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
