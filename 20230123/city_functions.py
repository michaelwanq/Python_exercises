# def city_country(cities,countries,population=''):
#     country = countries.title()
#     city = cities.title()
#     city_country = f"'{city},{country}'"
#
#     # print(f'你输入的城市和国家名称是：{city_country}')
#     return city_country


def format_name(first, last, middle=''):
    """ 格式化一个姓名"""

    if middle:
        fullname = first + ' ' + middle + ' ' + last
    else:
        fullname = first + ' ' + last
    return fullname.title()


def format_city(city, country, population=''):
    """ 格式化一个国家和城市 """
    if population:
        city_country = city + ',' + country + ' - population' + ' ' + population
    else:
        city_country = city + ',' + country
    return city_country.title()
# city = city_country('santiago', 'chile')
# print(city)