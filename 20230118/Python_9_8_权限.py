# 练习 9-8：权限
# 编写一个名为 Privileges 的类，它只有一个属性 privileges，其中存储了练习 9-7 所述的字符串列表。
# 将方法 show_privileges()移到这个类中。在 Admin类中，将一个 Privileges 实例用作其属性。
# 创建一个 Admin 实例，并使用方法show_privileges()来显示其权限。
class Privileges:
    """定义Privileges类"""
    def __init__(self,privileges):
        self.privileges = privileges

    def show_privileges(self):
        """显示管理员权限方法"""
        print(f'管理员权限有: {self.privileges}')

prvilege = ["can add post","can delete post","can ban user"]
admin = Privileges(prvilege)
admin.show_privileges()
