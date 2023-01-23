# 练习 10-5：调查
# 编写一个 while 循环，询问用户为何喜欢编程。每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。
# reasons = 'reason.txt'
# while True:
#     reason = input('请输入你喜欢python编程的原因：')
#     if reason == 'quit':
#         break
#     else:
#         with open(reasons, 'a') as f:
#             f.write(f'{reason}\n')
#
# print('祝你学习愉快，学有所成！')

# 参考答案
filename = 'programming_poll.txt'
responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)
    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break
with open(filename, 'a') as f:
    for response in responses:
        f.write(f"{response}\n")
