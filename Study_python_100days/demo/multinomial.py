# 计算出多项式f(x)=a_0 + a_1*n^1 + ... a_x-1*n^x-1 + a_x*n^x
import time


# 定义多项式计算函数,n为a的系数,也是x的幂,a和x为固定常量
def multinomialA(n, a, x):
    # 当a的系数为0时结果为0,所以递归第1项结果为0
    res = a * 0
    # 因为第1项为0,为固定已知结果,所以正式计算从第2项开始,即当n为1时开始计算
    i = 1
    # 遍历n,判断条件
    while i < n + 1:
        # 结果等于上次的结果加上遍历的i为系数和幂的a*i和x^i的结果
        res += a * i * pow(x, i)
        # 循环控制条件,i每次循环后+1
        i += 1
    # 打印最终结果res
    print(res)


# 根据题目提供的计算式化简可得到f(x)=a_0+x(a_1+x(...(a_n-1+x(a_n))...))
def multinomialB(n, a, x):
    # 根据化简式从里面开始往外面计算,首先计算a*n
    i = n
    res = a * n
    # 根据化简计算式得知,a_0结果为0所以忽略即可,只需要计算n>0的结果即可
    while i > 0 and i <= n:
        # 从化简计算式得知每次的结果等于a的系数n-1加上x乘以上次的结果
        res = a * (i - 1) + x * res
        # 循环控制条件,i每次循环后-1
        i -= 1
    # 打印最终结果res
    print(res)


if __name__ == '__main__':
    t1 = time.time()
    multinomialA(10000, 10, 10)
    t2 = time.time()
    multinomialB(10000, 10, 10)
    t3 = time.time()
    print("A计算式耗费时间%f秒" % (t2 - t1), end="\n")
    print("B计算式耗费时间%f秒" % (t3 - t2), end="\n")
