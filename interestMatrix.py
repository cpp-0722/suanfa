#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author cpp
    @Date 2021/10/21 18:16
    @Describe 
    @Version 1.0
    输出形如: 0 1 1 1 0
            2 0 1 0 4
            2 2 0 4 4
            2 0 3 0 4
            0 3 3 3 0
"""
import numpy as np


def generate(n):
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i < j and i + j < n-1:
                matrix[i][j] = 1
            elif i < j and i + j > n-1:
                matrix[i][j] = 4
            elif i > j and i + j > n-1:
                matrix[i][j] = 3
            elif i > j and i + j < n-1:
                matrix[i][j] = 2
    print(matrix)


if __name__ == '__main__':
    try:
        n = eval(input("请输入："))
        generate(n)
    except Exception:
        print("请输入整数！")


