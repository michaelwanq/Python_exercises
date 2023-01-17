# 练习 4-8：立方 将同一个数乘三次称为立方。例如，在 Python 中，
# 2 的立方用2**3 表示。请创建一个列表，其中包含前 10 个整数（1～10）的立方，
# 再使用一个 for循环将这些立方数打印出来。
numbers = range(1,11)
for number in numbers:
    triangle = number ** 3
    message = str(number) + " 的立方是： " + str(triangle)
    print(message)
