# 练习 4-2：动物 想出至少三种有共同特征的动物，将其名称存储在一个列表中，
# 再使用 for 循环将每种动物的名称打印出来。
# 修改这个程序，使其针对每种动物都打印一个句子，下面是一个例子。
# A dog would make a great pet.
#  在程序末尾添加一行代码，指出这些动物的共同之处，如打印下面这样的句子。
# Any of these animals would make a great pet!
animals = ['dog','pig','rabbit']
for animal in animals:
    print(animal)
for animal in animals:
    message = "A " + animal + " would make a great pet."
    print(message)
print("Any of these animals would make a great pet!")