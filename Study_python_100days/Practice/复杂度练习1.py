# 输入一个正整数x,循环打印出1到x的所有真正数
import time


def printA(x):
    if x:
        printA(x - 1)
        print(x)


def printB(x):
    for i in range(1, x + 1):
        print(i)


def printC(x):
    i = 0
    while i < x:
        i += 1
        print(i)


if __name__ == '__main__':
    t1 = time.time()
    printA(995)
    t2 = time.time()
    printB(995)
    t3 = time.time()
    printC(995)
    t4 = time.time()
    print("A计算耗费时间%f秒" % (t2 - t1))
    print("B计算耗费时间%f秒" % (t3 - t2))
    print("C计算耗费时间%f秒" % (t4 - t3))
