#递归斐波那契数列
def fibonacci_1(n):
    if n < 3:
        return 1
    val = fibonacci_1(n - 1) + fibonacci_1(n - 2)
    return val

#递归阶乘
def fibonacci_2(n):
    if n == 1 or n == 0:
        print(1,end='\t')
        return 1
    result = fibonacci_2(n - 1) * n
    print(result,end="\t")
    return result