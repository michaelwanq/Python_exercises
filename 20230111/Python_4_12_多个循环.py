# 练习 4-12：使用多个循环 在本节中，为节省篇幅，程序 foods.py 的每个版本都没
# 有使用 for 循环来打印列表。请选择一个版本的 foods.py，在其中编写两个 for 循环，
# 将各个食品列表打印出来。
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
for food in my_foods:
    print("My favorite foods are:",food)
for food2 in friend_foods:
    print("My friend's favorite foods are:",food2)