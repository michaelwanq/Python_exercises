# 练习 9-11：导入Admin 类
# 以为完成练习 9-8 而做的工作为基础。将 User 类、Privileges 类和 Admin 类存储在一个模块中，再创建一个文件，
# 在其中创建一个 Admin实例并对其调用方法 show_privileges()，以确认一切都能正确运行。
# from Admin import Admin
# eric = Admin('eric', 'matthes')
# eric.describe_user()
# eric_privileges = [
#  'can reset passwords',
#  'can moderate discussions',
#  'can suspend accounts'
#  ]
# eric.Privileges.privileges = eric_privileges
# print(f"\nThe admin {eric.username} has these privileges: ")
# eric.Privileges.show_privileges()
from Admin import Admin
admin = Admin("Alice", 'Bob')
user = admin.describe_user()
admin.privileges = ['can reset passwords','can moderate discussions','can suspend accounts']
privilege = admin.show_privileges()
print(f"管理员{user}的权限有{privilege}。")