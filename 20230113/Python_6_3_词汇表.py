# 练习 6-3：词汇表
# Python 字典可用于模拟现实生活中的字典。为避免混淆，我们将后者称为词汇表。
# 想出你在前面学过的 5 个编程术语，将其用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
# 以整洁的方式打印每个术语及其含义。
# 为此，可先打印术语，在它后面加上一个冒号，再打印其含义；
glossarys = {
 'string': 'A series of characters.',
 'comment': 'A note in a program that the Python interpreter ignores.',
 'list': 'A collection of items in a particular order.',
 'loop': 'Work through a collection of items, one at a time.',
 'dictionary': "A collection of key-value pairs.",
 }

word = 'string'
print(f"\n{word.title()}: {glossarys[word]}")
word = 'comment'
print(f"\n{word.title()}: {glossarys[word]}")
word = 'list'
print(f"\n{word.title()}: {glossarys[word]}")
word = 'loop'
print(f"\n{word.title()}: {glossarys[word]}")
word = 'dictionary'
print(f"\n{word.title()}: {glossarys[word]}")