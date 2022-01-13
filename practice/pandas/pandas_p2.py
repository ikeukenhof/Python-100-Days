#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/13 17:11
# @Author  : name
# @File    : pandas_p2.py
import pandas as pd

# 创建数据
# data_series = pd.Series([1, 2, 3, 4])  # 列表生成Series
# data_pd = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [5, 6, 7, 8]})  # 可用包含等长列表（数组/Series）的字典生成DataFrame
# 设置索引
data_series = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])  # 列表生成Series
print(data_series)
data_pd = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [5, 6, 7, 8]}, index=['a', 'b', 'c', 'd'])
print(data_pd)
# 分别查看值和索引
# print(data_series.index)
# print(data_pd.index)
# print(data_series.values)  # 一维数组
# print(data_pd.values)  # 二维数组

# 读取其他数据文件
# df_excel = pd.read_excel('file.xlsx', sheet_name='Sheet1')  # 读入excel文件
# df_csv = pd.read_csv('file.csv')  # 读入csv文件
# df_json = pd.read_json('file.json')

# 输出数据文件
# df.to_csv('save_file.csv')
# df.to_excel('save_file.xlsx')
# df.to_json('save_file.json')

# 插入新行
data_pd['new_col1'] = 'a'
print(f'插入新列：\n {data_pd}')
# data_pd.loc[data_pd.shape[1]] = ['row1', 'row2', 'row3']
# print(data_pd)
row_add = {'col1': 'row_1', 'col2': 'row_2', 'col3': 'row_3'}
data_pd = data_pd.append(row_add, ignore_index=True)
print(f'追加行:{data_pd}')

# 指定位置插入行
data_pd1 = data_pd.iloc[:2, :]
data_pd2 = data_pd.iloc[2:, :]
# index 的len 决定了插入的行数
index = [1]
# 要插入的行
row_to_add = pd.DataFrame(row_add, )
data_pd_concat = pd.concat((data_pd1, row_to_add, data_pd2), ignore_index=True)
print(f'指定行插入: \n {data_pd_concat}')
