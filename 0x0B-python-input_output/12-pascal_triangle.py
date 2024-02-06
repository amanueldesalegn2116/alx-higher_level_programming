#!/usr/bin/python3


def pascal_triangle(n):
    if n <= 0:
        return []
    temp = []
    l = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if i == 0 or j == 0 or i == j:
                row.append(1)
            else:
                row.append(l[j] + l[j - 1])
        l = row
        temp.append(row)
    return temp
