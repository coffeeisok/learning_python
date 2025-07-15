try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    # 将捕获的异常（除数是0）赋值给实例e
    # 打印e可以看详细的异常描述
    print('except:', e)
finally:
    print('finally...')
print('END')
