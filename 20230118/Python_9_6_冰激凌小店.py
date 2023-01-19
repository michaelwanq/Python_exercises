# 练习 9-6：冰激凌小店
# 冰激凌小店是一种特殊的餐馆。编写一个名为 IceCreamStand的类，让它继承为完成练习 9-1 或练习 9-4 而编写的 Restaurant 类。
# 这两个版本的Restaurant 类都可以，挑选你更喜欢的那个即可。
# 添加一个名为 flavors 的属性，用于存储一个由各种口味的冰激凌组成的列表。
# 编写一个显示这些冰激凌的方法。创建一个IceCreamStand 实例，并调用这个方法。
class Restaurant():
    """一个表示餐馆的类。"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化餐馆属性"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """餐馆的描述信息"""
        full_name = self.restaurant_name + '是一家经营' + self.cuisine_type + '风味的餐馆。'
        print(full_name)

    def open_restaurant(self):
        """餐馆工作状态"""
        print(self.restaurant_name + '正在营业中。')

    def set_number_served(self, number_served):
        """让用户能够设置就餐人数。"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """让用户能够增加就餐人数。"""
        self.number_served += additional_served


class IceCreamStand(Restaurant):
     """一个表示冰激凌小店的类。"""
     def __init__(self, name, cuisine_type='ice_cream'):
         """初始化冰激凌小店。"""
         super().__init__(name, cuisine_type)
         self.flavors = []
     def show_flavors(self):
         """显示出售的冰激凌品种。"""
         print("\nWe have the following flavors available:")
         print(self.flavors)
         # for flavor in self.flavors:
         #    print(f"- {flavor.title()}")
big_one = IceCreamStand('The Big One')
icecream = ['vanilla', 'chocolate', 'black cherry']
big_one.flavors = icecream
big_one.describe_restaurant()
big_one.show_flavors()
