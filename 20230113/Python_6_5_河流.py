# 练习 6-5：河流
# 创建一个字典，在其中存储三条重要河流及其流经的国家。
# 例如，一个键值对可能是'nile': 'egypt'。
# 使用循环为每条河流打印一条消息，下面是一个例子。
# The Nile runs through Egypt.
# 使用循环将该字典中每条河流的名字打印出来。
# 使用循环将该字典包含的每个国家的名字打印出来。
rivers = {'nile': 'egypt','changjiang': 'china','amazon': 'brazil'}
for n,c in rivers.items():
    print(f'The {n} runs through {c.title()}.')