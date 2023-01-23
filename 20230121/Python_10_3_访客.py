# 练习 10-3：访客
# 编写一个程序，提示用户输入名字。用户做出响应后，将其名字写入文件 guest.txt 中。
file = "guest.txt"

username = input("请输入你的用户名：")
with open(file, 'w') as f:
    f.write(username)

with open(file) as f:
    name = f.read()
    print(f'{name},欢迎登录')
