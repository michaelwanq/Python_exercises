# 练习 8-3：T恤
# 编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。
# 这个函数应打印一个句子，概要地说明 T恤的尺码和字样。
# 使用位置实参调用该函数来制作一件T恤，再使用关键字实参来调用这个函数。
def make_shirt(size, pattern):
    print(f"你需要的T恤尺码是{size},T恤上的字样是{pattern}。")
make_shirt('XL码','小年快乐')
make_shirt(size='L码',pattern='健康平安')