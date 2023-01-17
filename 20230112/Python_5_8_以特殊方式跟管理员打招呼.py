# 练习 5-8：以特殊方式跟管理员打招呼
# 创建一个至少包含 5 个用户名的列表，且其中一个用户名为'admin'。
# 想象你要编写代码，在每位用户登录网站后都打印一条问候消息。
# 遍历用户名列表，并向每位用户打印一条问候消息。
# 如果用户名为'admin'，就打印一条特殊的问候消息，如下所示。
# Hello admin, would you like to see a status report?
# 否则，打印一条普通的问候消息，如下所示。
# Hello Jaden, thank you for logging in again.
admin = ['alex','bob','carry','admin','dani']
# user = 'hawk'
# user = 'bob'
user = 'admin'
if user in admin:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello %s, thank you for logging in again." %user)
else:
    print("很抱歉，你输入的用户名:%s，没有注册！" %user)