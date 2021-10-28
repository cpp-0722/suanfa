#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author cpp
    @Date 2021/10/21 20:02
    @Describe 
    @Version 1.0
"""
import numpy as np


def serve(n):
    matrix = np.zeros((n, n))
    i = 0
    j = int((n - 1) / 2)
    x = 1
    while x <= (n * n):
        matrix[i][j] = x
        x = x + 1
        i1 = i
        j1 = j
        i = i - 1
        j = j - 1
        if i == -1:
            i = n - 1
        if j == -1:
            j = n - 1
        if matrix[i][j] != 0:
            i = i1 + 1
            j = j1

    print(matrix)


if __name__ == '__main__':
    try:
        n = eval(input("请输入奇数："))
        if n % 2 == 0:
            print("请输入奇数！")
        else:
            serve(n)

    except Exception:
        print("请输入奇数！")
