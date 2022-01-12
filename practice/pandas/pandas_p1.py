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
    return pd.read_excel(io='C:/Users/Administrator/Desktop/报警负责人.xlsx', sheet_name='Sheet1', header=1)


# http://www.pypandas.cn/docs/getting_started/dsintro.html#series
def create_series():
    # pd.Series(data, index=index)
    # data 标量值，字典，多维数组
    # data 是多维数组时，index 长度必须与 data 长度一致。没有指定 index 参数时，创建数值型索引，即 [0, ..., len(data) - 1]
    s = pd.Series(('三', '四', '五'), )
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
    print(s)
    print(s.index)  # RangeIndex(start=0, stop=3, step=1)
    print(s.index.values)  # [0 1 2]
    print(s.index.shape)  # (3,)
    return s


if __name__ == '__main__':
    series = create_series()

    # DataFrame
    df = excel_read()
    print(df)
    # Index(['值班人员表', 'Unnamed: 1', 'Unnamed: 2'], dtype='object')
    print(df.columns)
    # 3行，3列
    print(df.shape)
