# 练习 9-12：多个模块
# 将 User 类存储在一个模块中，并将 Privileges 类和 Admin类存储在另一个模块中。
# 再创建一个文件，在其中创建一个 Admin 实例并对其调用方法show_privileges()，以确认一切依然能够正确运行。
from Admin import Admin

admin = Admin("Alice", 'Bob')
user = admin.describe_user()
print(user)
admin.privileges = ['can reset passwords', 'can moderate discussions', 'can suspend accounts']
privilege = admin.show_privileges()
print(f"管理员{user}的权限有{privilege}。")
