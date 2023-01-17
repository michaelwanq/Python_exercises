# 练习 5-11：序数 序数表示位置，如 1st 和 2nd。序数大多以 th 结尾，只有 1、2和 3 例外。
# 在一个列表中存储数字 1～9。
# 遍历这个列表。
# 在循环中使用一个 if-elif-else 结构，以打印每个数字对应的序数。
# 输出内容应为"1st 2nd 3rd 4th 5th 6th 7th 8th 9th"，但每个序数都独占一行。
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print("%s的序数是：1st",%number)
    elif number == 1:
        print("%s的序数是：1st",%number)