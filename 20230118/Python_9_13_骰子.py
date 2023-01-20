# 练习 9-13：骰子
# 创建一个 Die 类，它包含一个名为 sides 的属性，该属性的默认值为 6。
# 编写一个名为 roll_die()的方法，它打印位于 1 和骰子面数之间的随机数。
# 创建一个 6 面的骰子再掷 10 次。
# 创建一个 10 面的骰子和一个 20 面的骰子，再分别掷 10 次。
class Die:
    """初始化骰子"""
    def __init__(self,sides):
        """初始化骰子的点数属性"""
        self.sides = 6

    def roll_die(self):
        number = range(1,11)

