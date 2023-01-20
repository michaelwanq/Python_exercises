class User():
    '''创建User类'''
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print(full_name)

    def greet_user(self):
        print(self.first_name + ' ' + self.last_name + '，欢迎你的的到来！')

class Admin(User):
    """继承user类"""
    def __init__(self,first_name, last_name):
        """初始化父类属性"""
        super().__init__(first_name, last_name)
        self.privileges = []
    def show_privileges(self):
        """显示管理员权限方法"""
        print(f'管理员权限有: {self.privileges}')

class Privileges:
    """定义Privileges类"""
    def __init__(self,privileges):
        self.privileges = privileges

    def show_privileges(self):
        """显示管理员权限方法"""
        print(f'管理员权限有: {self.privileges}')

