#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author cpp
    @Date 2021/9/30 15:32
    @Describe 
    @Version 1.0
"""

import numpy as np

if __name__ == '__main__':

    na = 0  # 判断有没有鞍点
    try:

        x, y = map(int, input("输入维度，空格分开：").split())
        a = np.ones((x, y))
        print("输入矩阵：")
        for i in range(x):
            for j in range(y):
                a[i][j] = eval(input())
        print("输入的矩阵：")
        print(a)
        for i in range(x):
            minA = 999
            maxB = 0
            minJ = 0
            for j in range(y):

                if minA > a[i][j]:
                    minA = a[i][j]
                    minJ = j  # 记录下标
            for k in range(x):
                for z in range(y):
                    if maxB < a[k][minJ]:
                        maxB = a[k][minJ]
            if minA == maxB:
                na = 1
                print(int(minA))
        if na == 0:
            print("没有鞍点")

    except (EOFError, Exception):
        print("输入异常")
