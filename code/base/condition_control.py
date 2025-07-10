print("if...elif...else")
height = 1.75
weight = 80.5

bmi = weight / (height ** 2)
print(bmi)
if bmi <18.5:
    print("过轻")
elif (18.5 <= bmi <=25):
    print("正常")
elif (25 <= bmi <= 28):
    print("过重")
elif (28 <= bmi <= 32):
    print("肥胖")
elif bmi > 32 :
    print("严重肥胖")

print("----------------我--是--分--割--线-------------------")
print("match...case部分：")

age = 15
match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')

args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')

