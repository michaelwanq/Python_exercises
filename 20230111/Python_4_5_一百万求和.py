# 练习 4-5：一百万求和 创建一个包含数 1～1 000 000的列表，再使用 min()和 max()
# 核实该列表确实是从 1 开始、到 1 000 000 结束的。另外，对这个列表调用函数 sum()，
# 看看 Python 将一百万个数相加需要多长时间。
import time
start = time.perf_counter()
numbers = []
for number in range(1,1000001):
    numbers.append(number)
print(numbers[-10:])
print(min(numbers))
print(max(numbers))
print(sum(numbers))
end = time.perf_counter()
print("程序运行耗时:", end-start)
