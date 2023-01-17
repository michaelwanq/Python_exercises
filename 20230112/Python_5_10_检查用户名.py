# 练习 5-10：检查用户名
# 按下面的说明编写一个程序，模拟网站如何确保每位用户的用户名都独一无二。
# 创建一个至少包含 5 个用户名的列表，并将其命名为 current_users。
# 再创建一个包含 5 个用户名的列表，将其命名为 new_users，并确保其中有一两个用户名也包含在列表 current_users 中。
# 遍历列表 new_users，对于其中的每个用户名，都检查它是否已被使用。如果是，就打印一条消息，指出需要输入别的用户名；
# 否则，打印一条消息，指出这个用户名未被使用。
# 确保比较时不区分大小写。换句话说，如果用户名'John'已被使用，应拒绝用户名'JOHN'。
# （为此，需要创建列表 current_users 的副本，其中包含当前所有用户名的小写版本。）
current_users = ['alex','bob','carry','admin','dani']
new_users = ['alex','ben','Carry','clark','tim']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("你输入的用户名是：%s，已被注册，请重新输入！" %new_user)
    else:
        print("你输入的用户名是：%s，未使用，可注册!" %new_user)