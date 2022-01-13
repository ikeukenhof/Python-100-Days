#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/12 17:44
# @Author  : name
# @File    : pandas_p1.py
# @Link    : http://www.pypandas.cn/docs/getting_started/10min.html
import pandas as pd
from pandas import DataFrame
import numpy as np


def excel_read():
    # header = 1 可以理解为从 index=1开始读取excel数据
    df = pd.read_excel(io='C:/Users/Administrator/Desktop/报警负责人.xlsx', sheet_name='Sheet1', header=1)
    # DataFrame
    print(df)
    # Index(['值班人员表', 'Unnamed: 1', 'Unnamed: 2'], dtype='object')
    print(df.columns)
    # 3行，3列
    print(df.shape)
    return df


# http://www.pypandas.cn/docs/getting_started/dsintro.html#series
def create_series():
    # pd.Series(data, index=index)
    # data 标量值，字典，多维数组
    # data 是多维数组时，index 长度必须与 data 长度一致。没有指定 index 参数时，创建数值型索引，即 [0, ..., len(data) - 1]
    s = pd.Series(2.0, index=['a', 'b', 'c', 'd', 'e'])
    """
    a    2.0
    b    2.0
    c    2.0
    d    2.0
    e    2.0
    """
    print(s.array)
    """
    <PandasArray>
    [2.0, 2.0, 2.0, 2.0, 2.0]
    Length: 5, dtype: float64
    """
    # s = pd.Series(('三', '四', '五'), )
    """
    0    三
    1    四
    2    五
    """
    # s = pd.Series(('三', '四', '五'), index=['01', '02', '03'])
    """
    01    三
    02    四
    03    五
    """
    # s = pd.Series({'02': '张三', '03': '李四', '01': '王五'}, index=['01', '02', '03'])
    """
    01    王五
    02    张三
    03    李四
    """
    # s = pd.Series({'02': '张三', '03': '李四', '01': '王五'})
    """
    02    张三
    03    李四
    01    王五
    """
    print(f'Series：\n{s}')
    """
    0    三
    1    四
    2    五
    dtype: object
    """
    print(s.index)  # RangeIndex(start=0, stop=3, step=1)
    print(s.index.values)  # [0 1 2]
    print(s.index.shape)  # (3,)
    return s


def series_field(series):
    # Series 是扩展数组 (opens new window)，Series.to_numpy() (opens new window)返回的是 NumPy 多维数组。
    print(f'series.to_numpy()：{series.to_numpy()}')
    # 类似字典，可通过索引标签获取值；若key不存在则触发异常
    print(f"series['b']： {series['b']}")
    # get 方法可以提取 Series 里没有的标签，返回 None 或指定默认值：
    print(series.get('f'))  # None
    print(series.get('f', np.NAN))  # nan
    print(series * 2)
    """
        a    4.0
        b    4.0
        c    4.0
        d    4.0
        e    4.0
        dtype: float64
        """
    # 操作未对齐索引的 Series， 其计算结果是所有涉及索引的并集。如果在 Series 里找不到标签，运算结果标记为 NaN，即缺失值
    s = series[1:] + series[:-1]
    """
        a    NaN
        b    4.0
        c    4.0
        d    4.0
        e    NaN
        dtype: float64
        """
    print(s)
    # 可用dropna函数清除含有缺失值的标签(https://blog.csdn.net/qq_17753903/article/details/89817371)


# 用 Series 字典或字典生成 DataFrame
def create_dataFrame_by_series():
    d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
         'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
    df = pd.DataFrame(d)
    print(df)
    """
       one  two
    a  1.0  1.0
    b  2.0  2.0
    c  3.0  3.0
    d  NaN  4.0
    """
    df = pd.DataFrame(d, index=['d', 'b', 'a'])
    print(df)
    df = pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])
    print(df)
    # index 和 columns 属性分别用于访问行、列标签：
    print(pd.DataFrame(d).index)  # Index(['a', 'b', 'c', 'd'], dtype='object')
    print(pd.DataFrame(d).columns)  # Index(['one', 'two'], dtype='object')


# 用结构多维数组或记录多维数组生成 DataFrame
def create_dataFrame_by_array():
    data = np.zeros((2,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
    print(data)  # [(0, 0., b'') (0, 0., b'')]
    data[:] = [(1, 2., 'Hello'), (2, 3., "World")]
    print(data)  # [(1, 2., b'Hello') (2, 3., b'World')]


# 用列表字典生成 DataFrame
def create_dataFrame_by_list():
    l = [{'a': 1, 'b': 2}, {'a': 11, 'b': 22, 'c': 33}]
    print(pd.DataFrame(l))
    """
        a   b     c
    0   1   2   NaN
    1  11  22  33.0
    """
    print(pd.DataFrame(l, index=['fir', 'sec']))
    """
        a   b     c
    fir   1   2   NaN
    sec  11  22  33.0
    """
    pass


if __name__ == '__main__':
    # series_ = create_series()

    # series_field(series_)
    pass
    # create_dataFrame_by_series()
    # create_dataFrame_by_array()
    # create_dataFrame_by_list()
