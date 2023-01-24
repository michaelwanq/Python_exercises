# 练习 11-3：雇员
# 编写一个名为 Employee 的类，其方法__init__()接受名、姓和年薪，并将它们存储在属性中。
# 编写一个名为 give_raise()的方法，它默认将年薪增加5000美元，但也能够接受其他的年薪增加量。
# 为 Employee 编写一个测试用例，其中包含两个测试方法：test_give_default_raise()和 test_give_custom_raise()。
# 使用方法 setUp()，以免在每个测试方法中都新建雇员实例。运行这个测试用例，确认两个测试都通过了。
import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """测试模块 employee。"""


def setUp(self):
    """创建一个 Employee 实例，以便在测试中使用。"""
    self.eric = Employee('eric', 'matthes', 65_000)


def test_give_default_raise(self):
    """测试使用默认的年薪增加量是否可行。"""
    self.eric.give_raise()
    self.assertEqual(self.eric.salary, 70000)


def test_give_custom_raise(self):
    """测试自定义年薪增加量是否可行。"""
    self.eric.give_raise(10000)
    self.assertEqual(self.eric.salary, 75000)


if __name__ == '__main__':
    unittest.main()
