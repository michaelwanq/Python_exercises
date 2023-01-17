# 练习 6-2：喜欢的数
# 使用一个字典来存储一些人喜欢的数。请想出 5 个人的名字，并将这些名字用作字典中的键；
# 找出每个人喜欢的一个数，并将这些数作为值存储在字典中。
# 打印每个人的名字和喜欢的数。
# 为了让这个程序更有趣，通过询问朋友确保数据是真实的。
numbers = {'userA': 3,'userB': 6,'userC': 9,'userD': 12,'userE': 15}
for name,number in numbers.items():
    print(f"{name} is like {number}.")
