# 练习 8-4：大号 T恤
# 修改函数 make_shirt()，使其在默认情况下制作一件印有“I love Python”字样的大号T恤。
# 调用这个函数来制作：一件印有默认字样的大号T恤，一件印有默认字样的中号T恤，以及一件印有其他字样的T恤（尺码无关紧要）。
def make_shirt(size, pattern='I love Python'):
    print(f"你需要的T恤尺码是{size},T恤上的字样是{pattern}。")


make_shirt('L码')
make_shirt(size='M码')
make_shirt(size='S码', pattern='学习进步')
