"""
Python的内置函数
- 数学相关: abs / divmod / pow / round / min / max / sum
- 序列相关: len / range / next / filter / map / sorted / slice / reversed
- 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
- 数据结构: dict / list / set / tuple
- 其他函数: all / any / id / input / open / print / type

Version: 0.1
Author: 骆昊
Date: 2018-03-05


对于字符串是否为空，以及比较(is、==)的问题：https://zhuanlan.zhihu.com/p/35219174
"""


def myfilter(mystr):
    # if mystr is None:
    if not mystr:
        return False
    return len(mystr) == 6


# help()
print(chr(0x9a86))  # 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符
print(hex(ord('骆')))  # ord：以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值；
# hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
print(abs(-1.2345))
print(round(-1.2345))  # 保留n位小数，默认0
print(pow(1.2345, 5))  # 返回x的y次方
fruits = ['orange', 'peach', 'durian', 'watermelon', None]
print(fruits[1:3])
print(fruits[slice(1, 3)])  # slice用于指定如何对序列进行裁切
fruits2 = list(filter(myfilter, fruits))
print(fruits)
print(fruits2)
