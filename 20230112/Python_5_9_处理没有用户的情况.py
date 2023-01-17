# 练习 5-9：处理没有用户的情形
# 在为完成练习 5-8 编写的程序中，添加一条 if 语句，检查用户名列表是否为空。
# 如果为空，就打印如下消息。
# We need to find some users!
# 删除列表中的所有用户名，确定将打印正确的消息。
# admin = ['alex','bob','carry','admin','dani']
# users = ['alex','bob']
users = []
if users:
    print("用户列表:",users)
else:
    print("We need to find some users!")
# user = 'hawk'
# user = 'bob'
# user = 'admin'
# if user in admin:
#     if user == 'admin':
#         print("Hello admin, would you like to see a status report?")
#     else:
#         print("Hello %s, thank you for logging in again." %user)
# else:
#     print("很抱歉，你输入的用户名:%s，没有注册！" %user)
