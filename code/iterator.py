list = [1,2,3,4]
it = iter(list)
print(next(it))
print("以下是接着遍历")
for x in it:
    print(x)


