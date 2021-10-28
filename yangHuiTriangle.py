#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author cpp
    @Date 2021/10/28 19:37
    @Describe 
    @Version 1.0
"""


def coeff(a, n):
    if n == 1:
        a[0] = 1
        a[1] = 1
    else:
        coeff(a, n - 1)
        a[n] = 1
        i = n-1
        while i >= 1:
            a[i] = a[i] + a[i - 1]
            i = i - 1
        a[0] = 1


if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n+1):
        a.append(1)

    coeff(a,n)
    print(a)
