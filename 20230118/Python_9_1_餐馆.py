# 练习 9-1：餐馆
# 创建一个名为 Restaurant 的类，为其方法__init__()设置属性restaurant_name 和 cuisine_type。
# 创建一个名为 describe_restaurant()的方法和一个名为 open_restaurant()的方法，
# 前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
# 根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
class Restaurant():
    """一个表示餐馆的类。"""

    def __init__(self, restaurant_name, cuisine_type):
        '''初始化餐馆属性'''
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''餐馆的描述信息'''
        full_name = self.restaurant_name + '是一家经营' + self.cuisine_type + '风味的餐馆。'
        print(full_name)

    def open_restaurant(self):
        '''餐馆工作状态'''
        print(self.restaurant_name + '正在营业中。')


my_restaurant = Restaurant('小胖餐厅', '湘菜')
print('实例my_restaurant属性restaurant_name:' + my_restaurant.restaurant_name)
print('实例my_restaurant属性cuisine_type:' + my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# class Restaurant():
#     """一个表示餐馆的类。"""
#
#     def __init__(self, name, cuisine_type):
#         """初始化餐馆。"""
#         self.name = name.title()
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         """显示餐馆信息摘要。"""
#         msg = f"{self.name} serves wonderful {self.cuisine_type}."
#         print(f"\n{msg}")
#
#     def open_restaurant(self):
#         """显示一条消息，指出餐馆正在营业。"""
#         msg = f"{self.name} is open. Come on in!"
#         print(f"\n{msg}")
#
#
# restaurant = Restaurant('the mean queen', 'pizza')
# print(restaurant.name)
# print(restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
