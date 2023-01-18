# 练习 9-4：就餐人数
# 在为完成练习 9-1 而编写的程序中，添加一个名为 number_served 的属性，并将其默认值设置为 0。
# 根据这个类创建一个名为 restaurant 的实例。
# 打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
# 添加一个名为 set_number_served()的方法，让你能够设置就餐人数。
# 调用这个方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为 increment_number_served()的方法，让你能够将就餐人数递增。
# 调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
class Restaurant():
    """一个表示餐馆的类。"""

    def __init__(self, restaurant_name, cuisine_type):
        '''初始化餐馆属性'''
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''餐馆的描述信息'''
        full_name = self.restaurant_name + '是一家经营' + self.cuisine_type + '风味的餐馆。'
        print(full_name)

    def open_restaurant(self):
        '''餐馆工作状态'''
        print(self.restaurant_name + '正在营业中。')

    def set_number_served(self, number_served):
        """让用户能够设置就餐人数。"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """让用户能够增加就餐人数。"""
        self.number_served += additional_served

restaurant = Restaurant('克茗冰室','香港茶餐厅')
restaurant.number_served = 120
print(f"Number served: {restaurant.number_served}")
restaurant.set_number_served(1257)
print(f"Number served: {restaurant.number_served}")
restaurant.increment_number_served(143)
print(f"Number served: {restaurant.number_served}")
