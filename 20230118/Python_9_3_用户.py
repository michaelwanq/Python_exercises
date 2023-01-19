# 练习 9-3：用户
# 创建一个名为 User 的类，其中包含属性 first_name 和 last_name，以及用户简介通常会存储的其他几个属性。
# 在类 User 中定义一个名为 describe_user()的方法，用于打印用户信息摘要。
# 再定义一个名为 greet_user()的方法，用于向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例调用上述两个方法。
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

userA = User('michael','wan')
userA.describe_user()
userA.greet_user()
userB = User('hawk','wan')
userB.describe_user()
userB.greet_user()
userC = User('jing','du')
userC.describe_user()
userC.greet_user()

# '''参考答案'''
# class User():
#     """一个表示用户的简单类。"""
#
#     def __init__(self, first_name, last_name, username, email, location):
#
#         """初始化用户。"""
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.username = username
#         self.email = email
#         self.location = location.title()
#
#     def describe_user(self):
#
#         """显示用户信息摘要。"""
#         print(f"\n{self.first_name} {self.last_name}")
#         print(f"\tUsername: {self.username}")
#         print(f"\tEmail: {self.email}")
#         print(f"\tLocation: {self.location}")
#
#     def greet_user(self):
#
#         """向用户发出个性化的问候。"""
#         print(f"\nWelcome back, {self.username}!")
#
#
# eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
# eric.describe_user()
# eric.greet_user()
# willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
# willie.describe_user()
# willie.greet_user()