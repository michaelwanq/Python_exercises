# 练习 10-11：喜欢的数
# 编写一个程序，提示用户输入喜欢的数，并使用 json.dump()将这个数存储到文件中。
# 再编写一个程序，从文件中读取这个值，并打印如下所示的消息。
# I know your favorite number! It’s _____.
import json

file = 'favorite_number.json'
numbers = input('请输入你喜欢的数字：')
with open(file, 'w') as f:
    json.dump(numbers, f)

with open(file) as f:
    favorite_number = json.load(f)
print(f'I know your favorite number! It’s {favorite_number}.')
