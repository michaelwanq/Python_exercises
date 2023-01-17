# 练习 4-9：立方解析 使用列表解析生成一个列表，其中包含前 10 个整数的立方。
# numbers = range(1,11)
# for number in numbers:
#     triangle = number ** 3
#     message = str(number) + " 的立方是： " + str(triangle)
#     print(message)

numbers = [number ** 3 for number in range(1,11)]
print(numbers)
