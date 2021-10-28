#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author cpp
    @Date 2021/10/28 18:45
    @Describe 
    @Version 1.0
"""


def serveTriangle(a, b, c):
    flag = 0
    if a + b <= c and a + c <= b and b + c <= a:
        print("不能构成三角形")
    elif a == b == c:
        print("构成等边三角形")
    elif a == b or a == c or b == c:
        flag = 1
        print("构成等腰三角形")
    elif a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b:
        if flag:
            print("构成等腰直角三角形")
        else:
            print("构成直角三角形")
    else:
        print("构成一般三角形")


if __name__ == '__main__':
    print("请输入三条边")
    x = int(input("x:"))
    y = int(input("y:"))
    z = int(input("z:"))
    serveTriangle(x, y, z)
