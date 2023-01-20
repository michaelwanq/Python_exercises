# 练习 9-10：导入Restaurant 类
# 将最新的 Restaurant 类存储在一个模块中。
# 在另一个文件中，导入 Restaurant 类，创建一个 Restaurant 实例并调用 Restaurant 的一个方法，以确认 import 语句正确无误。
# """方法一、导入模块中的一个类"""
# from restaurant import Restaurant
# restaurant_a = Restaurant('小胖餐厅','粤菜')
# restaurant_a.describe_restaurant()

"""方法二、导入模块"""
import restaurant
restaurant_a = restaurant.Restaurant('小胖餐厅','粤菜')
restaurant_a.open_restaurant()