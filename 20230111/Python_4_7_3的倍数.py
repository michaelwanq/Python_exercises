# 练习 4-7：3 的倍数 创建一个列表，其中包含 3～30 能被 3 整除的数，
# 再使用一个 for 循环将这个列表中的数打印出来。
numbers = list(range(3,31))
numbers2 = []
for number in numbers:
    if number % 3 == 0:
        numbers2.append(number)
print(numbers2)
