# 练习 6-8：宠物
# 创建多个表示宠物的字典，每个字典都包含宠物的类型及其主人的名字。
# 将这些字典存储在一个名为 pets 的列表中，再遍历该列表，并将有关每个宠物的所有信息都打印出来。
pets = []
petA = {'kind': 'cat','owner': 'alex'}
pets.append(petA)
petB = {'kind': 'dog','owner': 'bob'}
pets.append(petB)
petC = {'kind': 'panda','owner': 'ken'}
pets.append(petC)
# for pet in pets:
#     # print(pet)
#     kind = (pet['kind'])
#     owner = pet['owner']
#     print(f'{owner} have a {kind}.')
for pet in pets:
    print(f"\nHere's what I know about {pet['kind'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")