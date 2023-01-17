# 练习 4-11：你的比萨，我的比萨 在你为完成练习 4-1 而编写的程序中，创建比萨
# 列表的副本，并将其赋给变量 friend_pizzas，再完成如下任务。
#  在原来的比萨列表中添加一种比萨。
#  在列表 friend_pizzas 中添加另一种比萨。
#  核实有两个不同的列表。为此，打印消息“My favorite pizzas are:”，再使用一个
# for 循环来打印第一个列表；打印消息“My friend’s favorite pizzas are:”，再使用
# 一个 for 循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。
pizzas = ['pizzaA','pizzaB','pizzaC']
friends_pizzas = pizzas[:]
pizzas.append("pizzaD")
friends_pizzas.append("pizzaE")
for pizza in pizzas:
	print("My favorite pizzas are:",pizza)
for pizza2 in friends_pizzas:
	print("My friend’s favorite pizzas are:",pizza2)