# 练习 9-14：彩票
# 创建一个列表或元组，其中包含 10 个数和 5 个字母。
# 从这个列表或元组中随机选择 4 个数或字母，并打印一条消息，指出只要彩票上是这 4 个数或字母，就中大奖了。

from random import choices

lottery = [5, 'a', 7, 8, 'b', 1, 3, 4, 'c', 6, 9, 2, 0, 'd']
print('以下4个号码为本次大奖的获奖号码：')
i = 1
while i <= 4:
    choice = choices(lottery)
    print(f'第{i}个号码是：{choice}')
    i += 1
