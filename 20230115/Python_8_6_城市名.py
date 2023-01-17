# 练习 8-6：城市名
# 编写一个名为describe_city()的函数，它接受城市的名称及其所属的国家。
# 这个函数应返回一个格式类似于下面的字符串："Santiago, Chile"
# 至少使用三个城市国家对来调用这个函数，并打印它返回的值。
def describe_city(city_name,country):
    print(f'{city_name.title()} is in {country.title()}.')

describe_city('london','england')
describe_city('shanghai','china')
describe_city('new york', 'usa')