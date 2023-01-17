# 对浮点数，保留小数点后几位
print('{:0.3f}'.format(50.5 / 220.5))
# print 格式化字符串
num = int(input('请输入一个十进制的整数：'))  # 将str 转为int类型
print(num,'的二进制数为：',bin(num))  # 第一种写法使用了个数可变的位置参数
print(str(num) + '的二进制数为：' + str(bin(num)))  # 第二种写法，使用“+”作为连接符 (+的左右均为str类型)
print('%s的二进制数为：%s' % (num, bin(num)))  # 第三种写法 格式化字符串
print('\033[0;35m{}的二进制数为：{}\033[m'.format(num, bin(num)))  # 第三种写法 格式化字符串
print(f'{num}的二进制数为：{bin(num)}')  # 第三种写法 格式化字符串
print('-'.center(50, '-'))
print(f'{num}的八进制数为{oct(num)}')
print(f'{num}的十六进制数为{hex(num)}')