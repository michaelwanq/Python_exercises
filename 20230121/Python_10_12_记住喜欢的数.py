# 练习 10-12：记住喜欢的数
# 将练习 10-11 中的程序合二为一。如果存储了用户喜欢的数，就向用户显示它，否则提示用户输入喜欢的数并将其存储到文件中。
# 运行这个程序两次，看看它能否像预期的那样工作。
import json

try:
    with open('favorite_number.json') as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What's your favorite number? ")
    with open('favorite_number.json', 'w') as f:
        json.dump(number, f)
    print("Thanks, I'll remember that.")
else:
    print(f"I know your favorite number! It's {number}.")
