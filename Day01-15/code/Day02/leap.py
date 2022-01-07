"""
输入年份 如果是闰年输出True 否则输出False

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\或()折行
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)

# 数字1为真，0为假
print(1 and 1, 1 and 0, 0 and 1)  # 1 0 0
print(1 or 1, 1 or 0, 0 or 1)  # 1 1 1

print(2 and 2, 2 and 0, 0 and 2)  # 2 0 0
print(2 or 2, 2 or 0, 0 or 2)  # 2 2 2

# 空字符串('')为假，非空字符串为真。非零的数为真；
# x and y, x为真返回y, x为假返回x
# x or y, x为真返回x, x为假返回y
print('1' and '1', '1' and '0', '0' and '1')  # 1 0 1
print('1' or '1', '1' or '0', '0' or '1')  # 1 1 0

print('' and '', '' and 'b', 'b' and '', sep='|')  # ||
print(' ' and ' ', ' ' and 'b', 'b' and ' ', sep='|')  # space|b|space
print('' or '', '' or 'b', 'b' or '', sep='|')  # |b|b
