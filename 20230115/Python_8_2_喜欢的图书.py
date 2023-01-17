# 练习 8-2：喜欢的图书
# 编写一个名为 favorite_book()的函数，其中包含一个名为title 的形参。
# 这个函数打印一条消息，下面是一个例子。
# One of my favorite books is Alice in Wonderland.
# 调用这个函数，并将一本图书的名称作为实参传递给它。
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}.")
favorite_book('Alice in Wonderland')
favorite_book('寻秦记')