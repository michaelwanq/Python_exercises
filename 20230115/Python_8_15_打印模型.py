# 练习 8-15：打印模型
# 将示例 printing_models.py 中的函数放在一个名为 printing_functions.py的文件中。
# 在printing_models.py的开头编写一条 import 语句，并修改该文件以使用导入的函数。
# from printing_functions import print_models
# from printing_functions import show_completed_models
# from printing_functions import show_completed_models
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止。
    打印每个设计后，都将其移到列表 completed_models 中。
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型。"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
