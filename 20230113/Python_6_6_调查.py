# 练习 6-6：调查
# 在 6.3.1 节编写的程序 favorite_languages.py 中执行以下操作。
# 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。
# 遍历这个人员名单。对于已参与调查的人，打印一条消息表示感谢；对于还未参与调查的人，打印一条消息邀请他参加。
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
users = ['jen','jobs','edward']
for user in users:
# 使用字典.key()或者字典.value()可以分别获取key或者value
    if user in favorite_languages.keys():
        print(f"Thank you for taking the poll, {user.title()}!")
    else:
        print(f"{user.title()}, what's your favorite programming language?")

# farovite_user = []
# for n,l in favorite_languages.items():
#     #print(n)
#     farovite_user.pop(str(n))
# # for user in users:
# #         if user in farovite_user:
# #             print(f"{user}，感谢参与调查！")
# #         else:
# #             print(f'{user}，很荣幸邀请您参与调查！')

