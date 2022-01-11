"""
生成斐波拉切数列

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    f = [1, 1]
    for i in range(2, 20):
        f += [f[i - 1] + f[i - 2]]
        # f.append(f[i - 1] + f[i - 2])
    for val in f:
        print(val, end=' ')


'''
list[start_index: stop_index: step]
起始位置 : start_index (空时默认为 0)。
终点位置: stop_index (空时默认为列表长度) 需要注意起点与终点索引的位置关系。
步长: step (空时默认为 1，不能为 0)。
'''


def cut():
    str2 = 'abc123456'
    # 从字符串中取出指定位置的字符(下标运算)
    print(str2[2])  # c
    # 字符串切片(从指定的开始索引到指定的结束索引)
    print(str2[2:5])  # c12
    print(str2[2:])  # c123456
    print(str2[2::2])  # c246
    print(str2[::2])  # ac246
    # 【步长为负数时，列表先翻转，再截取】
    print(str2[::-1])  # 654321cba
    # [-3,-1)
    print(str2[-3:-1])  # 45


def enumerate_list():
    for index, value in enumerate([i for i in range(1, 10)]):
        print(f'{index}, {value}')


if __name__ == '__main__':
    main()
    # cut()
    # enumerate_list()
