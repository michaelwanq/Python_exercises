# 练习 8-16：导入
# 选择一个你编写的且只包含一个函数的程序，将该函数放在另一个文件中。
# 在主程序文件中，使用下述各种方法导入这个函数，再调用它：
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *
import printing_functions as a
# from printing_functions import *

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
a.print_models(unprinted_designs, completed_models)
a.show_completed_models(completed_models)