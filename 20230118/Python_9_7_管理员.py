# 练习 9-7：管理员
# 管理员是一种特殊的用户。编写一个名为 Admin 的类，让它继承为完成练习 9-3 或练习 9-5 而编写的 User 类。
# 添加一个名为 privileges 的属性，用于存储一个由字符串（如"can add post"、"can delete post"、"can ban user"等）组成的列表。
# 编写一个名为 show_privileges()的方法，显示管理员的权限。创建一个 Admin实例，并调用这个方法。
class User:
    """创建User类"""

    def __init__(self, first_name, last_name):
        """初始化User类的属性"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """用户名称描述方法"""
        full_name = self.first_name + ' ' + self.last_name
        print(full_name)

    def greet_user(self):
        """给用户的问候语"""
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

user = Admin('michael','wan')
user.privileges = ["can add post","can delete post","can ban user"]
user.show_privileges()
# privilege = Admin.show_privileges()
# print(privilege)

