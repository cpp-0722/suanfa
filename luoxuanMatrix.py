#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author cpp
    @Date 2021/10/21 18:30
    @Describe 
    @Version 1.0

    输出形如: 1  16 15 14 13
            2  17 24 23 12
            3  18 25 22 11
            4  19 20 21 10
            5  6  7  8  9
"""
import numpy as np


def server(n):
    k = 1
    martrix = np.zeros((n,n))
    for i in range(int(n/2)):
        for j in range(i,n-i-1):
            martrix[j][i] = k
            k = k +1
        for j in range(i,n-i-1):
            martrix[n-i-1][j] = k
            k = k + 1
        if 1:
            j = n - i-1
            while j > i :
                martrix[j][n - i-1] = k
                k = k +1
                j = j - 1
        if 1:
            j = n - i-1
            while j > i:
                martrix[i][j] = k
                k = k +1
                j = j - 1

    if (n % 2==1):
        i = int((n -1)/2)
        martrix[i][i] = k
    print(martrix)


if __name__ == '__main__':

    try:
        n = eval(input("请输入："))
        server(n)
    except Exception:
        print("请输入整数！")


