# 练习 8-15：打印模型
# 将示例 printing_models.py 中的函数放在一个名为 printing_functions.py的文件中。
# 在printing_models.py的开头编写一条 import 语句，并修改该文件以使用导入的函数。
# from printing_functions import print_models
# from printing_functions import show_completed_models
import printing_functions

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)
