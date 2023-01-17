# 练习 7-4：比萨配料
# 编写一个循环，提示用户输入一系列比萨配料，并在用户输入'quit'时结束循环。
# 每当用户输入一种配料后，都打印一条消息，指出我们会在比萨中添加这种配料。
toppings = []
while True:
    peiliao = input("请输入你需要的披萨配料：")
    if peiliao != 'quit':
        toppings.append(peiliao)
        print(f'您的披萨已添加配料：{peiliao}')
    else:
        break
print('您的披萨全部配料表如下：')
for topping in toppings:
    print(f'\t{topping}')

# prompt = "\nWhat topping would you like on your toppings?"
# prompt += "\nEnter 'quit' when you are finished: "
# while True:
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f" I'll add {topping} to your toppings.")
#     else:
#         break