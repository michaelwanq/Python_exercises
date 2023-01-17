# 练习 8-12：三明治
# 编写一个函数，它接受顾客要在三明治中添加的一系列食材。
# 这个函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，对顾客点的三明治进行概述。
# 调用这个函数三次，每次都提供不同数量的实参。
# def sandwich_toppings(customer, *topping):
#     print(f'{customer}购买的三明治配料表如下：')
#     sandwich_topping = topping
#     print(sandwich_topping)
#     for i in sandwich_topping:
#         print(f'\t{i}')
#
#
# a_topping = ['肉松', '海苔', '芝士']
# b_topping = ['西红柿', '肉松', '芝士']
# c_topping = ['火腿', '虾', '芝士']
# usera = 'alex'
# userb = 'bob'
# userc = 'candy'
# sandwich_toppings(usera, a_topping)
# sandwich_toppings(userb, b_topping)
# sandwich_toppings(userc, c_topping)

def make_sandwich(customer,*items):
    """使用指定的食材制作三明治。"""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print(f" ...adding {item} to your sandwich.")
    print(f"{customer},Your sandwich is ready!")


make_sandwich('alex','roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('bob','turkey', 'apple slices', 'honey mustard')
make_sandwich('candy','peanut butter', 'strawberry jam')
