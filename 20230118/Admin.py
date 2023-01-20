from User import User


class Admin(User):
    """继承user类"""

    def __init__(self, first_name, last_name):
        """初始化父类属性"""
        super().__init__(first_name, last_name)
        self.privileges = []

    def show_privileges(self):
        """显示管理员权限方法"""
        # print(f'管理员权限有: {self.privileges}')
        return self.privileges


class Privileges:
    """定义Privileges类"""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        """显示管理员权限方法"""
        print(f'管理员权限有: {self.privileges}')
