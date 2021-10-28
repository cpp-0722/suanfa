#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author cpp
    @Date 2021/9/29 18:49
    @Describe 
    @Version 1.0
"""

if __name__ == '__main__':
    do = []
    with open('chinese.txt', 'r', encoding='utf-8') as f:
        cha = f.read()

    chinese = cha.split(" ")

    with open('math.txt', 'r', encoding='utf-8') as f:
        ma = f.read()

    math = ma.split(" ")

    with open('english.txt', 'r', encoding='utf-8') as f:
        eng = f.read()

    english = eng.split(" ")

    for i in chinese:
        for j in math:
            for z in english:
                if i == j == z:
                    do.append(i)

    print(do)


