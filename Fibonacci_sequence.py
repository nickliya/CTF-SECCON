# coding=utf-8
# create by 401219180 2017/01/09

# Run me!
# -----  RunMe.py
import sys

sys.setrecursionlimit(99999)


def f(n):
    return n if n < 2 else f(n - 2) + f(n - 1)


# print "SECCON{" + str(f(11011))[:32] + "}"
# -----

# 解法1 python list提供给的append轻松解出
a = [0, 1]


def f1(n):
    if n > 2:
        x = 0
        for i in range(n - 2):
            a.append(a[i] + a[i + 1])
            x += 1
        return a[-1]
    else:
        return a[-1]


print "SECCON{" + str(f1(11011))[:32] + "}"

# 解法2 更改原来的f(n)递归，重写for循环
b = 0
c = 1
d = 0


def f2(n):
    global b, c, d
    if n > 2:
        for i in range(n - 2):
            d = b + c
            b = c
            c = d
        return d
    else:
        return b + c


print "SECCON{" + str(f2(11011))[:32] + "}"
