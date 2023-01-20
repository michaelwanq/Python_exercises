# 练习 9-13：骰子
# 创建一个 Die 类，它包含一个名为 sides 的属性，该属性的默认值为 6。
# 编写一个名为 roll_die()的方法，它打印位于 1 和骰子面数之间的随机数。
# 创建一个 6 面的骰子再掷 10 次。
# 创建一个 10 面的骰子和一个 20 面的骰子，再分别掷 10 次。
from random import randint

class Die:
    """初始化骰子"""

    def __init__(self, sides=6):
        """初始化骰子的点数属性"""
        self.sides = sides

    def roll_die(self):
        """返回一个位于 1 和骰子面数之间的随机数。"""
        return randint(1, self.sides)
        # side = self.sides + 1
        # number = range(1, side)
        # print(number)


def numbers(sides):
    die = Die(sides)
    i = 1
    while i <= 10:
        print(f"第{i}次投掷的骰子点数是：{die.roll_die()}。")
        i += 1


print("六面骰子投掷10次的结果是：")
die1 = numbers(6)
print("\n十面骰子投掷10次的结果是：")
die2 = numbers(10)
print("\n二十面骰子投掷10次的结果是：")
die3 = numbers(20)

# print(die.roll_die())
# i = 1
# while i <= 10:
#     print(f"第{i}次投掷的骰子点数是：{die1.roll_die()}。")
#     i += 1
