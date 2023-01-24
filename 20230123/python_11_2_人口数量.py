# 练习 11-2：人口数量
# 修改前面的函数，加上第三个必不可少的形参population，并返回一个格式为City,Country – population xxx 的字符串，
# 如 Santiago, Chile – population 5000000。
# 运行 test_cities.py，确认测试 test_city_country()未通过。
# 修改上述函数，将形参 population 设置为可选的。再次运行 test_cities.py，确认测试 test_city_country()又通过了。
# 再编写一个名为 test_city_country_population()的测试，
# 核实可以使用类似于'santiago'、'chile'和'population=5000000'这样的值来调用这个函数。
# 再次运行test_cities.py，确认测试 test_city_country_population()通过了。
import unittest
from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """测试'city_functions.py'。"""

    def test_city_country(self):

        """传入简单的城市和国家可行吗？"""
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')

    def test_city_country_population(self):

        """可向形参 population 传递值吗？"""
        santiago_chile = city_country('santiago', 'chile', population=5_000_000)
        self.assertEqual(santiago_chile, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
