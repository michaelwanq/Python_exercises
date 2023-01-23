# 练习 10-4：访客名单
# 编写一个 while 循环，提示用户输入名字。
# 用户输入名字后，在屏幕上打印一句问候语，并将一条到访记录添加到文件 guest_book.txt 中。
# 确保这个文件中的每条记录都独占一行。
# guest_book = 'guest_book.txt'
# while not quit:
#     username = input('请输入你的用户名：')
#     print(f'{username}，欢迎你的到来，祝你游戏愉快！')
#     with open(guest_book,'a') as f:
#         f.writelines(username)
# with open(guest_book) as f:
#     line = f.readlines()
#     print(line)
filename = 'guest_book.txt'
print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{name}\n")
        print(f"Hi {name}, you've been added to the guest book.")
