import time

"""
def outer(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print("{}".format(func.__name__))
        print((time.time() - start)*1000)

    return inner


@outer
def calc_num(n):
    for i in range(n):
        print("hello world ! \t")
    return


calc_num(1000)
"""


def decorator_with_arguments(arg):  # 装饰器第1层，带参数的装饰，接受装饰器的参数
    def actual_decorator(func):  # 装饰器第2层，接受装饰的函数
        def wrapper(*args, **kwargs):  # 装饰器第3层，添加开始执行传入函数之前或之后的操作
            print(f"Decorator argument: {arg}")  # 执行传入函数执行的操作：打印一行文字
            func(*args, **kwargs)  # 开始执行传入的函数

        return wrapper  # 装饰器第2层返回第3层函数

    return actual_decorator  # 装饰器第1层返回第2层函数


@decorator_with_arguments("Custom Argument")  # 带参数的装饰器
def say_hello(name):  # 被装饰的函数
    print(f"Hello, {name}!")  # 函数内部执行的操作：打印传输参数的名字


say_hello("Alice")  # 调用被装饰的函数
