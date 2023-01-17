# 练习 8-11：消息归档
# 修改你为完成练习8-10而编写的程序，在调用函数send_messages()时，向它传递消息列表的副本。
# 调用函数 send_messages()后，将两个列表都打印出来，确认保留了原始列表中的消息。
def show_message(messages):
    """打印列表中的所有消息"""
    for message in messages:
        print(message)

def send_messages(messages,sent_messages):
    """打印列表中的所有消息并传递给sent_message数列"""
    while messages:
        for message in messages:
            print(message)
            temp_message = messages.pop()
            sent_messages.append(temp_message)
    return sent_messages

messages = ['我是这个系统的管理员', '这是我的测试列表', '作为形参传递给show_message函数']
print('你输入的列表信息是：')
print(messages)
sent_messages = []
sent_message = send_messages(messages[:],sent_messages)
print(f'这是现在的message列表：{messages}')
print(f'这是现在的sent_message列表：{sent_messages}')