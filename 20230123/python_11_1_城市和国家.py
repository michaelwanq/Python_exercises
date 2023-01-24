# 练习 11-1：城市和国家
# 编写一个函数，它接受两个形参：一个城市名和一个国家名。
# 这个函数返回一个格式为 City, Country 的字符串，如 Santiago, Chile。
# 将这个函数存储在一个名为 city_functions.py 的模块中。
# 创建一个名为 test_cities.py 的程序，对刚才编写的函数进行测试（别忘了，需要导入模块 unittest 和要测试的函数）。
# 编写一个名为 test_city_country()的方法，核实使用类似于'santiago'和'chile'这样的值来调用前述函数时，得到的字符串是正确的。
# 运行test_cities.py，确认测试 test_city_country()通过了。
import unittest
# def country_city(countries,cities):
#     country = countries.title()
#     city = cities.title()
#     country_city = city + ',' + country
#     print(f'你输入的城市和国家名称是：{country_city}')

import unittest
from city_functions import format_city


class CitiesTestCase(unittest.TestCase):
    """测试'city_functions.py'。"""

    def test_city_country(self):

        """传入简单的城市和国家可行吗？"""
        santiago_chile = format_city('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')

    # def test_city_country_population(self):
    #
    #     """可向形参 population 传递值吗？"""
    #     santiago_chile = city_country('santiago', 'chile', population=5_000_000)
    #     self.assertEqual(santiago_chile, 'Santiago, Chile - population 5000000')

unittest.main()
