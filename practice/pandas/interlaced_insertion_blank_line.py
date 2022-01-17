#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/17 10:36
# @Author  : yx.Jiang
# @File    : interlaced_insertion_blank_line.py
# @Des     : 隔行插入行并填充数据
import pandas as pd
from pandas import DataFrame


def insert(df, i, df_add):
    # 指定第i行插入一行数据
    df1 = df.iloc[:i, :]
    df2 = df.iloc[i:, :]
    df_new = pd.concat([df1, df_add, df2], ignore_index=True)
    return df_new


# data = {
#     'name': ['li', 'gg', 'zz'],
#     'age': [20, 21, 22],
#     'height': [170, 178, 174]}
# df = pd.DataFrame(data)
# print('df:')
# print(df)
# df_add = pd.DataFrame({'name': ['yy'], 'age': [25], 'height': [168]})
# # 在第2行插入一条新的数据
# df_new = insert(df, 1, df_add)
# print('df_new:')
# print(df_new)

"""
df:
  name  age  height
0   li   20     170
1   gg   21     178
2   zz   22     174
df_new:
  name  age  height
0   li   20     170
1   yy   25     168
2   gg   21     178
3   zz   22     174
"""


def read_excel(path='测试.xlsx', sheet_name="Sheet1"):
    if sheet_name is None:
        sheet_name = 'Sheet1'
    df_dict = pd.read_excel(path, sheet_name)
    df = DataFrame(df_dict, index=range(len(df_dict)))

    businesses = df['商家id']
    names = df['姓名']
    ages = df['年龄']
    headers = df.head(0).columns  # Index(['姓名', '年龄', '商家id', 'Unnamed: 3'], dtype='object')

    length = len(list(businesses.items()))  # 数据行长度
    index = 0  # 原始数据下标
    insert_index = 0  # 插入行下标

    for item in businesses.items():
        insert_index += 1
        # print(f'index: {index}, length: {length} , insert_index: {insert_index}')
        if index >= length:
            break
        raw_code = item[1]

        if raw_code.find('+') != -1:
            split_tuple = raw_code.split('+')  # 需要拆解的列
            df.loc[insert_index - 1, '商家id'] = split_tuple[0]  # 修改原始行

            # 新增行
            df_add1 = DataFrame(
                {headers[0]: [names[index]], headers[1]: [ages[index]], headers[2]: [split_tuple[1]]},
                index=range(0, 1))
            df = insert(df, insert_index, df_add1)

            df_add2 = DataFrame(
                {headers[0]: [names[index]], headers[1]: [ages[index]], headers[2]: [split_tuple[2]]},
                index=range(0, 1))
            insert_index += 1
            df = insert(df, insert_index, df_add2)

            index += 1
            insert_index += 1
    return df


if __name__ == '__main__':
    path = ''
    while path is None or path == '':
        path = str(input("请输入excel的路径及名称[如：C:/Users/Administrator/Desktop/测试.xlsx]:"))
    if path.find('/') != -1:
        path = path.replace("/", "\\")

    st_name = str(input("请输入Sheet名称[如：Sheet1（默认）]:"))
    if st_name == '':
        st_name = None
    data = read_excel(path, st_name)
    DataFrame(data).to_excel('update.xlsx', sheet_name='Sheet1', index=False, header=True)
