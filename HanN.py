#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author cpp
    @Date 2021/9/29 17:54
    @Describe 
    @Version 1.0


    首先把三根柱子按顺序排成品字型，把所有的圆盘按从大到小的顺序放在柱子A上。
    根据圆盘的数量确定柱子的排放顺序：若n为偶数，按顺时针方向依次摆放 A B C；
    若n为奇数，按顺时针方向依次摆放 A C B。
    （1）按顺时针方向把圆盘1从现在的柱子移动到下一根柱子，即当n为偶数时，若圆盘1在柱子A，则把它移动到B；
        若圆盘1在柱子B，则把它移动到C；若圆盘1在柱子C，则把它移动到A。
    （2）接着，把另外两根柱子上可以移动的圆盘移动到新的柱子上。
        即把非空柱子上的圆盘移动到空柱子上，当两根柱子都非空时，移动较小的圆盘
        这一步没有明确规定移动哪个圆盘，你可能以为会有多种可能性，其实不然，可实施的行动是唯一的。
    （3）反复进行（1）（2）操作，最后就能按规定完成汉诺塔的移动。

"""

n = eval(input("请输入："))
z = 0


# 第一步
def Part1(a, b, c, A, B, C):
    global z
    if len(a) != 0 and a[-1] == n - 1:
        print(A + "->" + B)
        b.append(a[-1])
        a.pop()
        z = 2
    elif len(b) != 0 and b[-1] == n - 1:
        print(B + "->" + C)
        c.append(b[-1])
        b.pop()
        z = 3
    else:
        print(C + "->" + A)
        a.append(c[-1])
        c.pop()
        z = 1


# 第二步
def Part2(a, b, c, A, B, C):
    if z == 1:
        if len(b) and len(c):
            if b[-1] > c[-1]:
                print(B + "->" + C)
                c.append(b[-1])
                b.pop()
            else:
                print(C + "->" + B)
                b.append(c[-1])
                c.pop()
        elif len(b):
            print(B + "->" + C)
            c.append(b[-1])
            b.pop()
        elif len(c):
            print(C + "->" + B)
            b.append(b[-1])
            c.pop()

    elif z == 2:
        if len(a) and len(c):
            if a[-1] > c[-1]:
                print(A + "->" + C)
                c.append(a[-1])
                a.pop()
            else:
                print(C + "->" + A)
                a.append(c[-1])
        elif len(a):
            print(A + "->" + C)
            c.append(a[-1])
            a.pop()
        elif len(c):
            print(C + "->" + A)
            a.append(a[-1])
            c.pop()


    elif z == 3:
        if len(b) and len(a):
            if b[-1] > a[-1]:
                print(B + "->" + A)
                a.append(b[-1])
                b.pop()
            else:
                print(A + "->" + B)
                b.append(a[-1])
        elif len(b):
            print(B + "->" + A)
            a.append(b[-1])
            b.pop()
        elif len(a):
            print(A + "->" + B)
            b.append(a[-1])
            a.pop()


def SolveHan(a, b, c):
    if n % 2 == 0:
        while len(a) != 0 or len(b) != 0:
            Part1(a, b, c, 'A', 'B', 'C')
            Part2(a, b, c, 'A', 'B', 'C')
    else:
        while len(a) != 0 or len(b) != 0:
            Part1(a, c, b, 'A', 'C', 'B')
            Part2(a, c, b, 'A', 'C', 'B')


if __name__ == '__main__':
    z = 0
    A = []
    B = []
    C = []
    # init A
    for i in range(n):
        A.append(i)

    SolveHan(A, B, C)
