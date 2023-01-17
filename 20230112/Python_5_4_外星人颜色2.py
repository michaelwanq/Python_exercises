# 练习 5-4：外星人颜色 2
# 像练习 5-3 那样设置外星人的颜色，并编写一个 if-else 结构。
# 如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了 5 分。
# 如果外星人不是绿色的，就打印一条消息，指出玩家获得了 10 分。
# 编写这个程序的两个版本，在一个版本中执行 if 代码块，在另一个版本中执行else 代码块。

# 通告测试版本
alien_color = 'green'
if alien_color == 'green':
    print("第一回合")
    print("恭喜你，你射杀了绿色外星人，获得5分。")
else:
    print("第一回合")
    print("恭喜你，你射杀了boss，获得10分。")
# elif alien_color == 'yellow':
#     print("恭喜你，你射杀了黄色外星人，获得4分。")
# elif alien_color == 'red':
#     print("恭喜你，你射杀了黄色外星人，获得3分。")

# 没有通告测试版本
alien_color = 'boss'
if alien_color == 'green':
    print("第二回合")
    print("恭喜你，你射杀了绿色外星人，获得5分。")
else:
    print("第二回合")
    print("恭喜你，你射杀了boss，获得10分。")
# elif alien_color == 'yellow':
#     print("恭喜你，你射杀了黄色外星人，获得4分。")
# elif alien_color == 'red':
#     print("恭喜你，你射杀了黄色外星人，获得3分。")