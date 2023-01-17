# 练习 4-6：奇数 通过给函数 range()指定第三个参数来创建一个列表，其中包含
# 1～20 的奇数，再使用一个 for 循环将这些数打印出来。
# range()函数的第三个参数是指定步长
# list()函数是将range()函数的生成的结果直接转换为数列
numbers = list(range(1,21,2))
for number in numbers:
	print("1-20中包含的奇数为：",number)