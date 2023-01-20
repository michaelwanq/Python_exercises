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