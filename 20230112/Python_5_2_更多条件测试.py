# 练习 5-2：更多条件测试 你并非只能创建 20 个测试。如果想尝试做更多比较，可
# 再编写一些测试，并将它们加入 conditional_tests.py 中。对于下面列出的各种情况，至
# 少编写两个结果分别为 True 和 False 的测试。
#  检查两个字符串相等和不等。
#  使用方法 lower()的测试。
#  涉及相等、不等、大于、小于、大于等于和小于等于的数值测试。
#  使用关键字 and 和 or 的测试。
#  测试特定的值是否包含在列表中。
#  测试特定的值是否未包含在列表中。

# car2 = 'subaru'
# # car2 = 'audi'
# # car2 = 'Subaru'
# car2 = 'Audi'
# if car2.lower() == car2.lower():
#     print("这两个车是同一品牌。")
# else:
#     print("这两个车不是一个品牌。")

# number2 = 9
# # number2 = 6
# number2 = 6
# if number2 > number2:
#     print("数字2比数字2大。")
# else:
#     print("这两个数字不相等")

# car1 = 'subaru'
# car2 = 'audi'
# colour1 = 'red'
# colour2 = 'black'
# if car2 == 'subaru' and colour1 == 'red':
#     print("这辆车是红色斯巴鲁汽车。")
# elif car2 == 'subaru' and colour1 == 'black':
#     print("这辆车是黑色斯巴鲁汽车。")
# elif car2 == 'audi' and colour1 == 'red':
#     print("这辆车是红色奥迪汽车。")
# elif car2 == 'audi' and colour1 == 'black':
#     print("这辆车是黑色奥迪汽车。")

cars = ['audi','benz','subaru']
car = 'Audi'
if car in cars:
    print("您选择的是汽车品牌本店有现货。")
else:
    print("很抱歉，您选择的汽车品牌本店未销售。")