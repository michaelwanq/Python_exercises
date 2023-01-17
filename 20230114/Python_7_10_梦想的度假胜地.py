# 练习 7-10：梦想的度假胜地
# 编写一个程序，调查用户梦想的度假胜地。使用类似于下面的提示，并编写一个打印调查结果的代码块。
# If you could visit one place in the world, where would you go?
citys = []
while True:
    city = input('If you could visit one place in the world, where would you go?')
    if city != 'quit':
        citys.append(city)
    else:
        break
print('你梦想的度假胜地包括：')
for city in citys:
    print(f'\t{city}')