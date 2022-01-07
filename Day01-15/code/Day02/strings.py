"""
字符串常用操作

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

str1 = 'hello, world!'
print('字符串的长度是:', len(str1))
print('单词首字母大写: ', str1.title())
print('字符串变大写: ', str1.upper())
# str1 = str1.upper()
print('字符串是不是大写: ', str1.isupper())
print('字符串是不是以hello开头: ', str1.startswith('hello'))
print('字符串是不是以hello结尾: ', str1.endswith('hello'))
print('字符串是不是以感叹号开头: ', str1.startswith('!'))
print('字符串是不是一感叹号结尾: ', str1.endswith('!'))
str2 = '- \u9a86\u660a'
str3 = str1.title() + ' ' + str2.lower()
print(str3)

print("\njoin():")
_tuple = ("a", "b", "c")
print(' * '.join(_tuple))
print("字符串格式化:")  # 可参考https://www.runoob.com/python/att-string-format.html
s = "我是{}, 我今年{}岁。".format('mary', 18)  # 需按顺序传入
print(s)  # 我是mary, 我今年18岁。

s = "我是{1}, 我今年{0}岁。".format(18, 'mary')  # 需按下标传入
print(s)  # 我是mary, 我今年18岁。

s = "我是{name}, 我今年{old}岁。".format(old=18, name='mary')  # 需键值对传入
print(s)  # 我是mary, 我今年18岁。

s = "我是{name}, 我今年{old}岁。".format(**{'old': 18, 'name': 'mary'})  # 需字典传入，【用 ** 标志将这个字典以关键字参数的方式传入】
print(s)  # 我是mary, 我今年18岁。

# ^, <, > 分别是居中、左对齐、右对齐，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。
# + 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格
# b、d、o、x 分别是二进制、十进制、八进制、十六进制
s = "我是{0[name]:_^6s}, 我今年{0[old]:_^6d}岁。".format({'old': 18, 'name': 'mary'})  # 可以传入一个字典，用中括号( [] )访问它的键
print(s)  # 我是_mary_, 我今年__18__岁。

s = "酒精的度数是{:.2f}%".format(47)  # 字段名后允许可选的 : 和格式指令。这允许对值的格式化加以更深入的控制
print(s)  # 酒精的度数是47.00%

k = ("name", "mh")
v = "名字：{0},name:{1}".format(*k)
print(v)
