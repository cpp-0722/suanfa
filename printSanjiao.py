#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author cpp
    @Date 2021/9/30 16:41
    @Describe 
    @Version 1.0
"""
import numpy as np

if __name__ == '__main__':

    try:
        n = eval(input("输入数字："))

        if n <= 0:
            print("请输入大于0的数。")
        a = np.ones((n+1, n+1))

        k = 1
        for i in range(1, n + 1):
            for j in range(1, n + 2 - i):
                a[i - 1 + j][j] = k
                k = k + 1
        for i in range(1, n + 1):
            print()
            for j in range(1, i + 1):
                print(int(a[i][j]), end=' ')
    except EOFError:
        print("输入错误！")
