#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author cpp
    @Date 2021/10/7 15:40
    @Describe 
    @Version 1.0
"""


def server(start, n):
    if n == 0:
        return

    for j in range(1, n + 1):
        reList.append(j)
        server(start + 1, n - j)


if __name__ == '__main__':
    num = 3
    reList = []
    server(1, num)
    x = 0
    z = 0
    for i in range(len(reList)):
        z = z + reList[i]
        if z == num:
            z = 0
            for j in range(x, i + 1):
                if j == i:
                    x = j + 1
                    print(reList[j])
                else:
                    print("{}+".format(reList[j]), end='')
