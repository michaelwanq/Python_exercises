# 练习 10-8：猫和狗
# 创建文件 cats.txt 和 dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。
# 编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。
# 将这些代码放在一个 try-except 代码块中，以便在文件不存在时捕获 FileNotFound 错误，并显示一条友好的消息。
# 将任意一个文件移到另一个地方，并确认 except 代码块中的代码将正确执行。
cats_file = 'cats.txt'
dogs_file = 'dogs.txt'
try:
    with open(cats_file) as cat_file:
        cats = cat_file.readlines()
    print('猫咪的名字是：')
    for cat in cats:
        print(f'\t-{cat.rstrip()}')
    with open(dogs_file) as dog_file:
        dogs = dog_file.readlines()
    print('\n狗狗的名字是：')
    for dog in dogs:
        print(f'\t-{dog.rstrip()}')
except FileNotFoundError:
    print('\n抱歉，未找到你需要的文档！')