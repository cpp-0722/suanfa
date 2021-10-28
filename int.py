#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author cpp
    @Date 2021/10/7 19:22
    @Describe 
    @Version 1.0
    整数划分
"""


def divinteger(n, m):
    if n == 1 or m == 1:
        return 1
    elif n < m:
        return divinteger(n, n)
    elif n == m:
        return 1 + divinteger(n, n - 1)
    else:
        return divinteger(n, m - 1) + divinteger(n - m, m)


def main():
    n = eval(input("请输入n的值："))
    if int(n):
        print("请输入整数")
        return
    if n < 1:
        print("输入的参数有误！")
    num = divinteger(n, n)
    print("%d 的分划数为：%d" % (n, num))


if __name__ == '__main__':
    main()
