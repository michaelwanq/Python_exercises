# 练习 8-9：消息
# 创建一个列表，其中包含一系列简短的文本消息。
# 将该列表传递给一个名为 show_messages()的函数，这个函数会打印列表中的每条文本消息。
def show_message(messages):
    """打印列表中的所有消息"""
    for message in messages:
        print(message)


messages = ['我是这个系统的管理员', '这是我的测试列表', '作为形参传递给show_message函数']
print('你输入的列表信息是：')
print(messages)
show_message(messages)

# def show_messages(messages):
#     """打印列表中的所有消息"""
#     for message in messages:
#         print(message)
#
#
# messages = ["hello there", "how are u?", ":)"]
# show_messages(messages)
