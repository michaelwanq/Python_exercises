# 练习 6-11：城市
# 创建一个名为 cities 的字典，将三个城市名用作键。
# 对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。
# 在表示每座城市的字典中，应包含 country、population 和 nearby mountains 等键。
# 将每座城市的名字以及有关信息都打印出来。
cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'nearby mountains': 'andes',
    },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'nearby mountains': 'alaska range',
    },
    'kathmandu': {
        'country': 'nepal',
        'population': 975_453,
        'nearby mountains': 'himilaya',
    }
}
for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()
    print(f"\n{city.title()} is in {country}.")
    print(f"It has a population of about {population}.")
    print(f"The {mountains} mounats are nearby.")
