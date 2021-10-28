#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author cpp
    @Date 2021/9/23 18:35
    @Describe 
    @Version 1.0
"""

if __name__ == '__main__':
    do = []
    chinese = [1, 9, 6, 8, 4, 3, 7]
    math = [5, 2, 9, 1, 3, 7]
    english = [8, 1, 6, 7, 3, 5, 4, 9]
    for i in chinese:
        for j in math:
            for z in english:
                if i == j == z:
                    do.append(i)

    print(do)
