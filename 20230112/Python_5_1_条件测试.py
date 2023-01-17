# 练习 5-1：条件测试 编写一系列条件测试，将每个测试以及对其结果的预测和实
# 际结果打印出来。你编写的代码应类似于下面这样：
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
#  详细研究实际结果，直到你明白它为何为 True 或 False。
#  创建至少 10 个测试，且其中结果分别为 True 和 False 的测试都至少有 5 个。
car = 'audi'
if car == 'subaru':
    print("Is car == 'subaru'? I predict True.")
if car != 'subaru':
    print("Is car == 'subaru'? I predict False.")
if car == 'audi':
    print(car == 'audi')
if car != 'audi':
    print("\nIs car == 'audi'? I predict False.")