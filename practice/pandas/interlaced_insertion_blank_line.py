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


def get_header_list_dict(date_frame, headers):
    """
    获取字典, key<header> : value:<column_list>
    """
    return {header: date_frame[header] for header in headers}


def structure_data_frame(headers, column_list_dict, index, target_column, target_column_value):
    dic = {header: str(column_list_dict[header][index]) for _, header in enumerate(headers)}
    dic[target_column] = str(target_column_value)
    return DataFrame(dic, index=range(0, 1))


def read_excel(path='测试.xlsx', sheet_name="Sheet1", target_column="商家编码"):
    if sheet_name is None:
        sheet_name = 'Sheet1'
    df_dict = pd.read_excel(path, sheet_name)
    df = DataFrame(df_dict, index=range(len(df_dict)))

    # 获取标题
    headers = df.head(0).columns  # Index(['姓名', '年龄', '商家id', 'Unnamed: 3'], dtype='object')

    # 获取key-标题, value-列值列表
    column_list_dict = get_header_list_dict(df, headers)
    # 获取目标列
    target_list = column_list_dict.get(target_column)
    if target_list is None:
        raise ValueError(f'目标列【{target_column}】不存在！')

    # print(f'目标列：{target_column}')
    target_series = df[target_column]

    length = len(list(target_series.items()))  # 数据行长度
    index = 0  # 原始数据下标
    insert_index = 0  # 插入行下标

    for item in target_series.items():
        insert_index += 1
        # print(f'index: {index}, length: {length} , insert_index: {insert_index}')
        if index >= length:
            break
        raw_code = str(item[1]).strip()

        if raw_code is not None and raw_code.find('+') != -1:
            split_tuple = raw_code.split('+')  # 需要拆解的列
            for header in headers:
                if target_column != header:
                    df.loc[insert_index - 1, header] = str(df.loc[insert_index - 1, header])
            df.loc[insert_index - 1, target_column] = str(split_tuple[0])  # 修改原始行

            # 新增行
            df_add1 = structure_data_frame(headers, column_list_dict, index, target_column, split_tuple[1])
            df = insert(df, insert_index, df_add1)
            insert_index += 1

            if len(split_tuple) > 2:
                for i in range(2, len(split_tuple)):
                    # 新增行2
                    df_add2 = structure_data_frame(headers, column_list_dict, index, target_column, split_tuple[i])
                    df = insert(df, insert_index, df_add2)
                insert_index += 1

        # 需转换为字符串类型，避免科学计数法的影响
        elif raw_code is not None:
            for header in headers:
                if target_column != header:
                    df.loc[insert_index - 1, header] = str(df.loc[insert_index - 1, header])
            df.loc[insert_index - 1, target_column] = str(raw_code)  # 修改原始行

        index += 1
    return df


if __name__ == '__main__':
    path = ''
    while path is None or path == '':
        path = str(input("请输入【excel路径及名称】[如：C:/Users/Administrator/Desktop/测试.xlsx]:"))
    if path.find('/') != -1:
        path = path.replace("/", "\\")

    st_name = str(input("请输入【Sheet】名称[如：Sheet1（默认）]:"))
    if st_name == '' or st_name is None:
        st_name = "Sheet1"

    target_col = str(input("请输入【拆解列名称】[如：商家编码（默认）]:"))
    if target_col == '' or target_col is None:
        target_col = "商家编码"

    data = read_excel(path, st_name, target_col)
    # print(data)
    DataFrame(data).to_excel('修改后.xlsx', sheet_name='Sheet1', index=False, header=True)
