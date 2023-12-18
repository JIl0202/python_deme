# 创建列表测试数据
list_1 = [1, 2, 3]


# 创建生成器example
def example():
    print('starting . . .')
    yield list_1[1]
    print(list_1[2])
    raise StopIteration


# 将生成器创建对象
a = example()

# 通过next方法执行yeild关键字本句和之前的语句
print(a.__next__())
# print(next(a))
# 跟前一句效果一样

# 分割线
print('-' * 10)

# 通过next方法执行yeild关键字之后的语句
print(a.__next__())


# print(next(a,"Stop . . ."))
# 跟前一句效果一样

def foo(num):
    print("starting...")
    while num < 10:
        num += 1
        yield num
    while num >= 10:
        num -= 1
        yield num


for n in foo(20):
    print(n)

