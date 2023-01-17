# 练习 6-10：喜欢的数 2
# 修改为完成练习 6-2 而编写的程序，让每个人都可以有多个喜欢的数，然后将每个人的名字及其喜欢的数打印出来。
# numbers = {
#     'userA': "1、2、3",
#     'userB': "4、5、6",
#     'userC': "7、8、9",
#     'userD': "10、11、12",
#     'userE': "13、14、15"
#     }
# for name,number in numbers.items():
#     print(f"{name} is like {number}.")

favorite_numbers = {
    'mandy': [42, 17],
    'micah': [42, 39, 56],
    'gus': [7, 12],
}
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"\t{number}")
