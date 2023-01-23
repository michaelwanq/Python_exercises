# 练习 10-9：静默的猫和狗
# 修改你在练习 10-8 中编写的 except 代码块，让程序在任意文件不存在时静默失败。
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading file: {filename}")
        print(contents)
