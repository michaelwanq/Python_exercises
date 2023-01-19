# 练习 9-2：三家餐馆
# 根据为完成练习 9-1 而编写的类创建三个实例，并对每个实例调用方法 describe_restaurant()。
from restaurant import Restaurant

'''创建餐馆3个实例，调用describe_restaurant方法'''
a_restaurant = Restaurant('RA', '粤菜')
b_restaurant = Restaurant('RB', '湘菜')
c_restaurant = Restaurant('RC', '川菜')
a_restaurant.describe_restaurant()
b_restaurant.describe_restaurant()
c_restaurant.describe_restaurant()
