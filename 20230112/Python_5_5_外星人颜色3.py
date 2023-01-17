# 练习 5-5：外星人颜色 3 将练习 5-4 中的 if-else 结构改为 if-elif-else 结构。
# 如果外星人是绿色的，就打印一条消息，指出玩家获得了 5 分。
# 如果外星人是黄色的，就打印一条消息，指出玩家获得了 10 分。
# 如果外星人是红色的，就打印一条消息，指出玩家获得了 15 分。
# 编写这个程序的三个版本，分别在外星人为绿色、黄色和红色时打印一条消息。

# # 版本1
# # alian_colour = 'green'
# alian_colour = 'yellow'
# # alian_colour = 'red'
# if alian_colour == 'green':
#     print("恭喜你击败绿色外星人，获得5分！")
# elif alian_colour == 'yellow':
#     print("恭喜你击败黄色外星人，获得10分")
# elif alian_colour == 'red':
#     print("恭喜你击败红色外星人，获得15分")

# # 版本2
# # alian_colour = 'green'
# alian_colour = 'yellow'
# # alian_colour = 'red'
# if alian_colour == 'green':
#     print("恭喜你击败绿色外星人，获得5分！")
# elif alian_colour == 'yellow':
#     print("恭喜你击败黄色外星人，获得10分")
# else:
#     print("恭喜你击败红色外星人，获得15分")

# 版本3
# alian_colour = 'green'
# alian_colour = 'yellow'
alian_colour = 'red'
if alian_colour == 'green':
    print("恭喜你击败绿色外星人，获得5分！")
if alian_colour == 'yellow':
    print("恭喜你击败黄色外星人，获得10分")
if alian_colour == 'red':
    print("恭喜你击败红色外星人，获得15分")