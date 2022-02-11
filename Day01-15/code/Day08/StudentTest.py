#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Version : 0.1
Author  : yx
Date    : 2022-01-19
"""


class StudentTest(object):

    def __init__(self, name: str, age: int):
        """

        Args:
            name (str): 名称
            age (int): 年龄
        """
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')

    def watch_movie(self):
        if self.age < 18:
            print(f'{self.name}只能看熊出没')
        else:
            print(f'{self.name}可以看其它的')


def main():
    s1 = StudentTest('jj', 30)
    s1.study('ppp')
    s1.watch_movie()


if __name__ == '__main__':
    main()
